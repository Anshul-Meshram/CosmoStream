import app.models
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from app.api.router import api_router
from app.core.config import settings
from app.core.logging import logger
from fastapi.responses import JSONResponse
from app.exceptions.health import HealthRecordNotFound


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting CosmoStream Backend...")
    logger.info("Configuration loaded successfully.")

    #    logger.info("Creating database tables...")
    #    Base.metadata.create_all(bind=engine)
    #    logger.info("Database tables ready.")

    yield

    logger.info("Shutting down CosmoStream Backend...")


app = FastAPI(
    lifespan=lifespan,
    title=settings.app_name,
    version=settings.app_version,
    description="Backend API for the CosmoStream platform",
)

# Include API routers
app.include_router(api_router)


@app.exception_handler(HealthRecordNotFound)
async def health_not_found_handler(request: Request, exc: HealthRecordNotFound):
    return JSONResponse(status_code=404, content={"detail": "Health record not found"})


@app.get("/", tags=["Root"])
async def root():
    return {
        "message": f"Welcome to {settings.app_name}",
        "version": settings.app_version,
        "docs": "/docs",
    }
