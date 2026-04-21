from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.calculation import Calculation
from app.schemas.calculation import CalculationCreate

router = APIRouter(prefix="/calculations", tags=["Calculations"])


@router.post("/")
def create(calc: CalculationCreate, db: Session = Depends(get_db)):
    new_calc = Calculation(
        expression=calc.expression,
        result=calc.result
    )
    db.add(new_calc)
    db.commit()
    db.refresh(new_calc)
    return new_calc

@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return db.query(Calculation).all()

@router.get("/{id}")
def get_one(id: int, db: Session = Depends(get_db)):
    calc = db.get(Calculation, id)
    if not calc:
        raise HTTPException(status_code=404)
    return calc



@router.put("/{id}")
def update(id: int, updated: CalculationCreate, db: Session = Depends(get_db)):
    calc = db.get(Calculation, id)
    if not calc:
        raise HTTPException(status_code=404)

    for key, value in updated.model_dump().items():
        setattr(calc, key, value)

    db.commit()
    return calc

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    calc = db.get(Calculation, id)
    if not calc:
        raise HTTPException(status_code=404)

    db.delete(calc)
    db.commit()
    return {"message": "Deleted"}