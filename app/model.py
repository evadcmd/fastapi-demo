from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Entity = declarative_base()

class Camera(Entity):
    __tablename__ = 'camera'
    id = Column(Integer, primary_key=True)