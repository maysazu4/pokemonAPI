from fastapi import FastAPI, Request
from pokemon_api.routers import get_router
from pokemon_api.routers import delete_router

server = FastAPI()

server.include_router(get_router.router)
server.include_router(delete_router.router)

