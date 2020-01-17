import pytest
import requests
import allure

from helpers import is_liked, get_post_likes

from config import POSTS, PRIVATE_OWNER_ID, API_ADD_LIKES, API_DELETE_LIKES


@allure.story("Методы likes.add likes.delete")
@pytest.mark.parametrize("post_id", POSTS)
@pytest.mark.parametrize("method", [API_ADD_LIKES, API_DELETE_LIKES], ids=["likes.add", "likes.delete"])
@allure.title("Проверка корректности ответа метода на валидные параметры")
def test_add_delete_likes_positive(params, post_id, method):
    params["item_id"] = post_id
    response = requests.get(method, params=params).json()
    assert response["response"]["likes"], "В ответе отсуствует поле с лайками"
    assert int(response["response"]["likes"]), "Формат должен приводиться к числу"


@allure.story("Методы likes.add likes.delete")
@pytest.mark.parametrize("post_id", POSTS)
@pytest.mark.parametrize("method", [API_ADD_LIKES, API_DELETE_LIKES], ids=["likes.add", "likes.delete"])
@allure.title("Проверка ответа на запрос с приватным owner_id")
def test_add_delete_likes_private_profile(params, post_id, method):
    params["owner_id"] = PRIVATE_OWNER_ID
    params["item_id"] = post_id
    response = requests.get(method, params=params).json()
    assert response['error']
    assert response['error']['error_code'] == 30
    assert response['error']['error_msg'] == 'This profile is private'


@allure.story("Методы likes.add likes.delete")
@pytest.mark.parametrize("item_id, msg, status",
                         [(-1, 'One of the parameters specified was missing or invalid: item_id should be positive',
                           100),
                          ("Ten", 'One of the parameters specified was missing or invalid: item_id not integer', 100)],
                         ids=["Negative value", "String value"])
@pytest.mark.parametrize("method", [API_ADD_LIKES, API_DELETE_LIKES], ids=["likes.add", "likes.delete"])
@allure.title("Проверка ответа на запрос с неверным item_id")
def test_add_delete_likes_private_negative(params, item_id, msg, status, method):
    params["item_id"] = item_id
    response = requests.get(method, params=params).json()

    assert response.get('response') is None, "В ответе должен отсутствовать response ключ"

    error = response['error']
    assert error['error_code'] == status, "Неверный код ошибки"
    assert error['error_msg'] == msg, "Неверное сообщение об ошибке"


@allure.story("Методы likes.add likes.delete")
@allure.title("Проверка добавления лайка пользователю")
def test_add_like(params, add_likes_url, not_liked_post):
    """Проверка на удаление или добавление лайка посту в зависимости от исходного"""
    post = not_liked_post["post_id"]
    params["item_id"] = post
    requests.get(API_ADD_LIKES, params=params).json()
    likes = get_post_likes(post, params)
    assert is_liked(post, params), "Пост не добавилсся в лайки пользователю"
    assert likes - 1 == not_liked_post["likes"], "У поста должно быть на 1 больше лайков"


@allure.story("Методы likes.add likes.delete")
@allure.title("Проверка удаления лайка пользователю")
def test_delete_like(params, add_likes_url, liked_post):
    """Проверка на удаление или добавление лайка посту в зависимости от исходного"""
    post = liked_post["post_id"]
    params["item_id"] = post
    likes = requests.get(API_DELETE_LIKES, params=params).json()
    assert not is_liked(post, params), "Пост не добавилсся в лайки пользователю"
    assert likes['response']['likes'] + 1 == liked_post["likes"], "У поста должно быть на 1 меньше лайков"
