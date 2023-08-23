import discord
from discord.ext import commands
import random
import asyncio
import math
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

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

@bot.command()
async def hola(ctx):
    await ctx.send("Good morning, or afternoon or night, I don't know what hour it is.")

@bot.command()
async def mem(ctx):
    imagen = random.choice(os.listdir('images'))
    with open(f'images/{imagen}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()   
async def solve(ctx, a: float, b: float, c: float):
    try:
        raiz = b**2 - 4*a*c
        if raiz >= 0:
            x_1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
            x_2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
            await ctx.send(f"The solutions are: {x_1} and {x_2}")
        else:
            await ctx.send("The equation has no real solutions.")
    except ValueError:
        await ctx.send("Invalid input. Please provide valid numerical values.")

bot.run("MTEwMTIwNTk4MDE1NjUzMDcxOQ.GBLWim.XLnJO93W6orXC_IhRMwFvC-I8b44mrUCByYbpA")
