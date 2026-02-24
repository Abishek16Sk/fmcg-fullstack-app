import pymongo
import gridfs
from bson import ObjectId
import requests
from io import BytesIO
from PIL import Image


client = pymongo.MongoClient('mongodb+srv://ASPV:ASPV@aspv.lxffi.mongodb.net/?retryWrites=true&w=majority&appName=ASPV')
db = client['ASPV'] 
products_collection = db['New']  
fs = gridfs.GridFS(db)  

def upload_product(name, category, price, description, image_path):
  
    img = Image.open(image_path)
    
    
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG') 
    img_byte_arr.seek(0)

   
    image_id = fs.put(img_byte_arr)

    
    product = {
        "name": name,
        "category": category,
        "price": price,
        "description": description,
        "image_id": image_id  
    }

  
    result = products_collection.insert_one(product)
    print(f"Product '{name}' uploaded successfully with ID: {result.inserted_id}")

def add_more_products():
    while True:  
        name = input("Enter product name: ")
        category = input("Enter product category: ")
        price = float(input("Enter product price: "))
        description = input("Enter product description: ")
        image_path = input("Enter image file path: ")

        upload_product(name, category, price, description, image_path)
        
      
        add_more = input("Do you want to add more products? (Y/N): ").strip().upper()
        if add_more != 'Y':
            print("Product addition process completed.")
            break 

if __name__ == '__main__':
    add_more_products()