from pydantic import BaseModel, ConfigDict
from datetime import datetime


class HealthCheckCreate(BaseModel):
    status: str


class HealthCheckResponse(BaseModel):
    id: int
    status: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
