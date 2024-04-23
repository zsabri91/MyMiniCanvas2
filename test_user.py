import pytest
from unittest.mock import Mock
from user import UserManager, User

# Define a fixture for the UserManager
@pytest.fixture
def user_manager():
    return UserManager()

# Test the following:
# USER_MANAGER - def generate_id(self):
def test_generate_id(user_manager):
    assert user_manager.generate_id() == 1
    assert user_manager.generate_id() == 2

# USER_MANAGER - def create_a_user(self, name, password, type):
def test_create_a_user(user_manager):
    user_manager.create_a_user("Moh Khaldoun", "password123", "student")
    assert len(user_manager.user_list) == 1
    assert user_manager.user_list[0].name == "Moh Khaldoun"
    assert user_manager.user_list[0].password == "password123"
    assert user_manager.user_list[0].type == "student"

# USER_MANAGER - def find_users(self, ids):
def test_find_users(user_manager):
    user_manager.create_a_user("Moh Khaldoun", "password123", "student")
    user_manager.create_a_user("Moh Khaldoun", "password456", "teacher")
    users_found = user_manager.find_users([1])
    assert len(users_found) == 1
    assert users_found[0].name == "Moh Khaldoun"

# Use mocker to mock the User class
def test_mock_user(mocker, user_manager):
    mock_user = Mock(spec=User)
    mock_user.name = "Mock User"
    mock_user.password = "mock_password123"
    mock_user.type = "mock_student"
    mocker.patch('user.User', return_value=mock_user)
    user_manager.create_a_user("Mock User", "mock_password123", "mock_student")
    assert len(user_manager.user_list) == 1
    assert user_manager.user_list[0].name == "Mock User"
    assert user_manager.user_list[0].password == "mock_password123"
    assert user_manager.user_list[0].type == "mock_student"