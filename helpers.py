import requests
from requests.exceptions import RequestException

from config import API_GET_LIKES, API_IS_LIKED_LIKES, API_ADD_LIKES, API_DELETE_LIKES, VK_USER_ID


def get_post_likes(post_id, params):
    """Метод получения лайков для поста"""
    params["item_id"] = post_id
    json_response = requests.get(url=API_GET_LIKES, params=params).json()
    try:
        items = json_response['response']['count']
        return items
    except KeyError:
        raise Exception(f"Не найден параметр лайфков у переданного {post_id} с параметрами {params}")


def is_liked(post_id, params):
    """Метод проверки лайкнул ли пользователь пост"""
    params["item_id"] = post_id
    params["user_id"] = VK_USER_ID  # Используем пользователя от имени которого работает приложение
    json_response = requests.get(url=API_IS_LIKED_LIKES, params=params).json()
    try:
        liked = json_response["response"]["liked"]
        return liked
    except KeyError:
        raise Exception(f"Не найден параметр лайфков у переданного {post_id} с параметрами {params}")


def delete_post_like(post_id, params):
    """Удалить лайк посту"""
    params["item_id"] = post_id
    try:
        response = requests.get(url=API_DELETE_LIKES, params=params).json()
        return response["response"]["likes"]
    except RequestException:
        raise RequestException("Возникла ошибка при удалени лайка у поста")


def add_post_like(post_id, params):
    """Добавить лайк посту"""
    params["item_id"] = post_id
    try:
        response = requests.get(url=API_ADD_LIKES, params=params).json()
        return response["response"]["likes"]
    except RequestException:
        raise RequestException("Возникла ошибка при добавлении лайка посту")
