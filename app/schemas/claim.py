from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ClaimCreate(BaseModel):
    patient_id: int
    provider: str
    date_of_service: datetime
    total_charge: float
    status: str  # Options: "Pending", "Paid", "Denied"
    submitted_at: datetime
    paid_at: Optional[datetime] = None  # Provide a default value
    denial_reason: Optional[str] = None  # Provide a default value

class ClaimResponse(BaseModel):
    id: str
    patient_id: int
    provider: str
    date_of_service: datetime
    total_charge: float
    status: str
    submitted_at: datetime
    paid_at: Optional[datetime] = None
    denial_reason: Optional[str] = None

    class Config:
        orm_mode = True
