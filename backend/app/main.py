import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .portfolio_data import (
    EXPERIENCE,
    EXPERTISE,
    FEATURED_PROJECTS,
    PROFILE,
    PUBLICATIONS,
    TOOLBOX,
)

BASE_DIR = Path(__file__).resolve().parents[2]
FRONTEND_DIST = BASE_DIR / "frontend" / "dist"
CV_DIR = BASE_DIR / "cvfiles"

app = FastAPI(
    title="Personal Page API",
    description="Portfolio API for Thanasak Wanglomklang personal website.",
    version="1.0.0",
)

cors_origins = [
    origin.strip()
    for origin in os.getenv(
        "CORS_ORIGINS",
        "http://localhost:5173,http://127.0.0.1:5173",
    ).split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if CV_DIR.exists():
    app.mount("/cvfiles", StaticFiles(directory=str(CV_DIR)), name="cvfiles")

if (FRONTEND_DIST / "assets").exists():
    app.mount("/assets", StaticFiles(directory=str(FRONTEND_DIST / "assets")), name="assets")


@app.get("/api/health")
def health():
    return {"status": "ok", "service": "personal-page", "version": app.version}


@app.get("/api/profile")
def profile():
    return PROFILE | {"expertise": EXPERTISE, "toolbox": TOOLBOX, "experience": EXPERIENCE}


@app.get("/api/projects")
def projects():
    return FEATURED_PROJECTS


@app.get("/api/publications")
def publications():
    return PUBLICATIONS


@app.get("/{path:path}", include_in_schema=False)
def spa_fallback(path: str):
    static_file = (FRONTEND_DIST / path).resolve()
    if (
        FRONTEND_DIST.exists()
        and static_file.is_relative_to(FRONTEND_DIST.resolve())
        and static_file.is_file()
    ):
        return FileResponse(str(static_file))

    index_file = FRONTEND_DIST / "index.html"
    if index_file.exists():
        return FileResponse(str(index_file))
    return {
        "message": "Personal Page API is running. Start the frontend with `cd frontend; npm run dev`.",
        "docs": "/docs",
    }
