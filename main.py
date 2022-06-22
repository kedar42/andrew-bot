import discord


class Datapack:
    def __init__(self, token):
        self.token = token


def parse_config(path):
    token = ""
    with open(path) as config:
        for line in config.readlines():
            what, value = line.split('=')
            if what == "token":
                token = value
    return Datapack(token)


class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")

data = parse_config("config")
client = MyClient()
client.run(data.token)
