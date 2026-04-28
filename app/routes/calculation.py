from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.calculation import Calculation
from app.schemas.calculation import CalculationCreate, CalculationResponse
from app.routes.user import get_current_user
from app.routes.math import calculate   # ✅ reusable logic

router = APIRouter(tags=["Calculations"])


# ✅ ADD (POST)
@router.post("/calculations", response_model=CalculationResponse)
def create_calculation(
    calc: CalculationCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    try:
        result = calculate(calc.operation, calc.operand1, calc.operand2)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    new_calc = Calculation(
        operand1=calc.operand1,
        operand2=calc.operand2,
        operation=calc.operation,
        result=result,
        user_id=user.id
    )

    db.add(new_calc)
    db.commit()
    db.refresh(new_calc)

    return new_calc


# ✅ BROWSE (GET ALL)
@router.get("/calculations", response_model=list[CalculationResponse])
def get_calculations(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return db.query(Calculation).filter(Calculation.user_id == user.id).all()


# ✅ READ (GET BY ID)
@router.get("/calculations/{id}", response_model=CalculationResponse)
def get_calculation(
    id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    calc = db.query(Calculation).filter(
        Calculation.id == id,
        Calculation.user_id == user.id
    ).first()

    if not calc:
        raise HTTPException(status_code=404, detail="Calculation not found")

    return calc


# ✅ EDIT (PUT)
@router.put("/calculations/{id}", response_model=CalculationResponse)
def update_calculation(
    id: int,
    updated: CalculationCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    calc = db.query(Calculation).filter(
        Calculation.id == id,
        Calculation.user_id == user.id
    ).first()

    if not calc:
        raise HTTPException(status_code=404, detail="Calculation not found")

    try:
        calc.result = calculate(updated.operation, updated.operand1, updated.operand2)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    calc.operation = updated.operation
    calc.operand1 = updated.operand1
    calc.operand2 = updated.operand2

    db.commit()
    db.refresh(calc)

    return calc


# ✅ DELETE
@router.delete("/calculations/{id}")
def delete_calculation(
    id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    calc = db.query(Calculation).filter(
        Calculation.id == id,
        Calculation.user_id == user.id
    ).first()

    if not calc:
        raise HTTPException(status_code=404, detail="Calculation not found")

    db.delete(calc)
    db.commit()

    return {"message": "Deleted successfully"}