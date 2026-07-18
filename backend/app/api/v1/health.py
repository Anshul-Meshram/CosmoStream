from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "cosmostream-backend",
        "version": "0.1.0-alpha.1",
    }
