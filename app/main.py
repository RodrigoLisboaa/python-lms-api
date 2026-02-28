from fastapi import FastAPI

from app.api.routers import auth, users

app = FastAPI(title="LMS API", version="0.1.0")

app.include_router(auth.router)
app.include_router(users.router)


@app.get("/health", tags=["health"])
def health():
    return {"status": "ok"}
