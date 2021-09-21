import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.group(invoke_without_command=True)
    async def help(ctx):
        embed=discord.Embed(title="Help",description="Use *help <command> for help on a specific command",color=ctx.author.color)
        embed.add_field(name="Memes/Images",value="wasted, gray, invert, trigger",inline=False)
        embed.add_field(name="Random Info",value="pokemon, space")
        embed.add_field(name="Useful Info",value="serverinfo, userinfo, roleinfo",inline=False)
        embed.add_field(name="Misc",value="vibecheck, rps, toss , solve, search",inline=False)

        await ctx.send(embed=embed)

    @help.command()
    async def wasted(ctx):
        embed=discord.Embed(title="Wasted",description="Puts the wasted overlay from GTA over a profile picture. \n If no user is mentioned it will default to the user of the command's profile picture",color=ctx.author.color)
        embed.add_field(name="Usage",value="*wasted [mention user]")
        embed.add_field(name="Aliases",value="waste")
        await ctx.send(embed=embed)
    async def gray(ctx):
        embed=discord.Embed(title="Gray",description="Converts a profile picture into a grayscale image. \n If no user is mentioned it will default to the user of the command's profile picture",color=ctx.author.color)
        embed.add_field(name="Usage",value="*gray [mention user]")
        embed.add_field(name="Aliases",value="grayscale")
        await ctx.send(embed=embed)
    async def invert(ctx):
        embed=discord.Embed(title="Invert",description="Inverts the colors in a user's profile picture. \n If no user is mentioned it will default to the user of the command's profile picture",color=ctx.author.color)
        embed.add_field(name="Usage",value="*invert [mention user]")
        embed.add_field(name="Aliases",value="opposite")
        await ctx.send(embed=embed)
    async def pokemon(ctx):
        embed=discord.Embed(title="Pokemon",description="Returns information about a specified pokemon. Does not support all pokemon.",color=ctx.author.color)
        embed.add_field(name="Usage",value="*pokemon [pokemon]")
        embed.add_field(name="Aliases",value="pokedex")
<<<<<<< HEAD
<<<<<<< HEAD
        await ctx.send(embed=embed) 
=======
        await ctx.send(embed=embed)
>>>>>>> c754cab... Music Functionality
=======
        await ctx.send(embed=embed) 
>>>>>>> 3a1c375... initial commit

    

def setup(bot):
    bot.add_cog(Help(bot))
