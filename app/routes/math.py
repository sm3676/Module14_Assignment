from fastapi import APIRouter

router = APIRouter()

@router.post("/add")
def add(a: float, b: float):
    return {"result": a + b}

@router.post("/subtract")
def subtract(a: float, b: float):
    return {"result": a - b}

@router.post("/multiply")
def multiply(a: float, b: float):
    return {"result": a * b}

@router.post("/divide")
def divide(a: float, b: float):
    if b == 0:
        return {"error": "Division by zero not allowed"}
    return {"result": a / b}