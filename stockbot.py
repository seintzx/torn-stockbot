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
    global run
    global MYFUCKINGDATA

    MYFUCKINGDATA = getData()
    print("updating..")

    if run:
        Timer(30, test).start()


def checkPrice(stockName, cond, value):
    global MYFUCKINGDATA, run

    while run:
        stockData = scrapeData(MYFUCKINGDATA)["stocks"]

        for stockID in stockData:
            stock = stockData[stockID]
            if stock["acronym"].lower() == stockName.lower():
                stockValue = float(stock["current_price"])
                break

        print("checking..")
        if cond == "over":
            if stockValue >= value:
                print(stockValue, cond, value, "BINGO")
                return
        elif cond == "under":
            if stockValue <= value:
                print(stockValue, cond, value, "BINGO")
                return
        sleep(30)


def getData():
    url = "https://api.torn.com/torn/?selections=stocks&key={}&comment=stockBot".format(
        os.getenv('TORN_API'))
    response = requests.get(url)
    return (response.json())


def scrapeData(json):
    return json


def stopBot():
    global run
    run = False
    return


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!',
                   allowed_mentions=discord.AllowedMentions(everyone=True))


@bot.command(name='add', help="add notification for selected stock")
async def stat(ctx, stock: str, cond: str, value: float):
    checkPrice(stock, cond, float(value))

    await ctx.send("@everyone - {} is {} {}".format(stock, cond, value))


@bot.command(name='stop', help="stop the whole bot")
async def stat(ctx):
    stopBot()
    await ctx.send("bot is closed, contact seintz to turn it on")


test()
bot.run(TOKEN)
