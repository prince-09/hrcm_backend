from app.db.connection import database
from bson.objectid import ObjectId

async def create_payment(payment_data: dict):
    result = await database.payments.insert_one(payment_data)
    return str(result.inserted_id)

async def get_payment_by_id(payment_id: str):
    payment = await database.payments.find_one({"_id": ObjectId(payment_id)})
    if payment:
        payment["id"] = str(payment["_id"])
        del payment["_id"]
    return payment

async def get_payments():
    payments = await database.payments.find()
    return payments
