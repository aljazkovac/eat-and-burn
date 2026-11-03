from fastapi import FastAPI

from app.config import settings

app = FastAPI(title="Eat and Burn")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
