from fastapi import FastAPI

app = FastAPI(title="LMS API", version="0.1.0")

@app.get("/health", tags=["health"])
def health():
    return {"status": "ok"}