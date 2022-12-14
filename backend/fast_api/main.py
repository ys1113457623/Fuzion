from enum import Enum
import time
from typing import Dict, List
from fastapi import FastAPI
from pydantic import BaseModel


from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = ["*"]
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

