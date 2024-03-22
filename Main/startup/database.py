from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.pool import QueuePool

class Database:
    def __init__(self, db_uri: str, db_type: str = 'postgresql', debug: bool = False,
                 base_cls=None, pool_size: int = 5, max_overflow: int = 10, scopefunc=None):
        self.db_uri = db_uri
        self.db_type = db_type
        self.debug = debug
        self.base = base_cls or declarative_base()
        self.engine = None
        self.session = None
        self.pool_size = pool_size
        self.max_overflow = max_overflow
        self.scopefunc = scopefunc

    def connect(self):
        if self.db_uri and self.db_uri.startswith(f"{self.db_type}://"):
            self.engine = create_engine(self.db_uri, client_encoding="utf8", echo=self.debug,
                                        poolclass=QueuePool, pool_size=self.pool_size,
                                        max_overflow=self.max_overflow)
        else:
            raise ValueError(f"Invalid database URI or type. Must start with '{self.db_type}://'.")

        self.base.metadata.bind = self.engine
        self.base.metadata.create_all(self.engine)
        self.session = scoped_session(sessionmaker(bind=self.engine, autoflush=False, scopefunc=self.scopefunc))

    def close(self):
        if self.session:
            self.session.close_all()

    def get_session(self) -> scoped_session:
        return self.session

    def get_base(self):
        return self.base

    def get_engine(self):
        return self.engine