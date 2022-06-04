import discord

bot = discord.Client()

@bot.event
async def on_message(message):
    if message.content == "$hello":
        await message.channel.send("Hello! I am a bot.")

bot.run("OTgyNzE4MjExNzA1NDE3NzYz.Ga0Rf9.6xhPWsHHvk_nP5acfu1MiE--vun24XKCReSRGo")