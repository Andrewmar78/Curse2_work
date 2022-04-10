from flask import Flask, jsonify
from app import app
import pytest

app = Flask(__name__)


# def test_get_comments_all():
#     response = app.test_client().get('/')
#     assert response.json.get("poster_name") == "larry", "User name incorrect"


# Не работает...
@app.route("/")
def test_all_posts():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.status_code == 500
    assert response.json.get("posters_list") == "leo", "Имя неверно"


# Не работает...
# @app.route("/users/<username>")
def test_user_post():
    response = app.test_client().get("/users")
    assert response.json.get("username") == "larry", "Имя неверно"
    assert response.status_code == 200


# @app.route("/api/posts/<pk>")
def test_one_post():
    params = {"pk": "2"}
    response = app.test_client().get("/api/posts", query_string=params)
    assert response.json.get("pk") == "2", "Номер поста неверный"
    assert response.status_code == 200

# if __name__ == "main":
#     app.run(debug=True)

