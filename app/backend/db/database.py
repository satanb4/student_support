from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DbHandler:
    """
    Database handler class
    :param url: Database URL
    :type url: str
    """

    def __init__(self, url: str):
        if not url:
            raise ValueError("Database URL is not set")
        if url.startswith("sqlite"):
            self.engine = create_engine(
                url,
                connect_args={
                    "check_same_thread": False
                },  # check_same_thread is only for SQLite
            )
        else:
            self.engine = create_engine(url, connect_args={"check_same_thread": True})
        self.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )
        self.base = None

    def get_db(self):
        """
        Get a database session
        :return: Database session
        """
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()

    def create_all(self, base):
        """
        Create all tables in the database
        :param base: SQLAlchemy base object
        """
        self.base = base
        self.base.metadata.create_all(bind=self.engine)


if __name__ == "__main__":
    path = Path(__file__).parent / "test.sqlite3"
    SQLALCHEMY_DATABASE_URL = f"sqlite:///{path}"
    # SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
    db = DbHandler(SQLALCHEMY_DATABASE_URL)
