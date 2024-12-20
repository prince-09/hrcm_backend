from fastapi import APIRouter, HTTPException
from app.schemas.adjustment import AdjustmentCreate, AdjustmentResponse
from app.crud.adjustment import create_adjustment, get_adjustment_by_id

router = APIRouter()

@router.post("/", response_model=AdjustmentResponse)
async def create_new_adjustment(adjustment: AdjustmentCreate):
    adjustment_id = await create_adjustment(adjustment.dict())
    created_adjustment = await get_adjustment_by_id(adjustment_id)
    if not created_adjustment:
        raise HTTPException(status_code=500, detail="Adjustment creation failed")
    return created_adjustment

@router.get("/{adjustment_id}", response_model=AdjustmentResponse)
async def get_adjustment(adjustment_id: str):
    adjustment = await get_adjustment_by_id(adjustment_id)
    if not adjustment:
        raise HTTPException(status_code=404, detail="Adjustment not found")
    return adjustment
