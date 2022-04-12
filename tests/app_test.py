from app import app
import json


def test_all_posts():
    """Тест вьюшки возврата всех постов в JSON"""
    response = app.test_client().get("/api/posts")
    json_data = json.loads(response.data)
    assert response.status_code == 200
    assert 'content' in json_data[0]
    # assert 'something' in json_data[0]
    assert 'тар' in json_data[0]['content']


def test_one_post():
    """Тест вьюшки возврата одного постов в JSON"""
    response = app.test_client().get("/api/posts/2")
    json_data = json.loads(response.data)
    assert response.status_code == 200
    assert 'not_found' in json_data


def test_user_data():
    """Тест проверки возврата списка со странички пользователя в JSON"""
    response = app.test_client().get("/api/users/leo")
    json_data = json.loads(response.data)
    assert response.status_code == 200
    assert type(json_data) == list
