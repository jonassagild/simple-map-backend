from fastapi import FastAPI
from routers import max_wave_height

app = FastAPI()

app.include_router(max_wave_height.router)
