import pytest
import os
import sys
sys.path.append(os.path.realpath('.'))
from main import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_index_route(client):
    resp = client.get('/')

    assert resp.status_code == 200


def test_index_student_route_not_session(client):
    resp = client.get('/student/')

    assert resp.status_code == 302


def test_index_guest_route(client):
    resp = client.get('/guest/')

    assert resp.status_code == 200
