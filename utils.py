import json
from configure import path_all_comments_datas, path_all_posts_datas

__all_comments_datas = []
__all_posts_datas = []


# Получение списка всех комментариев из файла
# def get_comments_all(path):
def get_comments_all():
    global __all_comments_datas
    # with open(path, "r", encoding="utf-8") as file:
    with open(path_all_comments_datas, "r", encoding="utf-8") as file:
        __all_comments_datas = json.load(file)
    print("Полный список комментариев", __all_comments_datas)
    return __all_comments_datas


# Получение списка всех постов из файла
def get_posts_all():
    global __all_posts_datas
    with open(path_all_posts_datas, "r", encoding="utf-8") as file:
        __all_posts_datas = json.load(file)
    print("Полный список постов", __all_posts_datas)
    return __all_posts_datas


# Возвращение списка постеров и их постов
def get_poster_and_posts_all():
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


# Возвращение постов пользователя
def get_posts_by_user(poster_name):
    user_all_posts = []
    for poster in __all_posts_datas:
        # print("poster=", poster)
        if poster["poster_name"].lower() == poster_name.lower():
            print(f'Юзер {poster["poster_name"]}\n {poster["content"]}\n')
            user_all_posts.append(poster["content"])
    print("posts", poster["poster_name"], ": ", user_all_posts)
    return user_all_posts

    # print("Poster is not found")
    # return {"not_found": "Такого постера нет"}


# Возвращение комментариев поста
def get_comments_by_post_id(post_id):
    commenter_list = []
    comments_list = []
    username = None
    for item in __all_comments_datas:
        if item[str("post_id")] == post_id:
            commenter_list.append(item.get('commenter_name', None))
            comments_list.append(item.get('comment', None))
            username = item.get("commenter_name")
    print("Постер", username, "\nКомментаторы: ", commenter_list, "\nКомментарии: ", comments_list)
    return [commenter_list, comments_list, username]


# Возвращение списка постов по ключевому слову
def search_for_posts(query):
    posts_list = []
    for post_word in __all_posts_datas:
        if query.lower() in post_word["content"].lower() and len(posts_list) <= 9:
            posts_list.append(post_word["content"])
    print("Посты по слову ", query, ":", posts_list)
    return posts_list
    # print("Posts are not found")
    # return {"not_found": "Таких постов нет"}


# Возвращение поста по его идентификатору
def get_post_by_pk(pk):
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
get_comments_by_post_id(1)
# search_for_posts("тАР")
