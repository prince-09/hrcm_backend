from pydantic import BaseModel

class AdjustmentCreate(BaseModel):
    claim_id: str
    amount: float
    reason: str

class AdjustmentResponse(BaseModel):
    id: str
    claim_id: str
    amount: float
    reason: str

    class Config:
        orm_mode = True
