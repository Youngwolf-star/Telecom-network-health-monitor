from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Telecom Network Monitor API running"}

@app.get("/health")
def health():
    host = "8.8.8.8"
    result = subprocess.run(["ping", "-c", "1", host], capture_output=True)
    status = "UP" if result.returncode == 0 else "DOWN"
    return {
        "host": host,
        "status": status
    }
