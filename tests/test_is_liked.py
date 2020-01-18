import random
import allure
import pytest
import requests

from config import POSTS


@allure.story("Метод likes.isLiked")
@allure.title("Проверка ответа метода с валидными параметрами")
def test_is_liked_response_positive(params, is_liked_url):
    params["item_id"] = random.choice(POSTS)
    response = requests.get(is_liked_url, params=params).json()
    assert response["response"], "Отсутствует ключ response в ответе likes.isLiked"
    assert "liked" in response["response"], "Отсутствует ключ liked"
    assert "copied" in response["response"], "Отсутствует ключ copied"


@allure.story("Метод likes.isLiked")
@pytest.mark.parametrize("user_id, msg, status",
                         [(-1, 'One of the parameters specified was missing or invalid: user_id should be positive', 100),
                          ("Ten", 'One of the parameters specified was missing or invalid: user_id not integer', 100)],
                         ids=["Negative value", "String value"])
@allure.title("Проверка ответа метода с невалидными параметрами")
def test_is_liked_response_negative(params, is_liked_url, user_id, msg, status):
    params["user_id"] = user_id
    params["item_id"] = random.choice(POSTS)
    response = requests.get(is_liked_url, params=params).json()
    assert response.get("response") is None, "В ответе должен отсутствовать ключ response"
    error = response["error"]
    assert error["error_code"] == status, "Неверный код ошибки"
    assert error["error_msg"] == msg, "Неверное сообщение об ошибке"
