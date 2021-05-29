#!/usr/bin/env python3

import os
import discord
import requests
from time import sleep
from threading import Timer
from dotenv import load_dotenv
from discord.ext import commands

run = True
i = 0
MYFUCKINGDATA = 0


def test():
    global run, i
    global MYFUCKINGDATA

    # get data from API
    MYFUCKINGDATA = i
    i += 1

    if run:
        Timer(1, test).start()


def checkPrice(stock, cond, value):
    global MYFUCKINGDATA, run

    # scrape data, return selected stock current price
    while True:
        print(MYFUCKINGDATA)
        if MYFUCKINGDATA >= value:
            # run = False
            return
        sleep(2)


def getData():
    return


def scrapeData():
    return


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!',
                   allowed_mentions=discord.AllowedMentions(everyone=True))


@bot.command(name='add', help="add notification for selected stock")
async def stat(ctx, stock: str, cond: str, value: int):
    checkPrice(stock, cond, int(value))
    allowed_mentions = discord.AllowedMentions(everyone=True)
    await ctx.send("@everyone- {} is {} {}".format(stock, cond, value),
                   allowed_mentions=allowed_mentions)


test()
bot.run(TOKEN)
