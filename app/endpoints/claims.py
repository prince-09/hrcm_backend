from fastapi import APIRouter, HTTPException
from app.schemas.claim import ClaimCreate, ClaimResponse
from app.crud.claim import create_claim, get_claim_by_id, update_claim

router = APIRouter()

@router.post("/", response_model=ClaimResponse)
async def create_new_claim(claim: ClaimCreate):
    claim_id = await create_claim(claim.dict())
    created_claim = await get_claim_by_id(claim_id)
    if not created_claim:
        raise HTTPException(status_code=500, detail="Claim creation failed")
    return created_claim

@router.get("/{claim_id}", response_model=ClaimResponse)
async def get_claim(claim_id: str):
    claim = await get_claim_by_id(claim_id)
    if not claim:
        raise HTTPException(status_code=404, detail="Claim not found")
    return claim
