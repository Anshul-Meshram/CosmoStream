from sqlalchemy import DateTime, Integer, func, Enum
from sqlalchemy.orm import Mapped, mapped_column
from app.models.enums import HealthStatus
from app.db.base import Base


class HealthCheck(Base):
    __tablename__ = "health_checks"

    def __repr__(self) -> str:
        return (
            f"HealthCheck("
            f"id={self.id}, "
            f"status='{self.status}', "
            f"created_a={self.created_at})"
        )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    status: Mapped[str] = mapped_column(Enum(HealthStatus), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
