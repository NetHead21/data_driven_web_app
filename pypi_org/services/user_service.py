import pypi_org.data.db_session as db_session
from pypi_org.data.users import User
from typing import Optional
from passlib.handlers.sha2_crypt import sha512_crypt as crypto


def get_user_count() -> int:
    session = db_session.create_session()
    return session.query(User).count()


def find_user_by_email(email: str) -> Optional[User]:
    session = db_session.create_session()
    return session.query(User).filter(User.email == email).first()


def create_user(name: str, email: str, password: str) -> Optional[User]:
    if find_user_by_email(email):
        return None

    user = User()
    user.email = email
    user.name = name
    user.hashed_password = hash_text(password)

    # create database session then add new user
    session = db_session.create_session()
    session.add(user)
    session.commit()
    return user


def hash_text(text: str) -> str:
    hash_text = crypto.encrypt(text, rounds=171204)
    return hash_text


def verify_hash(hash_text: str, plain_text: str) -> bool:
    return crypto.verify(plain_text, hash_text)


def login_user(email: str, password: str) -> Optional[User]:
    session = db_session.create_session()
    
    user = session.query(User).filter(User.email == email).first()
    if not user:
        return None
    
    if not verify_hash(user.hashed_password, password):
        return None

    return user


def find_user_by_id(user_id: int) -> Optional[User]:
    session = db_session.create_session()
    
    user = session.query(User).filter(User.id == user_id).first()
    return user