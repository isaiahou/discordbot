import discord
from discord.ext import commands
import music_commands
import embed_commands
import asyncio

import platform
if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

client = commands.Bot(command_prefix = "?", intents = discord.Intents.all())

music_commands.setup(client)
embed_commands.setup(client)

@client.event
async def on_ready():
    print(f'Bot logged in as {client.user}')

client.run("OTgyNzE4MjExNzA1NDE3NzYz.Ga0Rf9.6xhPWsHHvk_nP5acfu1MiE--vun24XKCReSRGo")
