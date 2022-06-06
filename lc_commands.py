# import discord
# import lc_selenium
# from lc_selenium import ProblemFinder
# from discord.ext import commands

# class leetcode(commands.Cog):
#     def __init__(self, client):
#         self.client = client
    
#     @commands.command()
#     async def find(self, ctx, difficulty):
#         acceptable_commands = ["easy", "medium", "hard"]
#         if difficulty.lower() not in acceptable_commands:
#             await ctx.send("Please enter a valid difficulty: easy, medium, or hard")
#             return
#         finder = ProblemFinder(difficulty=difficulty)
#         result = finder.find_problem()
#         while result is None:
#             await ctx.send("LeetCode fed us a premium problem. We will try again...")
#             result = finder.find_problem()
#         embed = discord.Embed(title = result[0], url = result[1], description = result[2], color = discord.Color.green())
#         embed.set_thumbnail(url = "https://leetcode.com/static/images/LeetCode_Sharing.png")
#         await ctx.send(embed = embed)

# def setup(client):
#     client.add_cog(leetcode(client))