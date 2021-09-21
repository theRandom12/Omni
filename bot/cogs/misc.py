import discord
from discord import Embed
from discord.ext import commands
import datetime
from googlesearch import search as gsearch


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["server"])
    async def serverinfo(self, ctx):
        humanCount=len([m for m in ctx.guild.members if not m.bot])
        print(ctx.guild.members)
        print(humanCount)
        botCount=ctx.guild.member_count-humanCount
        owner=ctx.guild.owner
        icon=str(ctx.guild.icon_url)
        name=str(ctx.guild.name)
        text_channels=len(ctx.guild.text_channels)
        voice_channels = len(ctx.guild.voice_channels)
        role_count = len(ctx.guild.roles)
        created = ctx.guild.created_at.strftime("%m-%d-%Y %H:%M%p")
        
        embed1=Embed(timestamp=ctx.message.created_at,color=ctx.author.color,title=name+" Server Info")
        embed1.set_thumbnail(url=icon)
        embed1.add_field(name="Human Count",value=humanCount)
        embed1.add_field(name="Bot Count",value=botCount)
        embed1.add_field(name="Owner",value=owner)
        embed1.add_field(name="Text Channels",value=text_channels)
        embed1.add_field(name="Voice Channels",value=voice_channels)
        embed1.add_field(name="Role Count",value=role_count)
        embed1.add_field(name="Created On",value=created)
        await ctx.send(embed=embed1)
    @commands.command()
    async def search(ctx,results=10,*argv):
        query=" ".join(argv)
        if query==None:
            await ctx.send('You need to enter a query...')
        else:
            embed=discord.Embed(title='Results for '+query+':')
            results=gsearch(query,lang='en',num_results=results)
            for i in results:
                embed.add_field(name='Search Result:',value=i,inline=False)
            await ctx.send(embed=embed)
    @commands.command()
    async def solve(ctx,e):
        try:
            embed=discord.Embed(title="Answer:",description="Your problem returned with the answer {}".format(eval(e)))
            await ctx.send(embed=embed)
        except:
            await ctx.send("Oh no! Something went wrong")
        



        
    


    

def setup(bot):
    bot.add_cog(Misc(bot))
