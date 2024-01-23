import datetime
import os
import jwt
from datetime import timedelta, datetime

from .schemas import  User, UserInDB, UserLogin
from .database import get_async_session

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, APIRouter

from dotenv import load_dotenv
from passlib.context import CryptContext

from models.models import users


load_dotenv()
register_router = APIRouter()

secret_key = os.environ.get('SECRET')
algorithm = 'HS256'
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def generate_token(user_id: int):
    data_access_token = {
        'token_type': 'access',
        'exp': datetime.utcnow() + timedelta(minutes=30),
        'user_id': user_id,
    }
    data_refresh_token = {
        'token_type': 'refresh',
        'exp': datetime.utcnow() + timedelta(days=1),
        'user_id': user_id,
    }
    access_token = jwt.encode(data_access_token, secret_key, algorithm)
    refresh_token = jwt.encode(data_access_token, secret_key, algorithm)

    return {
        'access_token': access_token,
        'refresh_token': refresh_token,
    }


@register_router.post('/register')
async def register(user: User, session: AsyncSession = Depends(get_async_session)):
    if user.password1 == user.password2:
        if not select(users).where(users.c.username == user.username).exists:
            return {'success': False, 'message': 'Username already exists! '}
        if not select(users).where(users.c.email == user.email).exists:
            return {'success': False, 'message': 'Email already exists! '}
        password = pwd_context.hash(user.password1)
        user_in_db = UserInDB(**dict(user), password=password)
        query = insert(users).values(**dict(user_in_db))
        await session.execute(query)
        await session.commit()
        user_info = UserInDB(**dict(user_in_db))
        return dict(user_info)


@register_router.post('/login')
async def login(user: UserLogin, session: AsyncSession = Depends(get_async_session)):
    query = select(users).where(users.c.username == user.username)
