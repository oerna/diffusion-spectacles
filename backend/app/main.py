from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine
import os

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Diffusion Spectacles API", version="0.1.0")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/shows", response_model=list[schemas.ShowOut])
def list_shows(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_shows(db, skip=skip, limit=limit)

@app.post("/shows", response_model=schemas.ShowOut)
def create_show(show: schemas.ShowCreate, db: Session = Depends(get_db)):
    return crud.create_show(db, show)

@app.get("/performances", response_model=list[schemas.PerformanceOut])
def list_performances(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_performances(db, skip=skip, limit=limit)

@app.post("/performances", response_model=schemas.PerformanceOut)
def create_performance(perf: schemas.PerformanceCreate, db: Session = Depends(get_db)):
    return crud.create_performance(db, perf)