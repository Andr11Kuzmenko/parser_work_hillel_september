import requests
from fake_useragent import UserAgent
from requests import Response


class RequestEngine:

    def get_response(self, url: str, params: dict | None = None) -> Response:
        user_agent = UserAgent(platforms='pc')
        response = requests.get(url, params=params, headers={'User-Agent': user_agent.random})
        return response
