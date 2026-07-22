from pydantic import BaseModel, ConfigDict
from datetime import datetime
from app.models.enums import HealthStatus


class HealthCheckCreate(BaseModel):
    status: HealthStatus


class HealthCheckResponse(BaseModel):
    id: int
    status: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
