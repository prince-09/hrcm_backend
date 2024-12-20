from fastapi import APIRouter, HTTPException
from app.utils.calculations import calculate_days_in_ar, calculate_denial_rate, calculate_payment_ratio
from app.crud.claim import get_claims
from app.crud.payment import get_payments
from app.crud.adjustment import get_adjustments
from datetime import datetime
from app.db.connection import database as db

router = APIRouter()

@router.get("/days-in-ar")
async def get_days_in_ar():
    days_in_ar = await calculate_days_in_ar()
    return {"average_days_in_ar": days_in_ar}

@router.get("/denial-rate")
async def get_denial_rate():
    denial_rate = await calculate_denial_rate()
    return {"denial_rate": f"{denial_rate:.2f}%"}

@router.get("/payment-ratio")
async def get_payment_ratio():
    payment_ratio = await calculate_payment_ratio()
    return {"payment_collection_ratio": f"{payment_ratio:.2f}%"}


@router.get("/claims")
async def get_claims_overview():
    try:
        # Convert the cursor to a list
        claims = await db.claims.find().to_list(None)  # None fetches all documents
        total_claims = len(claims)

        # Count claims by status
        paid_claims = sum(1 for c in claims if c["status"] == "Paid")
        denied_claims = sum(1 for c in claims if c["status"] == "Denied")
        pending_claims = sum(1 for c in claims if c["status"] == "Pending")

        # Calculate total charges, payments, and adjustments
        print("Prince in")
        total_charges = sum(c["total_charge"] for c in claims)
        print("Prince out")
        payments = await db.payments.find().to_list(None)
        total_payments = sum(p["amount"] for p in payments)
        adjustments = await db.adjustments.find().to_list(None)
        total_adjustments = sum(a["amount"] for a in adjustments)

        # Calculate Days in AR (Average)
        paid_claims_data = [
            (datetime.strptime(c["paid_at"], "%Y-%m-%d") - datetime.strptime(c["submitted_at"], "%Y-%m-%d")).days
            for c in claims
            if c["status"] == "Paid" and c["paid_at"]
        ]
        average_days_in_ar = sum(paid_claims_data) / len(paid_claims_data) if paid_claims_data else 0

        return {
            "totalClaims": total_claims,
            "paidClaims": paid_claims,
            "deniedClaims": denied_claims,
            "pendingClaims": pending_claims,
            "totalCharges": total_charges,
            "totalPayments": total_payments,
            "totalAdjustments": total_adjustments,
            "averageDaysInAR": average_days_in_ar,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/denials")
async def get_denials_overview():
    try:
        claims = await db.claims.find({"status": "Denied"}).to_list(None)
        total_denied_claims = len(claims)
        
        # Count denial reasons
        denial_reasons = {}
        for claim in claims:
            reason = claim.get("denial_reason", "Unknown")
            denial_reasons[reason] = denial_reasons.get(reason, 0) + 1

        
        # Calculate denial rate
        all_claims = await db.claims.find().to_list(None)
        total_claims = len(all_claims)
        denial_rate = round(((total_denied_claims / total_claims) * 100 if total_claims else 0), 2)

        return {
            "totalDeniedClaims": total_denied_claims,
            "denialReasons": denial_reasons,
            "denialRate": denial_rate
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/payments")
async def get_payments_overview():
    try:
        claims = await db.claims.find().to_list(None)
        total_charges = sum(c["total_charge"] for c in claims)

        # Payments and adjustments
        payments = await db.payments.find().to_list(None)
        total_payments = sum(p["amount"] for p in payments)

        # Calculate payment collection ratio
        payment_collection_ratio = round(((total_payments / total_charges) * 100 if total_charges else 0), 2)

        # Group payments by payer
        payer_payments = {}
        for payment in payments:
            payer = payment["payer"]
            payer_payments[payer] = payer_payments.get(payer, 0) + payment["amount"]

        return {
            "totalPayments": total_payments,
            "totalCharges": total_charges,
            "paymentCollectionRatio": payment_collection_ratio,
            "payerPayments": payer_payments
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
