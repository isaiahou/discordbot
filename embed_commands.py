import discord
from discord.ext import commands

class embed(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def embed(self, ctx, title, url, description, thumbnail_url):
        embed = discord.Embed(title = title, url = url, description = description, color = _color)
        embed.set_author(name = ctx.author.display_name, icon_url = ctx.author.avatar_url)
        embed.set_thumbnail(url = thumbnail_url)
        await ctx.send(embed = embed)

_color = discord.Color.blurple()

def setup(client):
    client.add_cog(embed(client))
