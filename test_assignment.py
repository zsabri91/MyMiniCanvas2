import pytest
from unittest.mock import Mock
from assignment import Assignment, Submission

# Define a fixture for the Assignment
@pytest.fixture
def assignment():
    return Assignment(1, "2024-12-01", 101)

# Define a fixture for the Submission
@pytest.fixture
def submission():
    return Submission(1, "This is my assignment.")

# ASSIGNMENT - def __init__(self, assignment_id, due_date, course_id):
def test_assignment_init(assignment):
    assert assignment.assignment_id == 1
    assert assignment.due_date == "2024-12-01"
    assert assignment.course_id == 101
    assert assignment.submission_list == []

# ASSIGNMENT - def submit(self, submission):
def test_assignment_submit(assignment, submission):
    assignment.submit(submission)
    assert len(assignment.submission_list) == 1
    assert assignment.submission_list[0].submission == "This is my assignment."

# SUBMISSION - def __init__(self, student_id, content):
def test_submission_init(submission):
    assert submission.student_id == 1
    assert submission.submission == "This is my assignment."
    assert submission.grade == -1.0
