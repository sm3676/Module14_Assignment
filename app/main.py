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