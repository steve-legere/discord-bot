'''
Created on Feb 27, 2021

@author: Steve
'''

from os import getenv

from discord.ext import commands
from dotenv import load_dotenv
import discord


load_dotenv()
TOKEN = getenv('DISCORD_TOKEN')
GUILD = getenv('DISCORD_GUILD')
TRIGGER = getenv('BOT_TRIGGER')

bot = commands.Bot(TRIGGER)


@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f'{bot.user} is connected to the following server:\n'
        f'{guild.name} (id: {guild.id})'
    )


@bot.event
async def on_error(event, *args, **kwargs):
    with open('error.log', 'a') as logger:
        if event == 'on_message':
            logger.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


@bot.command(name='hello')
async def hello(ctx):
    await ctx.send('Hi!')


if __name__ == '__main__':
    bot.run(TOKEN)
