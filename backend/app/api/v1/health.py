from app.services.health_service import get_latest_health, create_health_record
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
