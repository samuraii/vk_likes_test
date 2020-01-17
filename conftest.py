import pytest
import time
import random

from helpers import is_liked, get_post_likes, delete_post_like, add_post_like

from config import ACCESS_TOKEN, API_VERSION, API_GET_LIKES, API_ADD_LIKES, \
    API_DELETE_LIKES, API_IS_LIKED_LIKES, OPEN_OWNER_ID, POSTS, USER_ID, TYPE_POST


@pytest.fixture(scope="session")
def get_likes_url():
    return API_GET_LIKES


@pytest.fixture(scope="session")
def add_likes_url():
    return API_ADD_LIKES


@pytest.fixture(scope="session")
def delete_likes_url():
    return API_DELETE_LIKES


@pytest.fixture(scope="session")
def is_liked_url():
    return API_IS_LIKED_LIKES


@pytest.fixture
def params(request):
    """Параметры передаваемые при каждом запросе по умолчанию"""
    data = {
        "owner_id": OPEN_OWNER_ID,
        "type": TYPE_POST,
        "access_token": ACCESS_TOKEN,
        "v": API_VERSION,
        "user_id": USER_ID
    }

    def fin():
        """Ограничение кол-ва запросов, иначе отрубает"""
        time.sleep(0.5)

    request.addfinalizer(fin)
    return data


@pytest.fixture
def not_liked_post(params):
    """Создание не лайкнутого поста"""
    post = random.choice(POSTS)
    if is_liked(post, params):
        likes = delete_post_like(post, params)
    else:
        likes = get_post_likes(post, params)
    return {"post_id": post, "likes": likes}


@pytest.fixture
def liked_post(params):
    """Создание лайкнутого поста"""
    post = random.choice(POSTS)
    likes = add_post_like(post, params)
    return {"post_id": post, "likes": likes}
