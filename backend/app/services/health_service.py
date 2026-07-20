from app.schemas.health_check import HealthCheckCreate
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.health_check import HealthCheck


def get_latest_health(db: Session):
    stmt = select(HealthCheck).order_by(HealthCheck.created_at.desc())
    health = db.execute(stmt).scalars().first()
    return health


def create_health_record(db: Session, payload: HealthCheckCreate):
    health = HealthCheck(status=payload.status)

    db.add(health)
    db.commit()
    db.refresh(health)

    return health
