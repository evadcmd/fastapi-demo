from fastapi import FastAPI
import redis
from .ws import info

app = FastAPI()
app.include_router(info.router)

r = redis.StrictRedis(host='redis', port=6379, db=0)
r.set('foo', 'bar')

@app.get('/test')
async def index():
    return {'msg': r.get('foo')}

