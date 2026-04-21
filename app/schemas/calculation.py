
from pydantic import BaseModel

class CalculationCreate(BaseModel):
    expression: str
    result: str