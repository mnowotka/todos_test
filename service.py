from urllib.parse import urljoin
import requests
from constants import BASE_URL


class Service:
    TODOS_URL = urljoin(BASE_URL, 'todos')

    @classmethod
    def get_todos(cls):
        response = requests.get(cls.TODOS_URL)
        if response.ok:
            return response.json()
        else:
            return None

