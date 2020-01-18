import pytest
import random
import requests
import allure

from config import POSTS


@allure.story("Метод likes.getLikes")
@pytest.mark.parametrize("count", [1, 100, 1000])
@allure.title("Проверка параметра count. Positive.")
def test_count_param_positive(params, get_likes_url, count):
    params["item_id"] = random.choice(POSTS)
    params["count"] = count
    response = requests.get(get_likes_url, params=params).json()
    items_amount = len(response['response']['items'])
    assert items_amount == count, f"Возвращено неверное количество лайков {items_amount}, a должно быть {count}"


@allure.story("Метод getLikes")
@pytest.mark.parametrize("count, expected", [(0, 100), (1001, 1000), ('', 100)])
@allure.title("Проверка параметра count на 0 и max. Positive.")
def test_count_param_special(params, get_likes_url, count, expected):
    params["item_id"] = random.choice(POSTS)
    params["count"] = count
    response = requests.get(get_likes_url, params=params).json()
    items_amount = len(response['response']['items'])
    assert items_amount == expected, f"Возвращено неверное количество лайков {items_amount}, a должно быть {count}"


@allure.story("Метод getLikes")
@pytest.mark.parametrize("count, msg, status",
                         [(-1, 'One of the parameters specified was missing or invalid: count should be positive', 100),
                          ("Ten", 'One of the parameters specified was missing or invalid: count not integer', 100)],
                         ids=["Negative value", "String value"])
@allure.title("Проверка параметра count. Negative.")
def test_count_param_negative(params, get_likes_url, count, msg, status):
    params["item_id"] = random.choice(POSTS)
    params["count"] = count
    response = requests.get(get_likes_url, params=params).json()
    assert response.get('response') is None, "В ответе должен отсутствовать response ключ"
    error = response['error']
    assert error['error_code'] == status, "Неверный код ошибки"
    assert error['error_msg'] == msg, "Неверное сообщение об ошибке"
