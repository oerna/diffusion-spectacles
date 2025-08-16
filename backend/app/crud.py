from sqlalchemy.orm import Session
from . import models, schemas

def get_shows(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Show).offset(skip).limit(limit).all()

def create_show(db: Session, show: schemas.ShowCreate):
    db_show = models.Show(
        title=show.title,
        description=show.description,
        duration_minutes=show.duration_minutes,
        style=show.style,
        technical_requirements=show.technical_requirements,
        budget=show.budget,
        artist_id=show.artist_id
    )
    db.add(db_show)
    db.commit()
    db.refresh(db_show)
    return db_show

def get_performances(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Performance).offset(skip).limit(limit).all()

def create_performance(db: Session, perf: schemas.PerformanceCreate):
    db_perf = models.Performance(
        show_id=perf.show_id,
        venue_id=perf.venue_id,
        start_at=perf.start_at,
        end_at=perf.end_at
    )
    db.add(db_perf)
    db.commit()
    db.refresh(db_perf)
    return db_perf