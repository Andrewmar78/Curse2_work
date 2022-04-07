import pytest
from utils import get_comments_all
def test_get_comments_all():
    response = get_comments_all.test_client().get('/')
    assert response.json.get("poster_name") == "larry", "User name incorrect"
    