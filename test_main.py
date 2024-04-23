import pytest
import json
from unittest.mock import Mock
from fastapi.testclient import TestClient
from main import app, coursemanager, usermanager
from course import Course
from user import User

# Define a fixture for the test client
@pytest.fixture
def client():
    return TestClient(app)

# Define a fixture for a mock course
@pytest.fixture
def mock_course(mocker):
    return mocker.patch('main.Course', autospec=True)

# Define a fixture for a mock user
@pytest.fixture
def mock_user(mocker):
    return mocker.patch('main.User', autospec=True)

# Test the welcome endpoint
def test_welcome(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Welcome to our miniCanvas!"

# Test the create_a_course endpoint
def test_create_a_course(client):
    # Create a Course object
    course = Course(1, "CS314", "Fall 2022", [1, 2, 3])
    # Add the Course to course_list
    coursemanager.course_list.append(course)
    response = client.post("/courses/1?semester=Fall 2024",  json=[1])
    print(response.content)
    assert response.status_code == 200
    assert response.json() == 1



# Test the import_students endpoint
def test_import_students(client, mock_course, mock_user):
    mock_course.course_id = 1
    mock_course.student_list = [1, 2, 3]
    mock_user.user_id = 1
    coursemanager.find_a_course = Mock(return_value=mock_course)
    usermanager.find_users = Mock(return_value=[mock_user])
    response = client.put("/courses/1/students", json=[0])
    print(response.content)
    assert response.status_code == 200
