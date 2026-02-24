import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ---------- APP ----------
app = FastAPI()

# CORS (React ↔ Backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- DB CONFIG ----------
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = "ASPV"
COLLECTION = "ASPV"


def get_products_from_db():
    try:
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
        client.server_info()
        db = client[DB_NAME]
        return list(db[COLLECTION].find({}, {"_id": 0}))
    except ServerSelectionTimeoutError:
        return None


# ---------- ROUTES ----------
@app.get("/")
def root():
    return {"status": "Backend running"}


@app.get("/products")
def get_products():
    products = get_products_from_db()

    if products:
        return products

    # fallback (always safe)
    return [
        {
            "name": "Tata Salt",
            "category": "Groceries",
            "price": 28
        },
        {
            "name": "Surf Excel",
            "category": "Detergent",
            "price": 110
        }
    ]