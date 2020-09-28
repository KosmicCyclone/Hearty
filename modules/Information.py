import discord
from discord.ext import commands
import time, datetime
import json


class Information(commands.Cog):
    def __init__(self, client):
        self.client = client

    #server info command
    @commands.command()
    async def serverinfo(self, ctx):
        embed=discord.Embed(title=ctx.guild.name, description='The official Discord server for Glap.RS', color=0x3e03bf)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name='Member Count', value=ctx.guild.member_count, inline=False)
        embed.add_field(name='Created', value=ctx.guild.created_at.strftime("%m/%d/%Y") , inline=False)
        await ctx.send(embed=embed)

    #bot info command
    @commands.command(aliases=['ping'])
    async def uptime(self, ctx):

        uptime = int(round(time.time() - self.client.startTime))
        uptime = datetime.timedelta(seconds=uptime)
        with open('uptime.json', 'r+') as u:
            UptimeDict = json.load(u)
            UptimePercentage = round(
                (100 * UptimeDict['TotalUptime'] /
                 (time.time() - UptimeDict['FirstOnline'])), 2)

        ping = round(self.client.latency * 1000)

        embed = discord.Embed(color=0x1affe4)
        embed.add_field(name='Uptime', value=uptime, inline=False)
        embed.add_field(name='Ping', value=f'{ping}ms', inline=False)
        embed.set_footer(text=f'{UptimePercentage}% Uptime')
        await ctx.send(embed=embed)

    #help command


def setup(client):
    client.add_cog(Information(client))
