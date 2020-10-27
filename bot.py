#!/usr/bin/env python3.7
# Work with Python 3.7

import logging
import json
import discord

logging.basicConfig(format="%(asctime)s | %(levelname)s:%(name)s:%(message)s",
                    filename='crest.log', level=logging.INFO)
logging.info('----- Started -----')

with open("auth.json") as data_file:
    auth = json.load(data_file)
with open("params.json") as data_file:
    data = json.load(data_file)

TOKEN = auth["token"]

intents = discord.Intents(messages=True, guilds=True)
intents.members = True
intents.presences = False
intents.typing = False

client = discord.Client(intents=intents)


@client.event
async def on_member_update(before, after):
    # Bot ignore all members that have MEMBER_ID in ignored_ids list
    if after.id in data["ignored_ids"]:
        return
    for ban_word in data["banned_names"]:
        if after.guild.get_member(after.id) is not None and ban_word == after.name:
            await after.ban()
            logging.warning(f'Banned {after.name} with id: {after.id}')
            return


@client.event
async def on_ready():
    print(f"Logged in as: {client.user.name} {{{client.user.id}}}")

client.run(TOKEN)
logging.info('----- Finished -----')
