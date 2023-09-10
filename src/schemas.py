from datetime import datetime
from pydantic import BaseModel, Field


class ContactBase(BaseModel):
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    email: str = Field(max_length=55)
    phone: str = Field(max_length=24)
    birth_date: datetime
    bio: str = Field(max_length=255)
    created_at: datetime


class ContactResponse(ContactBase):
    # id: int
    created_at: datetime

    class Config:
        from_attributes = True


class ContactUpdate(ContactBase):
    done: bool
