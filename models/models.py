from sqlalchemy import MetaData, String, Integer, Table, Column, TIMESTAMP, ForeignKey, Boolean

from datetime import datetime


metadata = MetaData()

role = Table(
    'role',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(20), nullable=False)
)


user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('first_name', String(length=50)),
    Column('last_name', String(length=50)),
    Column('email', String(length=50), nullable=True),
    Column('phone_number', String(length=13),nullable=True),
    Column('username', String(length=50), nullable=False),
    Column('hashed_password', String(length=1024), nullable=False, unique=True),
    Column('is_active', Boolean(), default=False),
    Column('is_superuser', String(length=1024), default=False),
    Column('is_verified', Boolean(), default=False),
    Column('last_login', TIMESTAMP),
)