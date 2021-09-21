import discord
from discord import File
from discord.ext import commands
import aiohttp
from io import BytesIO
import requests


class ProfilePic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["waste"])
    async def wasted(self,ctx,member:discord.Member=None):
        print("hi")
        if not member:
            member=ctx.author
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url_as(format='png')}") as img:
                if not img.status==200:
                    await ctx.send("Oopsies, Something went wrong")
                    await session.close()
                else:
                    imgResp=BytesIO(await img.read())
                    await ctx.send(file=File(imgResp,"user_wasted.png"))
                    await session.close()
    @commands.command(aliases=["opposite"])
    async def invert(self,ctx,member:discord.Member=None):
        if not member:
            member=ctx.author
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://some-random-api.ml/canvas/invert?avatar={member.avatar_url_as(format='png')}") as img:
                if not img.status==200:
                    await ctx.send("Oopsies, Something went wrong")
                    await session.close()
                else:
                    imgResp=BytesIO(await img.read())
                    await ctx.send(file=File(imgResp,"user_inverted.png"))
                    await session.close()
    @commands.command(aliases=["gray"])
    async def grayscale(self,ctx,member:discord.Member=None):
        if not member:
            member=ctx.author
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://some-random-api.ml/canvas/greyscale?avatar={member.avatar_url_as(format='png')}") as img:
                if not img.status==200:
                    print(img.status)
                    await ctx.send("Oopsies, Something went wrong")
                    await session.close()
                else:
                    imgResp=BytesIO(await img.read())
                    await ctx.send(file=File(imgResp,"user_gray.png"))
                    await session.close()
    @commands.command(aliases=["trigger","trig"])
    async def triggered(self,ctx,member:discord.Member=None):
        if not member:
            member=ctx.author
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format='png')}") as img:
                if not img.status==200:
                    print(img.status)
                    await ctx.send("Oopsies, Something went wrong")
                    await session.close()
                else:
                    imgResp=BytesIO(await img.read())
                    await ctx.send(file=File(imgResp,"triggered.gif"))
                    await session.close()
    







            


    

def setup(bot):
    bot.add_cog(ProfilePic(bot))
