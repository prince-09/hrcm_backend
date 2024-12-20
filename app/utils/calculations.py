from app.db.connection import database

async def calculate_days_in_ar():
    claims = database.claims.find({"status": "Paid"})
    total_days = 0
    count = 0
    async for claim in claims:
        submitted_at = claim["submitted_at"]
        paid_at = claim["paid_at"]
        if submitted_at and paid_at:
            total_days += (paid_at - submitted_at).days
            count += 1
    return total_days / count if count > 0 else 0

async def calculate_denial_rate():
    total_claims = await database.claims.count_documents({})
    denied_claims = await database.claims.count_documents({"status": "Denied"})
    return (denied_claims / total_claims) * 100 if total_claims > 0 else 0

async def calculate_payment_ratio():
    total_charges = 0
    total_payments = 0
    claims = database.claims.find({})
    async for claim in claims:
        total_charges += claim["total_charge"]
    payments = database.payments.find({})
    async for payment in payments:
        total_payments += payment["amount"]
    return (total_payments / total_charges) * 100 if total_charges > 0 else 0
