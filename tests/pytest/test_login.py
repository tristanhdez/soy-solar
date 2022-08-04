import os
import sys
import pytest
sys.path.append(os.path.realpath('.'))
from main import app

@pytest.fixture
def client():
    return app.test_client()


def login(client):
    return client.post("/student/login", data=dict(
        studentCode="215628936",
    ), follow_redirects=True)