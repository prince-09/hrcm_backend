from pydantic import BaseModel
from datetime import datetime

class PaymentCreate(BaseModel):
    claim_id: str
    amount: float
    date: datetime
    payer: str

class PaymentResponse(BaseModel):
    id: str
    claim_id: str
    amount: float
    date: datetime
    payer: str

    class Config:
        orm_mode = True
