from fastapi import FastAPI
from app.config import APP_VERSION
from app.info import get_health_payload, get_version_payload

app = FastAPI()


@app.get("/health")
def health_check():
    return get_health_payload()
@app.get("/version")
def get_version():
    return get_version_payload(APP_VERSION)