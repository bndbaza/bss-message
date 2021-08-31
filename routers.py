from fastapi import APIRouter
from bss import blog

routers = APIRouter()

routers.include_router(blog.router, prefix="/blog")
