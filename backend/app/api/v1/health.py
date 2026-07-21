from app.services.health_service import (
    get_latest_health,
    create_health_record,
    get_health_by_id,
    get_health_by_status,
    update_health_record,
)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.health_check import HealthCheckCreate, HealthCheckResponse

router = APIRouter(tags=["Health"])


# @router.get("/health")
# async def health_check():
#    return {
#        "status": "healthy",
#        "service": "cosmostream-backend",
#        "version": "0.1.0-alpha.1",
#    }


@router.get("/health", response_model=HealthCheckResponse)
async def health_check(db: Session = Depends(get_db)):
    health = get_latest_health(db)
    if health is not None:
        return health
    raise HTTPException(
        status_code=404,
        detail="Health status not found",
    )


@router.post("/health", response_model=HealthCheckResponse)
async def create_health(payload: HealthCheckCreate, db: Session = Depends(get_db)):
    return create_health_record(db, payload)


@router.get("/health/search", response_model=list[HealthCheckResponse])
async def search_health(status: str, db: Session = Depends(get_db)):
    return get_health_by_status(db, status)


@router.get("/health/{health_id}", response_model=HealthCheckResponse)
async def get_health(health_id: int, db: Session = Depends(get_db)):
    health = get_health_by_id(db, health_id)
    if health is not None:
        return health
    raise HTTPException(
        status_code=404,
        detail="Health record not found",
    )


@router.put("/health/(health_id}", response_model=HealthCheckResponse)
async def update_health(
    health_id: int, payload: HealthCheckCreate, db: Session = Depends(get_db)
):
    health = update_health_record(db, health_id, payload)
    if health is None:
        raise HTTPException(
            status_code=404,
            detail="Health record not found",
        )
    return health
