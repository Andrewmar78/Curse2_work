from flask import Flask, request, render_template, jsonify, send_from_directory
from configure import path_all_comments_datas, path_all_posts_datas
from utils import get_poster_and_posts_all, get_comments_by_post_id, search_for_posts, get_posts_by_user,\
    get_posts_all, get_post_by_pk

import logging
logging.basicConfig(filename="basic.log", level=logging.INFO)

app = Flask(__name__)
# app.register_blueprint(main_blueprint)
# app.register_blueprint(loader_blueprint)


# Вьюшка главной страницы. Не удалось сделать нормальное представление
@app.route("/")
def all_post_main_page():
    all_posters_list = get_poster_and_posts_all()
    list_length = len(all_posters_list)
    return render_template("index.html", all_posters_list=all_posters_list, posters_list=all_posters_list[0],
                           posts_list=all_posters_list[1], avatars_list=all_posters_list[2],
                           pictures_list=all_posters_list[3], list_length=list_length)


# Вьюшка комментариев к посту. Не могу добиться вывода количества комментариев, имени постера
@app.route("/posts/<post_id>")
def post_id_comments_page(post_id):
    commenter_comments_list = get_comments_by_post_id(post_id)
    comments_length = len(commenter_comments_list[0])
    return render_template("post.html", commenter=commenter_comments_list[0], comments=commenter_comments_list[1],
                           username=commenter_comments_list[2], comments_length=comments_length)


# Вьюшка поиска по тексту в постах. Не получается сделать...
@app.route("/search")
def search_page(query):
    query = request.args["s"]
    posts_list = search_for_posts(query)
    return render_template("search.html", s=query, posts_list_length=len(posts_list), posts_list1=posts_list[0])


# Вьюшка постов заданного пользователя. Вроде бы заработала...
@app.route("/users/<username>")
def user_posts_page(username):
    user_posts = get_posts_by_user(username)
    posts_length = len(user_posts)
    return render_template("user-feed.html", username=username.title(), user_posts=user_posts, posts_length=posts_length)


# API для возврата всех постов в JSON. Где-то ошибся, тест не проходит.
@app.route("/api/posts")
def get_all_posts_json():
    data = get_posts_all()
    return jsonify(data)


# API для возврата одного поста по его pk в JSON
@app.route("/api/posts/<pk>")
def get_one_post_json(pk):
    data = get_post_by_pk(pk)
    return jsonify(data)


app.run(debug=True)

