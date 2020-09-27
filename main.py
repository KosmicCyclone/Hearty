import discord
from discord.ext import commands, tasks
import os
from keep_alive import keep_alive
from itertools import cycle
import logging
import json
import random

#Log important events
logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)
handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='a')
handler.setFormatter(
    logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = commands.Bot(command_prefix="h!")

with open('statuses.json', "r+") as s:
    statuses = json.load(s)
    random.shuffle(statuses)
    s.seek(0)
    s.write(json.dumps(statuses))

with open('statuses.json', 'r') as s:
    status = cycle(json.load(s))


#On Ready
@bot.event
async def on_ready():
    change_status.start()
    print(bot.user, "has booted up successfully.")


#Change Status Loop
@tasks.loop(minutes=5)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))


for filename in os.listdir('./modules'):
    if filename.endswith('.py'):
        bot.load_extension(f'modules.{filename[:-3]}')
        print(f'Loaded module: {filename[:-3]}')

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
bot.run(token)
