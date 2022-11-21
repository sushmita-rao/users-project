from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import json
from mongoengine import connect

from models import Users

# from models import Users


app = FastAPI()
connect(db="test", host="139.59.28.205", port=12345)


# class User(BaseModel):
#     id: Optional[int] = None
#     name: str
#     number: int
#     password: str
#
#
# with open('users.json', 'r') as f:
#     users = json.load(f)['users']


@app.post("/createUser", status_code=201)
def create_user(user: Users):

    user_id = max([p['id'] for p in user]) + 1
    new_user = {
        "id": user_id,
        "name": user.name,
        "number": user.number,
        "password": user.password
    }

    print(new_user)

    with open('users.json', 'a') as f:
        json.dump(dict(user), f)

    return new_user


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/get-all-users", status_code=200)
def get_users():
    userdata = Users.objects().to_json()
    print(userdata)

    return {"users": userdata}

