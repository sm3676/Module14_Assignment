

from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Calculation(Base):
    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True, index=True)
    expression = Column(String)
    result = Column(String)