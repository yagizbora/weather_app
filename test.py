import requests
from requests.exceptions import HTTPError


URLS = [
    "https://api.github.com",
    "https://api.github.com/invalid",
    "https://api.github.com/users",
    "https://httpstat.us/500",
]


def url():
    for url in URLS:
        try:
            response = requests.get(url)
            response.raise_for_status()
            response.content
        # except HTTPError as http_err:
        #     print(f"Something is wrong: {http_err}")
        except Exception as err:
            print(f"Other error: {err}")
        if response.status_code == 200:
            print(f"Success! :{response.status_code}")
        elif response.status_code == 404:
            print(f"Not found! :{response.status_code}")
        elif response.status_code == 500:
            print(f"Server Error: {response.status_code}")
        else:
            print(f"Unexpected status code: {response.status_code}")


if __name__ == "__main__":
    url()
