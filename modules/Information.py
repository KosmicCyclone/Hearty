import discord
from discord.ext import commands
import time, datetime


class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #server info command
    @commands.command(
        brief='Server info',
        description='Information about the Glap.RS Discord server')
    async def serverinfo(self, ctx):
        embed = discord.Embed(
            title=ctx.guild.name,
            description='The official Discord server for Glap.RS',
            color=0x3e03bf)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(
            name='Member Count', value=ctx.guild.member_count, inline=False)
        embed.add_field(
            name='Created',
            value=ctx.guild.created_at.strftime("%m/%d/%Y"),
            inline=False)
        await ctx.send(embed=embed)

    #bot info command
    @commands.command(
        aliases=['ping'],
        brief='Information about Hearty',
        description='Information about me, the centerpiece of Glap.RS')
    async def uptime(self, ctx):
        uptime = int(round(time.time() - self.bot.startTime))
        uptime = datetime.timedelta(seconds=uptime)

        ping = round(self.bot.latency * 1000)

        embed = discord.Embed(color=0x1affe4)
        embed.add_field(name='Uptime', value=uptime, inline=False)
        embed.add_field(name='Ping', value=f'{ping}ms', inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Information(bot))
