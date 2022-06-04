import discord

bot = discord.Client()

@bot.event
async def on_ready():
    print(f'Bot logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == "$hello":
        await message.channel.send("Hello! I am a bot.")
    if message.content == "what's something that runs fast and plays basketball well":
        await message.channel.send("a stinkin nigger")

bot.run("OTgyNzE4MjExNzA1NDE3NzYz.Ga0Rf9.6xhPWsHHvk_nP5acfu1MiE--vun24XKCReSRGo")