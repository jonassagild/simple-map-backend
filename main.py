from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from routers import max_wave_height


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(max_wave_height.router)
