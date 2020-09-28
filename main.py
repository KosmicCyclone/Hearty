import discord
from discord.ext import commands, tasks
import os
from keep_alive import keep_alive
from itertools import cycle
import logging
import json
import random
import io
import aiohttp
import time

#Get when the bot came online
startTime = time.time()

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

with open('avatars.json', "r+") as a:
    avatars = json.load(a)
    random.shuffle(avatars)
    a.seek(0)
    a.write(json.dumps(avatars))

with open('avatars.json', 'r') as a:
    avatar = cycle(json.load(a))


#On Ready
@bot.event
async def on_ready():
    change_status.start()
    change_avatar.start()
    store_uptime.start()
    print(bot.user, "has booted up successfully.")
    bot.startTime = startTime


#Change Status Loop
@tasks.loop(minutes=5)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))


#Change Avatar Loop
@tasks.loop(minutes=60)
async def change_avatar():
    async with aiohttp.ClientSession() as session:
        async with session.get(next(avatar)) as resp:
            buffer = io.BytesIO(await resp.read())
            image = buffer.read()
            await bot.user.edit(avatar=image)


#Store Uptime Loop
@tasks.loop(seconds=5)
async def store_uptime():
    with open('uptime.json', 'r+') as u:
        UptimeDict = json.load(u)
        UptimeDict['TotalUptime'] = UptimeDict['TotalUptime'] + 5
        u.seek(0)
        u.write(json.dumps(UptimeDict))


for filename in os.listdir('./modules'):
    if filename.endswith('.py'):
        bot.load_extension(f'modules.{filename[:-3]}')
        print(f'Loaded module: {filename[:-3]}')

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
bot.run(token)
