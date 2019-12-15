import discord  # импортируем библиотеку дс
from discord.ext import commands
from discord.ext.commands import Bot
import os

Bot = commands.Bot(command_prefix='!')

@Bot.event
async def on_ready():
    print('Bot is online and We have logged in as {0.user}' .format(Bot))
@Bot.command(pass_context=True)
async def hello(ctx):
    await ctx.send('Greetings, mortal')

@Bot.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member):
    mute_role = discord.utils.get(ctx.message.guild.roles, name='mute')
    await member.add_roles(mute_role)

token = os.environ.get('BOT_TOKEN')

bot.run(str(token))
