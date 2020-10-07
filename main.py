import discord
from discord.ext import commands
import os
from keep_alive import keep_alive
import logging
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


#On Ready
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('Glap.rs'))
    bot.startTime = startTime
    print(bot.user, "has booted up successfully.")


for filename in os.listdir('./modules'):
    if filename.endswith('.py'):
        bot.load_extension(f'modules.{filename[:-3]}')
        print(f'Loaded module: {filename[:-3]}')

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
bot.run(token)
