import requests
from pprint import pprint


url_base = "https://api.streamelements.com/kappa/v2/"
headers_base = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}


def get_channels(jwt, headers):
    url = url_base + "users/access"
    r = requests.get(url=url, headers=headers).json()
    pprint(r)


def get_commands(jwt, headers, channel_id):
    url = url_base + f"bot/commands/{channel_id}"


if __name__ == "__main__":
    jwt = input("JWT: ").strip("\"")
    headers_updated = headers_base
    headers_updated["Authorization"] = f"Bearer {jwt}"
    get_channels(jwt, headers_updated)
