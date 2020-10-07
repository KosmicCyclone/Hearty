import discord
from discord.ext import commands


class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['sm'],brief='Sets a custom slowmode for a channel')
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, seconds: int = None):
        if seconds == None:
            await ctx.channel.edit(slowmode_delay=0)
            await ctx.send(f'Ok! I disabled slowmode in this channel.')
            return
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send(f'Ok! I set the slowmode in this channel to {seconds} seconds.')
    
    #For Godly Apples
    @commands.command(aliases=['commitdie'],brief='A command built for sadists',description='A command built for sadists')
    async def die(self, ctx):
        await ctx.send('That sounds painful...<:Worry:749016905708208208>')

    #Game link command
    @commands.command(aliases=['gamelink'],brief='A link to Glap.RS',description='A link to Glap.RS')
    async def link(self, ctx):
        embed = discord.Embed(
            description="[Click here to play Glap.RS!](https://www.glap.rs/)",
            color=0xe5d315)
        await ctx.send(embed=embed)

    #Source code command
    @commands.command(aliases=['sc', 'sourcecodes', 'code'],brief='Links to the various source codes',description='Links to the sourcecodesfor Glap.RS and Hearty')
    async def sourcecode(self, ctx):
        embed = discord.Embed(
            title="Here are the links to the various source codes!",
            color=0x0a81ff)
        embed.add_field(
            name="Glap.RS",
            value=
            "[Glap.RS Server](https://github.com/christian7573/glap-rs-server)",
            inline=False)
        embed.add_field(
            name="Glap.RS",
            value=
            "[Glap.RS Client](https://github.com/christian7573/glap-rs-client)",
            inline=False)
        embed.add_field(
            name="Hearty",
            value=
            "[Hearty Source Code](https://github.com/KosmicCyclone/Hearty)",
            inline=False)
        await ctx.send(embed=embed)

    #bug report command
    @commands.command(aliases=['bugreport'],brief='A command to report a bug',description='Report a bug in Glap.RS')
    async def bug(self, ctx, *, report=None):
        guild = ctx.guild
        if not guild.get_role(763501096604794890) in ctx.author.roles:
          await ctx.send(
                'You must be at least level 3 to use this command.',
                delete_after=10)
          return
        if report == None:
            await ctx.send(
                'Please provide a helpful description of the bug. Feel free to attach an image.',
                delete_after=10)
            return
        channel = self.bot.get_channel(749806907857961060)
        if ctx.message.attachments:
            file = ctx.message.attachments[0]
            file.filename = f'{file.filename}'
            image = await file.to_file()
            bug: discord.Message = await channel.send(
                content=f'{report}', file=image)
        else:
            bug: discord.Message = await channel.send(content=f'{report}')
        await bug.add_reaction('✅')
        await bug.add_reaction('❌')
        await ctx.send(
            'Thank you! Your bug has been submitted for confirmation.')

    #feature request command
    @commands.command(aliases=['idea', 'request','featurerequest'],brief='A command to request a feature',description='Request a feature to be added to Glap.RS')
    async def feature(self, ctx, *, idea=None):
        guild = ctx.guild
        if not guild.get_role(763501096604794890) in ctx.author.roles:
          await ctx.send(
                'You must be at least level 3 to use this command.',
                delete_after=10)
          return
        if idea == None:
            await ctx.send(
                'Please provide a good description of your feature idea.',
                delete_after=10)
            return
        channel = self.bot.get_channel(750144643471245312)
        feature: discord.Message = await channel.send(content=f'{idea}')
        await feature.add_reaction('✅')
        await feature.add_reaction('❌')
        await feature.add_reaction('🤷‍♂️')
        await feature.add_reaction('☑️')
        await feature.add_reaction('🚫')
        await ctx.send(
            'Thank you! Your feature has been submitted for others to vote on!'
        )

    #bug report and feature request confirm/deny
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        channel = self.bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        guild = message.guild
        #make sure it isn't in dms
        if not guild:
            return
        if guild.get_role(748656283472625674) in payload.member.roles:
            #bug report version
            if channel.id == 749806907857961060:
                if str(payload.emoji) == '❌':
                    await message.delete()
                    await channel.send(
                        'Alright, I deleted that bug report for you.',
                        delete_after=5)
                elif str(payload.emoji) == '✅':
                    image = None
                    if message.attachments:
                        file = message.attachments[0]
                        file.filename = f'{file.filename}'
                        image = await file.to_file()
                    bugreportchannel = self.bot.get_channel(749807014959644792)
                    await bugreportchannel.send(
                        content=f'{message.content}', file=image)
                    await message.delete()
                    await channel.send(
                        f'Awesome! I moved that bug report to {bugreportchannel.mention}.',
                        delete_after=5)
            #feature request version
            if channel.id == 750144643471245312:
                if str(payload.emoji) == '🚫':
                    await message.delete()
                    await channel.send(
                        'Alright, I deleted that feature request for you.',
                        delete_after=5)
                elif str(payload.emoji) == '☑️':
                    todochannel = self.bot.get_channel(751437559015669770)
                    await todochannel.send(content=f'{message.content}')
                    await message.delete()
                    await channel.send(
                        f'Awesome! I moved that feature request to {todochannel.mention}.',
                        delete_after=5)


def setup(bot):
    bot.add_cog(Utilities(bot))
