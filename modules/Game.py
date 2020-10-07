import discord
from discord.ext import commands


class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Game info command
    @commands.command(
        aliases=['glap'],
        brief='Information about Glap.RS',
        description='Some basic information about Glap.RS')
    async def glaprs(self, ctx):
        embed = discord.Embed(
            title="Glap.RS",
            description=
            "What is Glap.RS? Glap.RS is a remake of the popular multiplayer game Glap.io (developed by IronJack) that shut down in January of 2019. Written in a combination of Rust and TypeScript, Glap.RS has been built from the ground up by <@!165796996966252544>. Development began on August 2, 2020, and the game is continuously being improved and expanded.",
            color=0x1fff80)
        embed.set_thumbnail(
            url=
            "https://images-ext-1.discordapp.net/external/OT3UlF-bsn-qYSolse5cNYV_Ke7fRtAkpqEiZKV3q2M/%3Fwidth%3D602%26height%3D401/https/media.discordapp.net/attachments/748657558926917734/753701805245857882/unknown.png"
        )
        embed.add_field(
            name="Latest Update",
            value="Beta 0.2: Bugfixes and stability",
            inline=False)
        embed.add_field(
            name="Server Status", value="Unavailable", inline=False)
        embed.add_field(name="Player Count", value="Unavailable", inline=False)
        embed.add_field(
            name="Links",
            value=
            "[Game](https://www.glap.rs/)\n[Wiki](https://glaprs.fandom.com/wiki/Glap.RS_Wiki)\n[Discord Server](https://discord.gg/qdFRb8H)",
            inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Game(bot))
