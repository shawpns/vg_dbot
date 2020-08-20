import discord
from discord.ext import commands
import platform
import random
import time
import asyncio

bot = commands.Bot(command_prefix='+', case_insensitive=True)

@bot.event
async def on_ready():
    activity = discord.Game(name="Discord", type=1)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="VapeGodZ Esports Server"))
    print(f'Logged in as {bot.user.name}(ID: +{bot.user.id}) |'
          f'Connected to {str(len(bot.guilds))} servers |'
          f'Connected to {str(len(set(bot.get_all_members())))} users')
    print('--------')
    print('CREATED AND HOSTED BY ShaW')


@bot.event
async def on_command_error(ctx, error):
    # Ignore these errors:
    ignored = (
        commands.CommandNotFound, commands.UserInputError, commands.BotMissingPermissions, commands.MissingPermissions, discord.errors.Forbidden, commands.CommandInvokeError, commands.MissingRequiredArgument)
    if isinstance(error, ignored):
        return


@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def userinfo(ctx, user: discord.Member):
    try:
        embed = discord.Embed(title="{}'s info".format(user.name),
                              description="Here's what I could find.",
                              color=discord.Colour.dark_red())

        embed.add_field(name="Name", value=user.name, inline=True)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Status", value=user.status, inline=True)
        embed.add_field(name="Highest role", value=user.top_role)
        embed.add_field(name="Joined", value=user.joined_at)
        embed.set_thumbnail(url=user.avatar_url)

        await ctx.send(embed=embed)
    except:
        await ctx.send("Missing Requrired Args")


@commands.has_permissions(administrator=True)
@bot.command(pass_context=True)
async def send(ctx, *, content: str):
    for member in ctx.guild.members:
        c = await member.create_dm()
        try:
            await c.send(content)
            await ctx.send("Message Sent to Targets")
        except:
            await ctx.send("DM can't send to : {} :x: ".format(member))
            
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
     
@bot.command(name='create-channel')
@commands.has_role(':)')
async def create_channel(ctx, channel_name='vg-temp-channel'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)
        
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')


bot.run("NzQxNTk4MTMyNTA0MzYzMDIw.Xy55FQ.1V940d4C7FKa2TEq2BnJ-mxA3I4")
