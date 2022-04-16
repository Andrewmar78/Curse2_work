import pytest
from utils import get_comments_all, get_posts_by_user, get_comments_by_post_id, search_for_posts, get_post_by_pk


def test_get_comments_all():
    assert type(get_comments_all()[0]) == dict, "Get comments mistake. Not a list"


def test_get_posts_by_user():
    assert type(get_posts_by_user("lar")) == list, "Get_posts_by_user mistake. Not a list"


def test_get_comments_by_post_id():
    assert type(get_comments_by_post_id(1)) == list, 'Post id is incorrect Not a list'


def test_search_for_posts():
    assert search_for_posts("лампочка")[0]["poster_name"] == "johnny", "Post search mistake"


def test_get_post_by_pk():
    assert get_post_by_pk(2) == "Вышел погулять днем, пока все на работе. На улице странные штуки," \
                                       " похожие на колонны, которые кто-то сгрыз – незаметно и аккуратно, так," \
                                       " что даже мусора не осталось. И еще много странного: например," \
                                       " почему-то все птицы летают, как птицы, и, похоже, им это совершенно не мешает." \
                                       " Или вот еще: в траве – как будто следы от чьих-то ног, хотя вроде бы я ходил" \
                                       " довольно тихо... На следующий день было совсем пусто. Я вышел и почувствовал" \
                                       " себя очень одиноко. Пошел к остановке. Вокруг было много народу – и все" \
                                       " одинаковые. Как будто все они приехали сюда из одного дома и вышли на этом" \
                                       " перекрестке после работы, чтобы не возвращаться в свои квартиры.", "pk mistake"
