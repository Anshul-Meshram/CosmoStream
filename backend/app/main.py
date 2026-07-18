from fastapi import FastAPI

app = FastAPI(
    title="CosmoStream API",
    version="0.1.0-alpha.1",
    description="Backend API for the CosmoStream platform",
)


@app.get("/")
async def root():
    return {"message": "Welcome to CosmoStream API"}


@app.get("/health")
async def health():
    return {"status": "healthy"}
