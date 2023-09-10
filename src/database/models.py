from sqlalchemy import Column, Integer, String, func
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(55), nullable=False, unique=True)
    phone = Column(String(24), nullable=False, unique=True)
    birth_date = Column(DateTime, nullable=True)
    bio = Column(String(255), nullable=True)
    created_at = Column("created_at", DateTime, default=func.now())
