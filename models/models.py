from sqlalchemy import MetaData, String, Integer, Table, Column, TIMESTAMP, ForeignKey, Boolean, Text

from datetime import datetime

metadata = MetaData()

blogs = Table(
    'blogs',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String, nullable=False),
    Column('description', Text, nullable=False),
    Column('date', TIMESTAMP, default=datetime.utcnow()),
    Column('view_count', Integer, default=0),
)

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('first_name', String),
    Column('last_name', String),
    Column('email', String),
    Column('phone_number', String),
    Column('username', String),
    Column('password', String),

)
