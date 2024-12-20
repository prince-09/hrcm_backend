from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ClaimBase(BaseModel):
    patient_id: int
    provider: str
    date_of_service: datetime
    total_charge: float
    status: str
    submitted_at: datetime
    paid_at: Optional[datetime] = None  # Make this optional
    denial_reason: Optional[str] = None  # Make this optional

class ClaimCreate(ClaimBase):
    pass

class Claim(ClaimBase):
    id: str

    class Config:
        orm_mode = True
