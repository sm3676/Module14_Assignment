from fastapi import FastAPI
from app.db.database import Base, engine
from app.routes import user, calculation
from app.models import user as user_model, calculation as calc_model

app = FastAPI()

# create tables
Base.metadata.create_all(bind=engine)

# include routes
app.include_router(user.router)
app.include_router(calculation.router)

from fastapi import FastAPI

app = FastAPI()

# ROOT
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI App"}

from app.routes import math

app.include_router(math.router)

from fastapi import FastAPI
from app.routes import user, calculation, math

app = FastAPI()

# include ALL routers
app.include_router(math.router)
app.include_router(user.router)
app.include_router(calculation.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI App"}