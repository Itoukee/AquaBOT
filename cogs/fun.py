import discord
from discord.ext import commands
import random
import os
import shutil
import urllib.request
import requests
import wikipedia
from PIL import Image,ImageFont,ImageDraw



possible_responses=['Non jamais',
        'Peut-être un jour',
        'Passe sous le bureau et on en reparle',
        'Oui',
        'Demain',
        'Dans un futur lointain',
        'A ton avis, petite merde qui me fait bosser',
        'Bah oé',
        'Après 200 essais',
        '*dort*',
        'Ui Maître',
        'Même pas en rêves',
        'Tu dois embrasser Hanouna et oui',
        'Non, et en+ tu pues',
        'Ui Kyaaaaaaaaaaaaaaaaa~',
        'Selon mes données, Oui',
        'Il semblerait',
        'Ptdr t ki ?',
        '**BUUUURP**',
        'Demandez à Klq Monkahmmm'
    ]


class Fun(commands.Cog):
    
    
    def __init__(self, bot):
        self.bot = bot
        print('Fun Ready')

    @commands.command(brief = "shows the avatar of someone")
    async def avatar(self,ctx, member: discord.Member):
    
        show_avatar = discord.Embed(
            title = f"{member}'s profile picture",
            timestamp=ctx.message.created_at,
            color = discord.Color.dark_blue()
        )
        show_avatar.set_image(url='{}'.format(member.avatar_url))
        await ctx.send(embed=show_avatar)
        
    
        

    @commands.command(brief="Show your big peepee to everyone")
    async def size(self,ctx):
        desc = random.uniform(5,29)
        dstring = str(desc)
        await ctx.send('La taille du Démon de '+ctx.message.author.mention +' est de '+dstring+'cm :banana:')
  
    
    @commands.command(brief ="Help me by updating the list")
    async def add_answ(self,ctx,*,prop:str):
        possible_responses.append(prop)
        rep=discord.Embed(
            title=f'Votre proposition a bien été prise en compte !',
            description=prop,
            timestamp=ctx.message.created_at,
            colour=discord.Colour.dark_red()
        )
        print(prop)
        user=self.bot.get_user(363711838690476034)
        await ctx.send(embed=rep)
        await user.send(prop)
    
    @commands.command()
    async def hbataille(self,ctx):
        bhataille = random.randint(1,315024)
        await ctx.send (f'Votre doujin est le : https://nhentai.net/g/{bhataille}/'+ "\n"+ctx.message.author.mention)

    @commands.command(brief="God is hearing you")
    async def eight_ball(self,ctx,*,question):
        await ctx.send(f'Question: {question}\nRéponse: {random.choice(possible_responses)+", "+ ctx.message.author.mention}')
    
    @commands.command()
    async def wiki(self,ctx,*,demande):
       wikipedia.set_lang("fr")
       image = wikipedia.page(demande).images[0]
       trouve = wikipedia.summary(demande,sentences=2)
       
       em = discord.Embed(
           title=demande,
           timestamp = ctx.message.created_at,
           colour = 0x708DD0
       )
       em.add_field(name="Résumé : ",value=trouve)
       em.set_image(url=image)
       await ctx.send(embed=em)


    '''Merci à Newen et 
        -EvieePy
        -Gio
        -Akaisorani pour cette partie'''
    @commands.command()
    async def img_two(self,ctx,message):
       url = message
       await ctx.send("Image reçue ! Merci de patienter quelques temps je ne suis pas très rapide ! ")
       resp = requests.get(url,stream=True)
       img_there=os.path.isfile('local_image.png')
       img_here = os.path.isfile('local_modif.png')
       if img_there:
            os.remove("local_image.png")
            if img_here:
                os.remove("local_modif.png") 
       
       
       local_img = open('local_image.png','wb')
       resp.raw.decode_content = True
       shutil.copyfileobj(resp.raw,local_img)
       del resp
       imge = Image.open('local_image.png') 
       img_modif =imge.convert("P",palette=Image.ADAPTIVE,colors=2)
       img_modif = img_modif.save("local_modif.png")
       await ctx.send(file=discord.File('local_modif.png'))

    @commands.command()
    async def blinking(self,ctx,*,texte):
        blink = Image.open('bwm.jpg')
        draw = ImageDraw.Draw(blink)
        x = len(texte)
        if x>20:
            x = 100
        else:
            x = 150
        font = ImageFont.truetype('impact.ttf',x)
        text = f"{texte}"
        draw.text((400-len(text)*4,5),text,fill=(255,255,255),font=font,align="center")
        blink.save('bwm_mod.jpg')
        await ctx.send(file=discord.File('bwm_mod.jpg'))
    
    @commands.command()
    async def coffin(self,ctx,*,texte):
        coff = Image.open('coffin.jpg')
        draw = ImageDraw.Draw(coff)
        x = len(texte)
        if x>20:
            x = 50
        else:
            x = 75
        font = ImageFont.truetype('impact.ttf',x)
        text = f"{texte}"
        draw.text((400-len(text)*2,5),text,fill=(0,0,0),font=font,align="center")
        coff.save('coffin_mod.jpg')
        await ctx.send(file=discord.File('coffin_mod.jpg'))



    @avatar.error
    async def avatar_author(self,ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            show_avatar = discord.Embed(
            title = f"{ctx.message.author}'s profile picture",
            timestamp=ctx.message.created_at,
            color = discord.Color.dark_blue()
            )
            show_avatar.set_image(url='{}'.format(ctx.message.author.avatar_url))
            await ctx.send(embed=show_avatar)

def setup(bot):
    bot.add_cog(Fun(bot))