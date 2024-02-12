import discord
from discord.ext import commands
from settings import *
import aiohttp
import random


intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent if you need it

bot = commands.Bot(command_prefix='!', intents=intents)


async def GenerateRandomPokemonLink():
    link = "https://pokeapi.co/api/v2/pokemon/?limit=1&offset="+random.randint(1, 1025)
    return link


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong! Latency: {} ms'.format(round(bot.latency * 1000)))

@bot.command(name='wa')
async def smash_or_pass(ctx):
    headers = {"Authorization": waifu_token}
    url = "https://waifu.it/api/v4/waifu"

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            data = await response.json()

    waifu_name = data['name']['userPreferred']
    image_url = data['image']['large']
    favorites = data['favourites']

    age = data['age'] if 'age' in data and data['age'] is not None else 'Unknown'

    embed = discord.Embed(title=f"Smash or Pass: {waifu_name}", color=discord.Color.blurple())
    embed.set_image(url=image_url)
    embed.add_field(name="Name", value=waifu_name, inline=True)
    
    # Only add the Age field if the age is known
    if age != 'Unknown':
        embed.add_field(name="Age", value=f"||{age}||", inline=True)
    
    embed.add_field(name="Favorites", value=favorites, inline=True)
    embed.add_field(name="AniList", value=f"[AniList Page]({data['siteUrl']})", inline=False)

    await ctx.send(embed=embed)


@bot.command(name='hu')
async def gimmieMen(ctx):
    headers = {"Authorization": waifu_token}
    url = "https://waifu.it/api/v4/husbando"

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            data = await response.json()

    husbando_name = data['name']['userPreferred']
    image_url = data['image']['large']
    favorites = data['favourites']
    
    age = data['age'] if 'age' in data and data['age'] is not None else 'Unknown'

    embed = discord.Embed(title=f"Gimmie Men: {husbando_name}", color=discord.Color.blurple())
    embed.set_image(url=image_url)
    embed.add_field(name="Name", value=husbando_name, inline=True)
    
    # Only add the Age field if the age is known
    if age != 'Unknown':
        embed.add_field(name="Age", value=f"||{age}||", inline=True)
    
    embed.add_field(name="Favorites", value=favorites, inline=True)
    embed.add_field(name="AniList", value=f"[AniList Page]({data['siteUrl']})", inline=False)

    await ctx.send(embed=embed)

@bot.command(name='rp')
async def randomPokemon(ctx)

    await ctx.send(embed=embed)
        
    
bot.run(bot_token)
