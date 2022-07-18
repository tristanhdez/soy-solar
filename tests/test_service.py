import pytest
import os
import sys
sys.path.append(os.path.realpath('.'))
from main import app


@pytest.fixture
def client():
    return app.test_client()


def test_service_bad_http_method(client):
    resp = client.get('/verify')
    assert resp.status_code == 404

