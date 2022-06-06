import discord
from discord.ext import commands
import music_commands
import embed_commands
import lc_commands
import asyncio
import os

# from dotenv import load_dotenv
# load_dotenv()

# BOT_KEY = os.getenv('BOT_TOKEN')
BOT_KEY = os.environ.get('BOT_TOKEN')

# import platform
# if platform.system()=='Windows':
#     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

client = commands.Bot(command_prefix = "?", intents = discord.Intents.all())

music_commands.setup(client)
embed_commands.setup(client)
# lc_commands.setup(client)

@client.event
async def on_ready():
    print(f'Bot logged in as {client.user}')

client.run(BOT_KEY)
