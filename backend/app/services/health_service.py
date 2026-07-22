from app.schemas.health_check import HealthCheckCreate
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.exceptions.health import HealthRecordNotFound
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


def get_health_by_id(db: Session, health_id: int):
    stmt = select(HealthCheck).where(HealthCheck.id == health_id)
    health = db.execute(stmt).scalars().first()
    if health is None:
        raise HealthRecordNotFound()
    return health


def get_health_by_status(db: Session, status: str):
    stmt = (
        select(HealthCheck)
        .where(HealthCheck.status == status)
        .order_by(HealthCheck.created_at.desc())
    )
    return db.execute(stmt).scalars().all()


def update_health_record(db: Session, health_id: int, payload: HealthCheckCreate):
    health = get_health_by_id(db, health_id)
    if health is None:
        return None
    health.status = payload.status
    db.commit()
    db.refresh(health)
    return health
