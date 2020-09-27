import discord
from discord.ext import commands


class Information(commands.Cog):
    def __init__(self, client):
        self.client = client

    #ping command
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! ({round(self.client.latency * 1000)}ms)')
      
    #uptime command

    #help command


def setup(client):
    client.add_cog(Information(client))
