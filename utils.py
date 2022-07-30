import json
from configure import path_all_comments_datas, path_all_posts_datas


def get_comments_all():
    """Получение списка всех комментариев из файла"""
    with open(path_all_comments_datas, "r", encoding="utf-8") as file:
        all_comments_datas = json.load(file)
    # print("Полный список комментариев", all_comments_datas)
    return all_comments_datas


def get_posts_all():
    """Получение списка всех постов из файла"""
    with open(path_all_posts_datas, "r", encoding="utf-8") as file:
        all_posts_datas = json.load(file)
    # print("Полный список постов", all_posts_datas)
    return all_posts_datas


def get_posts_by_user(poster_name):
    """Возвращение постов пользователя"""
    user_all_posts = []
    for poster in get_posts_all():
        if poster["poster_name"].lower() == poster_name.lower():
            # print(f'Юзер {poster["poster_name"]}\n {poster["poster_avatar"]}\n {poster["pic"]}\n {poster["content"]}\n')
            user_all_posts.append(poster)
    print(user_all_posts)
    if not user_all_posts:
        user_all_posts = [{"not_found": "Такого постера нет"}]
    return user_all_posts


# Не доделано
def get_posts_by_food():
    """Возвращение постов пользователей по тэгам"""
    all_posts_by_tag = []
    for poster in get_posts_all():
        if "#" in poster["content"]:
            print(f'Тэг {poster["poster_name"]}\n {poster["poster_avatar"]}\n {poster["pic"]}\n {poster["content"]}\n')
            all_posts_by_tag.append(poster)
    print(all_posts_by_tag)
    if not all_posts_by_tag:
        all_posts_by_tag = [{"not_found": "Таких постов нет"}]
    return all_posts_by_tag


def get_post_by_post_id(post_id):
    """Возвращение данных заданного поста"""
    poster_and_post = []
    for item in get_posts_all():
        if item["pk"] == post_id:
            poster_and_post.append({"poster_name": item["poster_name"], "content": item["content"],
                                    "poster_avatar": item["poster_avatar"], "pic": item["pic"]})
    # print("Список постеров с постом:", poster_and_post)
    return poster_and_post


def get_comments_by_post_id(post_id):
    """Возвращение комментариев к заданному посту"""
    comments_to_post = []
    for item in get_comments_all():
        if item["post_id"] == post_id:
            comments_to_post.append({"commenter_name": item["commenter_name"], "comments": item["comment"]})
    # print("Список комментаторов и их комментариев:", comments_to_post)
    return comments_to_post


def search_for_posts(query):
    """Возвращение списка постов по ключевому слову"""
    posts_list = []
    for item in get_posts_all():
        if query.lower() in item["content"].lower() and len(posts_list) <= 9:
            posts_list.append(item)
    # print("Посты по слову:", posts_list)
    return posts_list


def get_post_by_pk(pk):
    """Возвращение поста по его идентификатору"""
    for post in get_posts_all():
        if post[str("pk")] == pk:
            print("Пост по pk:", post["content"])
            return post["content"]
    print("Post is not found")
    return {"not_found": "Такого поста нет"}


# Проверки
# get_comments_all()
# get_posts_all()
# get_posts_by_user("JohNny")
# get_post_by_pk(2)
# get_post_by_post_id(1)
# get_comments_by_post_id(1)
# search_for_posts("тАР")
# get_posts_by_food()
