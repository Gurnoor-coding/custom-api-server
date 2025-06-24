from unittest.mock import MagicMock
from crud import create_user, get_user
from schemas import UserCreate
from models import User

def test_create_user():
	user_data = UserCreate(name="Alice", email="alice@example.com")
	db = MagicMock()
	db_user = create_user(db, user_data)
	assert db.add.called
	assert db.commit.called
	assert db_user.name == "Alice"

def test_get_user():
	db = MagicMock()
	db.query().filter().first.return_value = User(id=1, name="Bob", email="bob@example.com")
	result = get_user(db, user_id=1)
	assert result.name == "Bob"
