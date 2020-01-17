import os

from dotenv import load_dotenv

load_dotenv()

# Базовые константы
API = "https://api.vk.com"
API_LIKES = API + "/method/likes."
API_GET_LIKES = API_LIKES + "getList"
API_ADD_LIKES = API_LIKES + "add"
API_DELETE_LIKES = API_LIKES + "delete"
API_IS_LIKED_LIKES = API_LIKES + "isLiked"
API_VERSION = "5.103"
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
USER_ID = os.getenv("USER_ID")
VK_USER_ID = os.getenv("VK_USER_ID")
OPEN_OWNER_ID = "1"
PRIVATE_OWNER_ID = "2"
TYPE_POST = "post"

# Посты подобраны чтобы содержать большое кол-во лайков для проверок
# В ином случае нужно иметь способ подготовки постов с нужным кол-вом лайков
POSTS = ["45570", "45556", "45547"]
