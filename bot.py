#!/usr/bin/env python3
from boto.s3.connection import S3Connection
from pathlib import Path  # python3 only
import os
import requests
from datetime import datetime

# import discord API
import discord
from discord.ext import commands

# import Math sruff
import math
from math import *
from datetime import datetime

# Get Enviroment variables
from dotenv import load_dotenv
load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


# Discord Bot Token
token = os.environ['TOKEN']
# imgflip account
acc_username = "jshado"
acc_password = "q&#RqmycL=7Hu@6e"


client = discord.Client()

bot = commands.Bot(command_prefix='!')

memes = requests.get(
    'https://api.imgflip.com/get_memes').json()['data']['memes']

@bot.command(name='meme')
async def meme(ctx, meme_id: str, *args):
    url = 'https://api.imgflip.com/caption_image'
    template_id = 0
    try:
        # Check if ID supplied
        template_id = int(meme_id)
    except ValueError:
        # If ID not supplied try to guess meme from name
        for meme in memes:
            if meme_id.casefold() in meme['name'].casefold():
                template_id = meme['id']
                break

    # put every string passed in arguments in boxes array
    #boxes = []
    # for arg in args:
    #    boxes.append(dict(text=arg))

    # Send request
    params = dict(template_id=template_id,
                  username=acc_username, password=acc_password)
    for i, text in enumerate(args):
        params["text"+str(i)] = text

    res = requests.get(url, params=params)
    data = res.json()

    # Check for valid template_id
    if data['success'] == False:
        await ctx.send('Meme not found, check the ID with !meme_templates')
        return

    print("\n\nTimestamp: " + str(datetime.now().strftime("%Y-%m-%d %H-%M-%S")) +
          "\nMeme: " + str(data['data']['url']))

    await ctx.send(data['data']['url'])

@bot.command(name='meme_templates')
async def meme(ctx):
    await ctx.send('All memes here: https://shadijiha.github.io/shado-discord-meme-bot/index.html . Click on any meme to copy the bot command')

#if a message is a math operation, do the calculation
# @bot.command(name='eval')
# async def meme(ctx, *args :str):
#     stringR = ''
#     for s in args:
#         stringR += s
#     try:
#         result = eval(stringR)
#         await ctx.send('= ' + str(result))
#     except:        
#         await ctx.send(stringR + ' is not a valid math operation.')

# @bot.command(name='time')
# async def meme(ctx):   
#     now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
#     await ctx.send("Today's date: " + str(now))

bot.run(token)
