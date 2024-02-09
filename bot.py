import discord
from discord.ext import commands
from settings import bot_token
import aiohttp

intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent if you need it

bot = commands.Bot(command_prefix='iluv', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong! Latency: {} ms'.format(round(bot.latency * 1000)))



@bot.command(name='kids')
async def smash_or_pass(ctx):
    # Replace 'YOUR_ACCESS_TOKEN' with the actual access token from the waifu API
    headers = {"Authorization": "MTA2NzgxODY5NDEzMjEyNTcxNg--.MTcwNzQ3NTk5Nw--.5ceaf754e3a3"}
    url = "https://waifu.it/api/v4/waifu"
    
    # Make a request to the waifu API
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            data = await response.json()

    # Extract information from the API response
    waifu_name = data['name']['userPreferred']
    image_url = data['image']['large']
    favorites = data['favourites']
    age = data['age'] if 'age' in data and data['age'] is not None else 'Unknown'

    # Create an embed with waifu information
    embed = discord.Embed(title=f"Smash or Pass: {waifu_name}", color=discord.Color.blurple())
    embed.set_image(url=image_url)
    embed.add_field(name="Name", value=waifu_name, inline=True)
    embed.add_field(name="Age", value=age, inline=True)
    embed.add_field(name="Favorites", value=favorites, inline=True)
    embed.add_field(name="AniList", value=f"[AniList Page]({data['siteUrl']})", inline=False)

    # Send the embed to the Discord channel
    await ctx.send(embed=embed)



@bot.command(name='hugs')


    await ctx.send(embed=embed)
    
bot.run(bot_token)
