import requests


url_base = "https://api.streamelements.com/kappa/v2/"
header_base = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}


def get_channels(jwt, headers):
    url = url_base + "users/access"
    headers = headers_base


def get_commands(jwt, headers, channel_id):
    url = url_base + f"bot/commands/{channel_id}"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {jwt}",
        "Content-Type": "application/json"
    }


if __name__ == "__main__":
    jwt = input("JWT: ")
    headers_updates = headers_base
    headers["Authorization"] = f"Bearer {jwt}"
