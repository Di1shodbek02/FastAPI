from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get('/hello/{name}')
def hello(name):
    return {'message': f'Hello {name}!'}


fake_user = [
    {'id': 1, 'role': 'admin', 'name': 'Bob'},
    {'id': 2, 'role': 'investor', 'name': 'Bill'},
    {'id': 1, 'role': 'trader', 'name': 'Juli'},
]


@app.get('/users')
def users():
    return fake_user


@app.get('/users/{user_id}')
def user_retrieve(user_id: int):
    return list(filter(lambda x: x['id'] == user_id, fake_user))[0]


class User(BaseModel):
    id: int
    role: str
    name: str



@app.post('/users', response_model=User)
def add_user(user_list: User):
    fake_user.extend(user_list)
    return user_list


@app.delete('/users/{user_id}')
def delete_user(user_id: int):
    user = list(filter(lambda x: x['id'] == user_id, fake_user))
    fake_user.remove(user)
    return {'message': 204}
