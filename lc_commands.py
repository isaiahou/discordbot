import discord
from lc_selenium import ProblemFinder
from discord.ext import commands

class leetcode(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def find(self, ctx, difficulty):
        acceptable_commands = ["easy", "medium", "hard"]
        if difficulty.lower() not in acceptable_commands:
            await ctx.send("Please enter a valid difficulty: easy, medium, or hard")
            return
        if difficulty.lower() == "easy":
            color = discord.Color.green()
        elif difficulty.lower() == "medium":
            color = discord.Color.orange()
        else:
            color = discord.Color.red()
        finder = ProblemFinder(difficulty=difficulty)
        result = finder.find_problem()
        while result is None:
            await ctx.send("LeetCode fed us a premium problem. We will try again...")
            result = finder.find_problem()
        embed = discord.Embed(title = result[0].removesuffix(' - LeetCode'), url = result[1], description = result[2], color = color)
        embed.set_thumbnail(url = "https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco,dpr_1/83facdeba5b924cb3b1a")
        await ctx.send(embed = embed)
    
    @commands.command()
    async def daily(self, ctx):
        finder = ProblemFinder()
        result = finder.find_daily()
        if result is None:
            await ctx.send("Unfortunately, the daily problem is a Premium problem today.")
            return
        difficulty = result[3]
        if difficulty.lower() == "easy":
            color = discord.Color.green()
        elif difficulty.lower() == "medium":
            color = discord.Color.orange()
        else:
            color = discord.Color.red()
        embed = discord.Embed(title = result[0].removesuffix(' - LeetCode'), url = result[1], description = result[2], color = color)
        embed.set_thumbnail(url = "https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco,dpr_1/83facdeba5b924cb3b1a")
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(leetcode(client))
