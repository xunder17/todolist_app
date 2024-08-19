from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
import pytest

# Создание тестовой базы данных
TEST_DATABASE_URL = "sqlite:///./test.db"

engine_test = create_engine(TEST_DATABASE_URL, 
                            connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, 
                                   autoflush=False, 
                                   bind=engine_test)


@pytest.fixture(scope="function", autouse=True)
def override_get_db():
    Base.metadata.create_all(bind=engine_test)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine_test)
