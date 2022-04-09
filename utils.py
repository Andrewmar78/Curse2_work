import json
from configure import path_all_comments_datas, path_all_posts_datas

__all_comments_datas = []
__all_posts_datas = []


def get_comments_all():
    # Получение списка всех комментариев из файла
    global __all_comments_datas
    # with open(path, "r", encoding="utf-8") as file:
    with open(path_all_comments_datas, "r", encoding="utf-8") as file:
        __all_comments_datas = json.load(file)
    print("Полный список комментариев", __all_comments_datas)
    return __all_comments_datas


def get_posts_all():
    # Получение списка всех постов из файла
    global __all_posts_datas
    with open(path_all_posts_datas, "r", encoding="utf-8") as file:
        __all_posts_datas = json.load(file)
    print("Полный список постов", __all_posts_datas)
    return __all_posts_datas

"""
def get_poster_and_posts_all():
    # Возвращение списка постеров и их постов/ Функция не нужна
    posters_list = []
    posts_list = []
    avatars_list = []
    pictures_list = []
    for item in __all_posts_datas:
        posters_list.append(item.get('poster_name', None))
        posts_list.append(item.get('content', None))
        avatars_list.append(item.get('poster_avatar', None))
        pictures_list.append(item.get('pic', None))
    print("Юзеры: ", posters_list, "\nПосты: ", posts_list, "\nАватары: ", avatars_list, "\nРис: ", pictures_list)
    return [posters_list, posts_list, avatars_list, pictures_list]
"""


def get_posts_by_user(poster_name):
    # Возвращение постов пользователя
    user_all_posts = []
    for poster in __all_posts_datas:
        if poster["poster_name"].lower() == poster_name.lower():
            print(f'Юзер {poster["poster_name"]}\n {poster["content"]}\n')
            user_all_posts.append(poster["content"])
    print("posts", poster["poster_name"], ": ", user_all_posts)
    return user_all_posts


def get_comments_by_post_id(post_id):
    # Возвращение комментариев к заданному посту
    poster_and_post = []
    comments_to_post = []

    for item in __all_posts_datas:
        if item["pk"] == post_id:
            poster_and_post = item["poster_name"], item["content"]
    for item in __all_comments_datas:
        if item["post_id"] == post_id:
            comments_to_post.append({"commenter_name": item["commenter_name"], "comments": item["comment"]})
    print("Список комментаторов и их комментариев:", comments_to_post)
    print("Список постеров с постом:", poster_and_post)
    return poster_and_post, comments_to_post


def search_for_posts(query):
    # Возвращение списка постов по ключевому слову
    posts_list = []
    for item in __all_posts_datas:
        if query.lower() in item["content"].lower() and len(posts_list) <= 9:
            posts_list.append({"poster_name": item["poster_name"], "content": item["content"]})
    print("Посты по слову:", posts_list)
    return posts_list


def get_post_by_pk(pk):
    # Возвращение поста по его идентификатору
    for post in __all_posts_datas:
        if post[str("pk")] == pk:
            print("Пост по pk:", post["content"])
            return post["content"]
    print("Post is not found")
    return {"not_found": "Такого поста нет"}


# Проверки
# get_comments_all("data/comments.json")
# get_posts_all("data/data.json")
get_comments_all()
get_posts_all()
# get_poster_and_posts_all()
# get_posts_by_user("JohNny")
# get_post_by_pk(2)
# get_comments_by_post_id(1)
# search_for_posts("тАР")
