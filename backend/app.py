from flask import Flask, jsonify, send_file
import pymongo
import gridfs
from bson import ObjectId
from io import BytesIO
import base64
from PIL import Image
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)  


client = pymongo.MongoClient('mongodb+srv://ASPV:ASPV@aspv.lxffi.mongodb.net/?retryWrites=true&w=majority&appName=ASPV')
db = client['ASPV'] 
products_collection = db['New']
fs = gridfs.GridFS(db)


@app.route('/', methods=['GET'])
def get_products():
    products = []
    image_count = 0

    
    cursor = products_collection.find()  
    total_products_in_db = products_collection.count_documents({})  
    
    for product in cursor:
        product_data = {
            "id": str(product["_id"]),
            "name": product["name"],
            "category": product["category"],
            "price": product["price"],
            "description": product["description"],
            "image": get_image_data(product["image_id"])  
        }
        products.append(product_data)

      
        if product.get("image_id"):
            image_count += 1

    fetched_product_count = len(products)

    
    print(f"Total Products in Database: {total_products_in_db}")
    print(f"Total Products Fetched: {fetched_product_count}")
    print(f"Products with Images: {image_count}")

    return jsonify({
        "total_products_in_db": total_products_in_db,
        "fetched_product_count": fetched_product_count,
        "image_count": image_count,
        "products": products
    })


def get_image_data(image_id):
    
    image_file = fs.get(ObjectId(image_id))
    img = Image.open(image_file)

    
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')  
    img_byte_arr.seek(0)
    encoded_image = base64.b64encode(img_byte_arr.read()).decode('utf-8')

    return encoded_image

if __name__ == '__main__':
    app.run(debug=True, port = 5000)
