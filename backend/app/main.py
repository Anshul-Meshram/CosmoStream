from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"project": "CosmoStream", "version": "0.0.0", "status": "Running"}
