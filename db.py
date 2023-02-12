from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
from config import Config

# The Engine is the starting point for any SQLAlchemy application
# We use session, which maintains the ORM-objects, to communicate with database 
ENGINE: Engine = create_engine(Config.DATABASE_URL, pool_pre_ping=True)
SESSIONMAKER: sessionmaker = sessionmaker(bind=ENGINE)


def get_session():
    session = SESSIONMAKER()
    try:
        return session # yield can jump back to do session close
    finally:
        session.close()