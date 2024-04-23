import pytest
from unittest.mock import Mock
from course import Course, CourseManager
from assignment import Assignment

# Define a fixture for the CourseManager
@pytest.fixture
def course_manager():
    return CourseManager()

# Define a fixture for the Course
@pytest.fixture
def course():
    return Course(1, "COSC341", "Winter 2024", ["Ziad Sabri"])

# COURSE_MANAGER - def generate_id(self):
def test_course_manager_generate_id(course_manager):
    assert course_manager.generate_id() == 1
    assert course_manager.generate_id() == 2

# COURSE_MANAGER - def create_a_course(self, course_code, semester, teacher_list):
def test_course_manager_create_a_course(course_manager, mocker):
    mock_course = Mock()
    mocker.patch.object(course_manager, 'create_a_course', return_value=mock_course)
    course_id = course_manager.create_a_course("COSC341", "Winter 2024", ["Ziad Sabri"])
    assert course_id == mock_course

# COURSE_MANAGER - def find_a_course(self, id):
def test_course_manager_find_a_course(course_manager, mocker):
    mock_course = Mock()
    mocker.patch.object(course_manager, 'find_a_course', return_value=mock_course)
    found_course = course_manager.find_a_course(1)
    assert found_course == mock_course

# COURSE - def import_students(self, student_list):
def test_course_import_students(course):
    course.import_students(["Jane Doe", "Jim Doe"])
    assert len(course.student_list) == 2
    assert "Jane Doe" in course.student_list
    assert "Jim Doe" in course.student_list

# COURSE - def create_an_assignment(self, due_date):
def test_course_create_an_assignment(course, mocker):
    course.create_an_assignment("2024-12-01")
    assert course.assignment_list[-1].due_date == "2024-12-01"

# COURSE - def generate_assignment_id(self):
def test_course_generate_assignment_id(course):
    assert course.generate_assignment_id() == 1
    assert course.generate_assignment_id() == 2

# COURSE - def __str(self):
def test_course_str(course):
    assert str(course)== "ID: 1, code: COSC341, teachers: ['Ziad Sabri']. students: []"