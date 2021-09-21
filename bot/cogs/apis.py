import discord
from discord.ext import commands
from random import randint as ran
import requests

compText=open('compliments.txt')
insText=open('insults.txt')

def get_dog():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url


def get_cat():
    contents = requests.get('https://aws.random.cat/meow').json()    
    url = contents['url']
    return url
class Apis(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.comps=compText.read().split('\n')
        self.insults= insText.read().split('\n')
    
    @commands.command(aliases=['roast','roastme'])
    async def insult(self,ctx):
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3a1c375... initial commit
        if(ctx.message.author.id==589871370318381117):
            await ctx.send("I can't roast you. you're too amazing and epic")
        else:
            insult=self.insults[ran(0,len(self.insults)-1)]
            await ctx.send(insult)
<<<<<<< HEAD
=======
        insult=self.insults[ran(0,len(self.insults)-1)]
        await ctx.send(insult)
>>>>>>> c754cab... Music Functionality
=======
>>>>>>> 3a1c375... initial commit
    
    @commands.command(aliases=['comp','compli'])
    async def compliment(self,ctx):
        comp=self.comps[ran(0,len(self.comps)-1)]
        await ctx.send(comp)
    
    @commands.command(aliases=["dog","doggy"])
    async def doggo(self,ctx):
        try:
            await ctx.send(get_dog())
        except:
            await ctx.send("Something happened and we couldn't find a dog for you")
    @commands.command(aliases=["cat","kitty"])
    async def catto(self,ctx):
        try:
            await ctx.send(get_cat())
        except:
            await ctx.send("Something happened and we couldn't find a cat for you")
    @commands.command(aliases=["vibe"])
    async def vibecheck(self,ctx):
        if ctx.author.id==589871370318381117:
            await ctx.send("Your vibe level is 1000000. After all, you created me")
        else:
            vibe=ran(1,10)
            vibeDict={1:"You are not vibing",2:"Yu aren't really vibing",3:"You're vibing just a little",4:"You are just barely vibing",
            5:"You are sort of vibing",6:"You are vibing",7:"You are vibing quite a bit",8:"You are vibing a lot",9:"Wow! That's a lot of vibe",10:"The vibe is strong in this one"}
            await ctx.send("Your vibe level is "+str(vibe)+". "+vibeDict.get(vibe,"Something went wrong"))
    
    @commands.command(aliases=["astronauts"])
    async def space(self,ctx):
        
        space=requests.get("http://api.open-notify.org/astros.json").json()
        iss=requests.get("http://api.open-notify.org/iss-now.json").json()
        if space["message"]=="success":
            numSpace=space['number']
            people=space["people"]
            
            

            location=iss["iss_position"].get("latitude")+" "+iss["iss_position"].get("longitude")
            
            namesList=[]
            for i in people:
                namesList.append(i.get("name"))
            
            spaceEmb=discord.Embed(title="Space Deets")
            namesList="\n".join(namesList)
            spaceEmb.add_field(name="People In Space:",value=namesList)
            spaceEmb.add_field(name="ISS Location",value=location)
            await ctx.send(embed=spaceEmb)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3a1c375... initial commit
    @commands.command(aliases=["kanyequote"])
    async def kanye(self,ctx):
        quote=requests.get("https://api.kanye.rest/").json().get("quote")
        await ctx.send(quote+"\n-Kanye West")

    @commands.command(aliases=["skin"])
    async def minecraftskin(self,ctx,username=None):
        if not username:
            username="RandomIsYes"

        embed=discord.Embed(title="Minecraft Skin For {}".format(username))
        embed.set_thumbnail(url="https://minotar.net/body/{}/300.png".format(username))
        embed.set_footer(text="Powered By Minotaur")
        await ctx.send(embed=embed)

<<<<<<< HEAD
=======
>>>>>>> c754cab... Music Functionality
=======
>>>>>>> 3a1c375... initial commit
    @commands.command(aliases=["pokemon"])
    async def pokedex(self,ctx,pokemon=None):
        if pokemon:
            try:
                
                pokedex=requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon.lower()).json()
                imgUrl=pokedex.get("sprites").get("front_default")

                types=pokedex.get("types")
                weight=pokedex.get("weight")
                abilities=pokedex.get("abilities")
                species=requests.get(pokedex.get("species").get("url")).json()
                for i in species.get("flavor_text_entries"):
                    if i.get("language").get("name")=="en":
                        desc=i.get("flavor_text")
                stats=pokedex.get("stats")
                pokeEmbed=discord.Embed(title="Information for Pokémon "+pokemon[0].upper()+pokemon[1:],color=discord.Color.random(),description=desc,footer="Powered By PokeApi. https://pokeapi.co/")
                for i in stats:
                    pokeName=i.get("stat").get("name")
                    print(pokeName)
                    pokeEmbed.add_field(name=' '.join((pokeName[0].upper()+pokeName[1:]).split('-')),value=i.get("base_stat"),inline=True)
                typeList=[]
                abilityList=[]

                for i in types:
                    typeList.append(i.get("type").get("name"))
                for i in abilities:
                    abilityList.append(i.get("ability").get("name"))

                
                pokeEmbed.set_thumbnail(url=imgUrl)
                pokeEmbed.add_field(name="Type(s)",value=",".join(typeList),inline=True)
                pokeEmbed.add_field(name="Abilities",value=",".join(abilityList),inline=True)
                pokeEmbed.add_field(name="Weight",value=str(weight/10)+" KG",inline=True)
                try:
                    evolvesFrom=species.get("evolves_from_species").get("name")
                    pokeEmbed.add_field(name="Evolves From",value=evolvesFrom,inline=True)
                except:
                    pokeEmbed.add_field(name="Evolves From",value="None",inline=True)



                await ctx.send(embed=pokeEmbed)

            except Exception as e:
                print(e)
                await ctx.send("Something went wrong. Error")
        else:
            await ctx.send("Maybe Try Providing a Pokemon next time?")



    
def setup(bot):
    bot.add_cog(Apis(bot))
    
        