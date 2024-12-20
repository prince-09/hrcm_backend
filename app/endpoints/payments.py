from fastapi import APIRouter, HTTPException
from app.schemas.payment import PaymentCreate, PaymentResponse
from app.crud.payment import create_payment, get_payment_by_id

router = APIRouter()

@router.post("/", response_model=PaymentResponse)
async def create_new_payment(payment: PaymentCreate):
    payment_id = await create_payment(payment.dict())
    created_payment = await get_payment_by_id(payment_id)
    if not created_payment:
        raise HTTPException(status_code=500, detail="Payment creation failed")
    return created_payment

@router.get("/{payment_id}", response_model=PaymentResponse)
async def get_payment(payment_id: str):
    payment = await get_payment_by_id(payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment
