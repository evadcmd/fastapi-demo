from fastapi import FastAPI
import redis

import random
import string

from .model import Camera
from .db import async_session
from .ws import info

app = FastAPI()
app.include_router(info.router)

r = redis.StrictRedis(host='redis', port=6379, db=0)
r.set('foo', 'bar')

def random_ascii(num: int) -> str:
    return ''.join(random.choice(string.ascii_letters) for i in range(num))

@app.get('/test')
async def index():
    return {'msg': r.get('foo')}

@app.get('/add')
async def add():
    async with async_session() as session:
        async with session.begin():
            session.add_all(
                [
                    Camera(name=random_ascii(10)),
                    Camera(name=random_ascii(10)),
                    Camera(name=random_ascii(10))
                ]
            )


