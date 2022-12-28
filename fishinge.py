import requests
import os
from pprint import pprint


url_base = "https://api.streamelements.com/kappa/v2/"
headers_base = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}


def get_channel_id(jwt, headers, channel_name):
    url = url_base + "users/access"
    r = requests.get(url=url, headers=headers).json()
    for result in r:
        if result["username"] == channel_name:
            return result["channelId"]


def get_command(jwt, headers, channel_id, command_name):
    url = url_base + f"bot/commands/{channel_id}"
    r = requests.get(url=url, headers=headers).json()
    for result in r:
        if result["command"] == command_name:
            return result


def update_command(jwt, headers, channel_id, command):
    url = url_base + f"bot/commands/{channel_id}/{command['_id']}"
    command["enabledOnline"] = True
    r = requests.put(url=url, json=command, headers=headers).json()
    return r


if __name__ == "__main__":
    try:
        jwt = os.environ["SE_KEY"]
    except KeyError:
        jwt = input("JWT: ")
    jwt = jwt.strip("\"")
    headers = headers_base
    headers["Authorization"] = f"Bearer {jwt}"
    channel_name = "chobo"
    command_name = "fishinge"
    channel_id = get_channel_id(jwt, headers, channel_name)
    command = get_command(jwt, headers, channel_id, command_name)
    response = update_command(jwt, headers, channel_id, command)
    pprint(response)
