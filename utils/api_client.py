import requests

from config.settings import BASE_URL, API_KEY, DEFAULT_TIMEOUT


class APIClient:

    def __init__(self, base_url=BASE_URL, api_key=API_KEY):
        self.base_url = base_url
        self.session = requests.Session()

        if api_key:
            self.session.headers.update({
                "Authorization": f"Bearer {api_key}",
                "Accept": "application/json"
            })

    def get(self, endpoint, params=None, headers=None):
        return self.session.get(
            f"{self.base_url}{endpoint}",
            params=params,
            headers=headers,
            timeout=DEFAULT_TIMEOUT
        )