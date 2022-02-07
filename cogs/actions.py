import discord
from discord.ext import commands
import random
import PIL
import urllib.parse, urllib.request, re


sl4ps = ['https://media.giphy.com/media/jLeyZWgtwgr2U/giphy.gif','https://media2.giphy.com/media/j2h2sB2WkbH6U/giphy.gif','https://media3.giphy.com/media/NQGQW9YTBc9Co/giphy.gif',
'https://tof.cx/images/2017/08/26/e8f89035f4ae08e93f8f5db78527e0ff.gif','https://media.giphy.com/media/jLeyZWgtwgr2U/giphy.gif','https://thumbs.gfycat.com/LegalExhaustedEuropeanpolecat-size_restricted.gif']

devenir = ["https://cdn.discordapp.com/attachments/573206959667281920/690659536562028594/EBETaFPXUAI0SQo.jpg",
"https://cdn.discordapp.com/attachments/573168296359100436/689874583578476566/EHTHX0yXkAAhq-S.png",
"https://cdn.discordapp.com/attachments/642338920851570699/693889548526158055/deviendrefou.png",
"https://images-ext-1.discordapp.net/external/mJvHsK2DwQ_AdcuLfv_34lb98G1GA-gvZ22w93ke2og/%3Fwidth%3D573%26height%3D670/https/media.discordapp.net/attachments/690291187013386290/694523074833285170/deviene.png"
]
pbagarre = ["https://cdn.discordapp.com/attachments/558794425707266050/697251061882290186/unknown-1214_1.png","https://cdn.discordapp.com/attachments/573206959667281920/690661614508310619/Screenshot_20200317_192156.jpg"]
yourself = ["Are you trying to beat your meat ??","You hurt yourself in confusion"]

class Action(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        print('Actions Ready')


    @commands.command(
        brief = "Someone who should drown"
    )
    async def canoë(self,ctx,member: discord.Member):

        canoë = discord.Embed(
            description = f'Looks like {member.mention} is a canoë',
            color = discord.Colour.gold()
              
        )
        canoë.set_image(url='https://media.giphy.com/media/l0HlMG1EX2H38cZeE/giphy.gif')
        await ctx.send(embed = canoë)

    

    @commands.command(
        brief = "Do you want to...SLAP ?"
    )
    async def slap(self,ctx,member: discord.Member):
        slap = discord.Embed(
            description = f'Looks like {member.mention} deserved it',
            color = discord.Colour.gold()
              
        )
        slap.set_image(url=random.choice(sl4ps))
        await ctx.send(embed =slap)

    @commands.command(brief="J'AI GAGNÉ LA BAGARRE")
    async def gbagarre(self,ctx):
        bagarre = discord.Embed(
            color = discord.Colour.purple()
        )
        bagarre.set_image(url ="https://cdn.discordapp.com/attachments/573206959667281920/690659497324183622/EELw03hXUAIgqyD.jpg")
        await ctx.send(embed=bagarre)
    
    @commands.command(brief="LA BAGARRE")
    async def bagarre(self,ctx):
        bagarre = discord.Embed(
            color = discord.Colour.purple()
        )
        bagarre.set_image(url ="https://cdn.discordapp.com/attachments/573206959667281920/690661483662802974/Screenshot_20200317_192142.jpg")
        await ctx.send(embed=bagarre)
    
    @commands.command(brief="J'AI PERDU LA BAGARRE")
    async def pbagarre(self,ctx,):
        bagarre = discord.Embed(
              color = discord.Colour.purple()
         )
        bagarre.set_image(url =random.choice(pbagarre))
        await ctx.send(embed=bagarre)
    
    @commands.command(brief="JE DEVIENE FOU")
    async def deviendre(self,ctx):
       deviendre = discord.Embed(
            color = discord.Colour.purple()
        )
       deviendre.set_image(url =random.choice(devenir))
       await ctx.send(embed=deviendre)
    
    @commands.command(brief = "What else to say ?")
    async def octogone(self,ctx,member:discord.Member):
        winner = random.randint(1,2)
        if member == ctx.message.author:
            await ctx.send(random.choice(yourself))
        else:
             if winner == 1:
                 await ctx.send(f"Le gagnant est : {member}!!")
             else:
                 await ctx.send(f"Le gagnant est : {ctx.message.author}!!")   
      
    @canoë.error
    async def canoë_error(self,ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.send("Précisez l'argument manquant de type @Pomme")

    @slap.error
    async def slap_error(self,ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.send("Précisez l'argument manquant de type @Pomme")

    @octogone.error
    async def octogone_error(self,ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.send("Précisez l'adversaire manquant de type `%octogone @Pomme`")

    


    @commands.command(brief="Cherche une vidéo selon son nom")
    async def recherche_ytb(self,ctx,*,search):
        query_string = urllib.parse.urlencode({
            'search_query':search
        })
        htm_content = urllib.request.urlopen(
            'https://www.youtube.com/results?'+query_string
        )

        search_results = re.findall('href=\"\\/watch\\?v=(.{11})',htm_content.read().decode())
        await ctx.send('https://youtube.com./watch?v='+search_results[0])

    @commands.command(brief="Affiche les informations de votre profil")
    async def profil(self,ctx,user:discord.Member):
            if isinstance(user,discord.Member):
                role = user.top_role.name
                if role == "@everyone":
                    role = "N/A"

                voice_state = None if not user.voice else user.voice.channel
           
            em = discord.Embed(timestamp=ctx.message.created_at,colour=0x708DD0)
            em.add_field(name='User ID',value=user.id,inline=True)
            if isinstance(user,discord.Member):
                em.add_field(name='Surnom', value=user.nick, inline=True)
                em.add_field(name='Status', value=user.status, inline=True)
                em.add_field(name='Vocal', value=voice_state, inline=True)
                em.add_field(name='Jeu', value=user.activity, inline=True)
                em.add_field(name='Role', value=role, inline=True)
            em.add_field(name='Compte créé le ',value=user.created_at.__format__('%A,%d.%B,%Y %H:%M:%S'))
            if isinstance(user,discord.Member):
                em.add_field(name='Rejoint le serv le ',value=user.joined_at.__format__('%A,%d.%B,%Y %H:%M:%S'))
            em.set_thumbnail(url=user.avatar_url)
            em.set_author(name=user,icon_url='https://media.discordapp.net/attachments/574631772986277898/710210513099030568/ad9f3ecc63bc16aca45385e6d2362c61.png')
            await ctx.send(embed=em)
            

def setup(bot):
    bot.add_cog(Action(bot))