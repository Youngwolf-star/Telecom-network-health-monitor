from fastapi import FastAPI
from routes import auth, monitor
import subprocess

app = FastAPI()
app.include_router(auth.router)
app.include_router(monitor.router)

@app.get("/")
def root():
    return {"message": "Telecom Network Health Monitor API running"}

@app.get("/health")
def health():
    host = "8.8.8.8"

    try:
        subprocess.check_output(["ping", "-n", "1", host])
        status = "UP"
    except:
        status = "DOWN"

    return {
        "host": host,
        "status": status
    }

