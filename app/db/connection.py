from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ConnectionFailure
from app.config import settings

client = AsyncIOMotorClient(settings.MONGODB_URI)
database = client[settings.MONGODB_DB]

# Test the connection at startup
try:
    client.admin.command("ping")
    print("Connected to MongoDB!")
except ConnectionFailure:
    print("Failed to connect to MongoDB!")
