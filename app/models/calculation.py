from sqlalchemy import Column, Integer, Float, String, ForeignKey
from app.db.database import Base

class Calculation(Base):
    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True, index=True)

    operand1 = Column(Float)
    operand2 = Column(Float)
    operation = Column(String)
    result = Column(Float)

    user_id = Column(Integer, ForeignKey("users.id"))