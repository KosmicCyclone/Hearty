import discord
from discord.ext import commands
import json


class Records(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Record list command
    @commands.command(aliases=['recordlist'],brief='A list of Glap.RS records',description='Brings up a list of Glap.RS records')
    async def records(self, ctx):
        with open('records.json', 'r') as r:
            records = json.load(r)
        embed = discord.Embed(
            title='Record List',
            description=
            'Type **h!record [code]** to view information on a Glap.RS record.',
            color=0xff630f)
        for key, value in records.items():
            if isinstance(value, dict):
                embed.add_field(
                    name=key, value=records[key]['Name'], inline=True)
        await ctx.send(embed=embed)

    #Record Information command
    @commands.command(brief='Description of a record',description='A detailed description of a Glap.RS record')
    async def record(self, ctx, record=None):
        if record == None:
            await ctx.send('Please specify a record.', delete_after=10)
            return
        record = str(record)
        with open('records.json', 'r') as r:
            records = json.load(r)
        embed = discord.Embed(color=0xff1a1a)
        embed.add_field(
            name='Name', value=records[record]['Name'], inline=False)
        embed.add_field(
            name='Description',
            value=records[record]['Description'],
            inline=False)
        embed.add_field(
            name='Requirements',
            value=records[record]['Requirements'],
            inline=False)
        embed.add_field(
            name='Record Holder',
            value=records[record]['Record Holder'],
            inline=False)
        embed.add_field(
            name='Date', value=records[record]['Date'], inline=False)
        embed.add_field(
            name='Record', value=records[record]['Record'], inline=False)
        embed.add_field(
            name='Proof', value=records[record]['Proof'], inline=True)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Records(bot))
