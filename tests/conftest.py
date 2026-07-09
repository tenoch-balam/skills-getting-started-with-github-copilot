import copy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture
def client():
    """Create a TestClient with isolated activity state for each test."""
    original_activities = copy.deepcopy(app_module.activities)

    with TestClient(app_module.app) as test_client:
        yield test_client

    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(original_activities))
