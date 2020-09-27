import discord
from discord.ext import commands


class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #bug report command
    @commands.command()
    async def bug(self, ctx, report=None, image=None):
        if report == None:
            await ctx.send(
                'Please provide a helpful description of the bug. Feel free to attach an image.'
            )
            return
        if ctx.message.attachments:
            file = ctx.message.attachments[0]
            file.filename = f'{file.filename}'
            image = await file.to_file()
        channel = self.bot.get_channel(749806907857961060)
        bug: discord.Message = await channel.send(
            content=f'{report}', file=image)
        await bug.add_reaction('✅')
        await bug.add_reaction('❌')
        await ctx.send(
            'Thank you! Your bug has been submitted for confirmation.')

    #feature request command
    @commands.command(aliases=['idea', 'request'])
    async def feature(self, ctx, idea=None):
        if idea == None:
            await ctx.send(
                'Please provide a good description of your feature idea.')
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
