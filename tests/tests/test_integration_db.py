import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base
from crud import create_user, get_user
from schemas import UserCreate

TEST_DB_URL = "sqlite:///./test.db"
engine = create_engine(TEST_DB_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(bind=engine)

@pytest.fixture(scope="module")
def test_db():
	Base.metadata.create_all(bind=engine)
	db = TestingSessionLocal()
	yield db
	db.close()
	Base.metadata.drop_all(bind=engine)

def test_create_and_get_user(test_db):
	user_data = UserCreate(name="Charlie", email="charlie@example.com")
	created_user = create_user(test_db, user_data)
	fetched_user = get_user(test_db, created_user.id)
	assert fetched_user.email == "charlie@example.com"
