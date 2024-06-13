from fastapi import FastAPI

from api.routers.the_guardian_router import the_guardian_router

app = FastAPI()

app.include_router(the_guardian_router)
