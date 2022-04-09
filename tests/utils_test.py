import pytest
from utils import get_comments_all, get_posts_by_user, get_comments_by_post_id, search_for_posts, get_post_by_pk

# def test_get_comments_all():
#     response = get_comments_all.test_client().get('/')
#     assert response.json.get("poster_name") == "larry", "User name incorrect"


# Тест нерабочий. Не знаю, как записать, чтобы проверял, возвращается словарь или нет. Или что-нибудь другое.
def test_get_comments_all():
    assert type(get_comments_all()) == dict, "Get comments mistake"


def test_get_posts_by_user():
    assert get_posts_by_user("lar") == {"not_found": "Такого постера нет"}, "No user name is incorrect"


def test_get_comments_by_post_id():
    assert get_comments_by_post_id(1) == ['Очень здорово!', ':)', 'Класс!',
                                          'Интересно. А где это?'], 'Post id is incorrect'
    assert get_comments_by_post_id(100) == [], "Non-existing post id is incorrect"


def test_search_for_posts():
    assert search_for_posts("лампочка") == ['Вот обычная лампочка, которая может стать для тебя новым смыслом жизни.'],\
        "Post search mistake"


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
