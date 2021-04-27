from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

_engine = create_engine(
    'postgresql://root:root@db:5432/fastapidb',
    echo=True
)

session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=_engine)
)