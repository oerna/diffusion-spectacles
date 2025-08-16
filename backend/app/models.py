from sqlalchemy import Column, String, Integer, ForeignKey, TIMESTAMP, JSON, Text
from sqlalchemy.dialects.postgresql import UUID
import uuid
from .database import Base
from sqlalchemy.sql import func

def gen_uuid():
    return str(uuid.uuid4())

class Show(Base):
    __tablename__ = "shows"
    id = Column(UUID(as_uuid=False), primary_key=True, default=gen_uuid)
    title = Column(String, nullable=False)
    description = Column(Text)
    duration_minutes = Column(Integer)
    style = Column(String)
    technical_requirements = Column(JSON)
    budget = Column(JSON)
    artist_id = Column(UUID(as_uuid=False), ForeignKey("artists.id"))

class Performance(Base):
    __tablename__ = "performances"
    id = Column(UUID(as_uuid=False), primary_key=True, default=gen_uuid)
    show_id = Column(UUID(as_uuid=False), ForeignKey("shows.id"), nullable=False)
    venue_id = Column(UUID(as_uuid=False))
    start_at = Column(TIMESTAMP(timezone=True), nullable=False)
    end_at = Column(TIMESTAMP(timezone=True))
    status = Column(String, default="scheduled")
    metadata = Column(JSON)