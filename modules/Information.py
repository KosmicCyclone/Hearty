import discord
from discord.ext import commands
import time, datetime
import json


class Information(commands.Cog):
    def __init__(self, client):
        self.client = client

    #info command
    @commands.command(aliases=['uptime', 'ping'])
    async def info(self, ctx):

        uptime = int(round(time.time() - self.client.startTime))
        uptime = datetime.timedelta(seconds=uptime)

        with open('uptime.json', 'r+') as u:
            UptimeDict = json.load(u)
            UptimePercentage = round(
                (100 * UptimeDict['TotalUptime'] /
                 (time.time() - UptimeDict['FirstOnline'])), 2)

        ping = round(self.client.latency * 1000)

        embed = discord.Embed(color=0x1affe4)
        embed.add_field(name='Uptime', value=f'{uptime}', inline=False)
        embed.add_field(name='Ping', value=f'{ping}ms', inline=False)
        embed.set_footer(text=f'{UptimePercentage}% Uptime')
        await ctx.send(embed=embed)

    #help command


def setup(client):
    client.add_cog(Information(client))
