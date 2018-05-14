import discord
import logging
from discord.ext import commands
from ladder import *

from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='#')

logger = logging.getLogger('discord')
logging.basicConfig(level=logging.INFO)
handler = logging.FileHandler(filename='./discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#region commands

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!!")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The username is: {}".format(user.name))

@bot.command(pass_context=True)
async def ladder(ctx, id, limit):
    data = parse_response(make_request(id, limit = limit))
    for entry in data:
        await bot.say("{} the level {} {} ({})".
              format(entry["character"]["name"],
                     entry["character"]["level"],
                     entry["character"]["class"],
                     "Dead" if entry["dead"] else "Alive"))

#endregion

#region events

@bot.event
async def on_command_error(error, ctx):
    print(error)

@bot.event
async def on_ready():
    print ("Path of Bot is ready to serve")

#endregion






bot.run("NDQ1MDA5NTkxMjUyNjgwNzA1.DdkSDg.nEsOYkg5j5ymaajSo4AT-VO20FE")