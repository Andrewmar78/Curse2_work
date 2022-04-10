from flask import Flask, request, render_template, jsonify
from utils import get_comments_by_post_id, search_for_posts, get_posts_by_user,\
    get_posts_all, get_post_by_pk

import logging
logging.basicConfig(filename="basic.log", level=logging.INFO)

app = Flask(__name__)


@app.route("/")
def all_post_main_page():
    """Вьюшка главной страницы"""
    all_posters_list = get_posts_all()
    return render_template("index.html", all_posters_list=all_posters_list)


@app.route("/posts/<int:post_id>")
def post_id_comments_page(post_id):
    """Вьюшка комментариев к посту"""
    post_and_comments = get_comments_by_post_id(post_id)
    post_info = post_and_comments[0]
    comments_info = post_and_comments[1]
    return render_template("post.html", post_info=post_info, comments_info=comments_info)


@app.route("/search")
def search_page():
    """Вьюшка поиска по тексту в постах"""
    query = request.args["s"]
    posts = search_for_posts(query)
    return render_template("search.html", posts=posts, posts_length=len(posts))


@app.route("/users/<username>")
def user_posts_page(username):
    """Вьюшка постов заданного пользователя"""
    user_posts = get_posts_by_user(username)
    posts_length = len(user_posts)
    return render_template("user-feed.html", username=username.title(), user_posts=user_posts, posts_length=posts_length)


@app.route("/api/posts")
def get_all_posts_json():
    # API для возврата всех постов в JSON.
    data = get_posts_all()
    return jsonify(data)


@app.route("/api/posts/<pk>")
def get_one_post_json(pk):
    # API для возврата одного поста по его pk в JSON
    data = get_post_by_pk(pk)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
