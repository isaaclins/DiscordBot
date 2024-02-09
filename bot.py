import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent if you need it

bot = commands.Bot(command_prefix='~', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong! Latency: {} ms'.format(round(bot.latency * 1000)))

bot.run('your_bot_token_here')
