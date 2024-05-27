from fastapi import FastAPI, Request
from pokemon_api.routers import get_router

server = FastAPI()

server.include_router(get_router.router)

