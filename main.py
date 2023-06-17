from fastapi import FastAPI
from routers import max_wave_heigh

app = FastAPI()

app.include_router(max_wave_heigh.router)