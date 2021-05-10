from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import scoped_session, sessionmaker

_engine = create_async_engine(
    'postgresql+asyncpg://root:root@db:5432/fastapidb',
    echo=True
)

async_session = sessionmaker(
    _engine, expire_on_commit=False, class_=AsyncSession
)