from app.db.connection import database
from bson.objectid import ObjectId

async def create_adjustment(adjustment_data: dict):
    result = await database.adjustments.insert_one(adjustment_data)
    return str(result.inserted_id)

async def get_adjustment_by_id(adjustment_id: str):
    adjustment = await database.adjustments.find_one({"_id": ObjectId(adjustment_id)})
    if adjustment:
        adjustment["id"] = str(adjustment["_id"])
        del adjustment["_id"]
    return adjustment

async def get_adjustments():
    adjustments = await database.adjustments.find()
    return adjustments
