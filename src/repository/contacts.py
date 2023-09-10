from datetime import datetime
from typing import List

from sqlalchemy.orm import Session

from src.database.models import Contact
from src.schemas import (
    ContactBase,
    ContactUpdate,
)


# async def create_contact(body: ContactBase, db: Session) -> Contact:
async def create_contact(body, db: Session) -> Contact:
    birth_date_str = body.birth_date
    birth_date = datetime.strptime(birth_date_str, "%d-%m-%Y")
    contact = Contact(
        first_name=body.first_name,
        last_name=body.last_name,
        email=body.email,
        phone=body.phone,
        birth_date=birth_date,
    )
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def get_contacts(skip: int, limit: int, db: Session) -> List[Contact]:
    return db.query(Contact).offset(skip).limit(limit).all()


async def get_contact(contact_id: int, db: Session) -> Contact:
    return db.query(Contact).filter(Contact.id == contact_id).first()


async def update_contact(
    contact_id: int, body: ContactUpdate, db: Session
) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.email = body.email
        contact.phone = body.phone
        contact.birth_date = body.birth_date
        contact.bio = body.bio
        db.commit()
    return contact


async def remove_contact(contact_id: int, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact
