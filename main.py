from fastapi import FastAPI
from routers import routers
from starlette.responses import Response
from starlette.requests import Request
from core.db import Session


app = FastAPI()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internrt server error", status_code=500)
    try:
        request.state.db = Session()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

app.include_router(routers)
