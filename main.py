from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert

from auth.database import get_async_session
from models import blogs
from schemas import BlogSchema, BlogSchemaCreate
app = FastAPI()


@app.post('/blogs')
async def add_blog(new_blog: BlogSchemaCreate, session: AsyncSession = Depends(get_async_session)):
    query = insert(blogs).values(**dict(new_blog))
    await session.execute(query)
    await session.commit()
    return {'success': True}


@app.get('/blogs', response_model=List[BlogSchema])
async def blog_list(session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(blogs)
        result = await session.execute(query)
        return result.all()
    except Exception:
        raise HTTPException(status_code=500)


@app.get('/blogs{blog_id}', response_model=BlogSchema)
async def blog_detail(blog_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(blogs).where(blogs.c.id == blog_id)
    result = await session.execute(query)
    return result.one()


