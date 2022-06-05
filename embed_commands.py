import discord
from discord.ext import commands

class embed(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def embed(self, ctx):
        embed = discord.Embed(title = _title, url = _url, description = _description, color = _color)
        embed.set_author(name = ctx.author.display_name, url = _url2, icon_url = ctx.author.avatar_url)
        embed.set_thumbnail(url = "https://vignette.wikia.nocookie.net/clashroyale/images/4/4f/Laughing_Goblin.png/revision/latest/scale-to-width-down/340?cb=20180717203752")
        await ctx.send(embed = embed)

     

_title = "Test Embed"
_url = "https://github.com/isaiahou"
_description = "Checkout my GitHub profile!"
_color = discord.Color.red()
_name = "Salted"
_url2 = "https://google.com"
_icon_url = "icon url"
_thumbnail = "thumbnail"

def setup(client):
    client.add_cog(embed(client))
