#!/usr/bin/env python3

import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@bot.command(name='pingme', help="calculate stock checkpoints")
async def stat(ctx, stock: str, value: float, sign: str, perc: float):
    price = value + value * (perc / 100) if sign == ">" else value - value * (perc / 100)
    updown = "higher" if sign == ">" else "lower"
    response = "`/new-alert stocks reach stock:{} value:{} higher-or-lower:{}`".format(stock, round(price,2), updown)
    await ctx.send(response)

# OLD PINGME
# @bot.command(name='pingme', help="calculate stock checkpoints")
# async def stat(ctx, stock: str, value: float):
#     response = "`.pingme stock {} <{} <{} >{} >{} >{}`".format(
#         stock, 
#         round(value - value * 0.005, 2),
#         round(value - value * 0.002, 2),
#         round(value + value * 0.003, 2),
#         round(value + value * 0.006, 2),
#         round(value + value * 0.009, 2))
#  await ctx.send(response)

# @bot.command(name='calc', help="calculate stock checkpoints")
# async def stat(ctx, stock: str, value: float, sign: str, perc: float):
#     price = value + value * (perc / 100) if sign == ">" else value - value * (
#         perc / 100)
#     response = "`.pingme stock {} {}{}`".format(stock, sign, round(price, 2))
#     await ctx.send(response)

bot.run(TOKEN)
