from flask import Flask, request, jsonify
from app import app
import pytest

app = Flask(__name__)


# Не работает... В тему теста API не въехал. Не понимаю, что и как вообще можно сделать.
@app.route("/")
def test_all_posts():
    response = app.test_client().get('/')
    # response = request.get("https://127.0.0.1/")
    assert response.status_code == 200
    assert response.json.get("posters_list") == "leo", "Имя неверно"

"""
# Не работает... Не понимаю, что и как вообще можно сделать.
@app.route("/users/<name>")
def test_user_post():
    response = app.test_client().get("/users")
    assert response.json.get("name") == "larry", "Имя неверно"
    assert response.status_code == 200


@app.route("/api/posts/<pk>")
def test_one_post():
    params = {"pk": "2"}
    response = app.test_client().get("/api/posts", query_string=params)
    assert response.json.get("pk") == "2", "Номер поста неверный"
    assert response.status_code == 200
"""

if __name__ == "main":
    app.run(debug=True)

