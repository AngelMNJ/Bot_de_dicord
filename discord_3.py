import discord
from discord.ext import commands
import random
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def guess(ctx):
    await ctx.send('Guess a number between 1 and 10.')

    def is_correct(m):
        return m.author == ctx.author and m.content.isdigit()

    answer = random.randint(1, 10)

    try:
        guess = await bot.wait_for('message', check=is_correct, timeout=5.0)
    except asyncio.TimeoutError:
        return await ctx.send(f'Sorry, you took too long it was {answer}.')

    if int(guess.content) == answer:
        await ctx.send('You are right!')
    else:
        await ctx.send(f'Oops. It is actually {answer}.')

bot.run("MTEwMTIwNTk4MDE1NjUzMDcxOQ.GOM5Dn.fJSWodRWaVHnl_GPvKThOv172kRABluY5j4Qss")
