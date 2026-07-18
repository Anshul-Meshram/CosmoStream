from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.router import api_router
from app.core.config import settings
from app.core.logging import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting CosmoStream Backend...")
    logger.info("Configuration loaded successfully.")

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


@app.get("/", tags=["Root"])
async def root():
    return {
        "message": f"Welcome to {settings.app_name}",
        "version": settings.app_version,
        "docs": "/docs",
    }
