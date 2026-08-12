from sqlalchemy import Column, Integer, String
from .database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    priority = Column(String, default="medium")
    due_date_hint = Column(String, nullable=True)
    project_id = Column(Integer, index=True)