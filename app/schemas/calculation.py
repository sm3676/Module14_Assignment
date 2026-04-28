from pydantic import BaseModel, ConfigDict

# 👉 request body (POST)
class CalculationCreate(BaseModel):
    operand1: float
    operand2: float
    operation: str


# 👉 response model
class CalculationResponse(BaseModel):
    id: int
    operand1: float
    operand2: float
    operation: str
    result: float

    model_config = ConfigDict(from_attributes=True)