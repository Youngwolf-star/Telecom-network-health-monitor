from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Network Health Monitor API running"}

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

