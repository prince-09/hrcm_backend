from app.db.connection import database
from bson.objectid import ObjectId

async def create_claim(claim_data: dict):
    result = await database.claims.insert_one(claim_data)
    return str(result.inserted_id)

async def get_claim_by_id(claim_id: str):
    claim = await database.claims.find_one({"_id": ObjectId(claim_id)})
    if claim:
        claim["id"] = str(claim["_id"])
        del claim["_id"]
    return claim

async def get_claims():
    claims = await database.claims.find(filter={})
    return claims

async def update_claim(claim_id: str, update_data: dict):
    result = await database.claims.update_one(
        {"_id": ObjectId(claim_id)}, {"$set": update_data}
    )
    return result.modified_count > 0

async def delete_claim(claim_id: str):
    result = await database.claims.delete_one({"_id": ObjectId(claim_id)})
    return result.deleted_count > 0
