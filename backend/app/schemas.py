from pydantic import BaseModel
from typing import Optional, Any
from datetime import datetime

class ShowBase(BaseModel):
    title: str
    description: Optional[str] = None
    duration_minutes: Optional[int] = None
    style: Optional[str] = None

class ShowCreate(ShowBase):
    technical_requirements: Optional[Any] = None
    budget: Optional[Any] = None
    artist_id: Optional[str] = None

class ShowOut(ShowBase):
    id: str
    technical_requirements: Optional[Any] = None
    budget: Optional[Any] = None
    artist_id: Optional[str] = None

    class Config:
        orm_mode = True

class PerformanceCreate(BaseModel):
    show_id: str
    venue_id: Optional[str]
    start_at: datetime
    end_at: Optional[datetime]

class PerformanceOut(PerformanceCreate):
    id: str
    status: Optional[str]

    class Config:
        orm_mode = True