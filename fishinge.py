import requests
import os

from pprint import pprint
from sys import argv


url_base = "https://api.streamelements.com/kappa/v2/"
headers_base = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}


def get_channel_id(jwt, headers, channel_name):
    url = url_base + "users/access"
    r = requests.get(url=url, headers=headers)
    r.raise_for_status()
    for result in r.json():
        if result["username"] == channel_name:
            return result["channelId"]


def get_command(jwt, headers, channel_id, command_name):
    url = url_base + f"bot/commands/{channel_id}"
    r = requests.get(url=url, headers=headers)
    r.raise_for_status()
    for result in r.json():
        if result["command"] == command_name:
            return result


def update_command(jwt, headers, channel_id, command_name):
    command = get_command(jwt, headers, channel_id, command_name)
    url = url_base + f"bot/commands/{channel_id}/{command['_id']}"

    if set(argv) & set(["--enable", "--disable"]):
        command["enabledOnline"] = False if "--disable" in argv else True
    else:
        if command["enabledOnline"]:
            command["enabledOnline"] = False
        else:
            command["enabledOnline"] = True
    r = requests.put(url=url, json=command, headers=headers)
    r.raise_for_status()

    return r.json()


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
    response = update_command(jwt, headers, channel_id, command_name)
    pprint(response)
