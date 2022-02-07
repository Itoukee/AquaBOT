import discord
from discord.ext import commands
import os
import asyncio
import time


bot = commands.Bot(command_prefix = '%')

#bot.remove_command('help')


for filename in os.listdir('cogs/'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.command(brief = "never use the commands below")
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send('Loaded')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send('Unloaded')

@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    await ctx.send('Reloaded')



   
#async def clock(x):
        #user=bot.get_user(311955925109833728)
        #while True:
            #await user.send("écoute moi bien face de lysopaïne, la prochaine fois tu mdis tg jte prend jte retourne gare du Nord octogone")
            #await asyncio.sleep(x)
"""
@bot.command()
async def enregistrer(ctx,):
    db.ajouter()
    await ctx.send("Réussi !")
"""

@bot.event
async def on_ready():
    print('Aqua is ready')
    await bot.change_presence(activity=discord.Game('Useless Goddess|%help'))
    #await asyncio.create_task(clock(86400))


bot.run(TOKEN)
