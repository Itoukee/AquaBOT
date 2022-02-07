import discord
from discord.ext import commands


class Initialisation(commands.Cog):

    def __init__(self, bot):
        message = bot
        print('__init__ is Ready')
    

    @commands.command(brief ="shows the latency between you and me")
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency*1000)}ms')

    @commands.command(brief="Proposez vos idées ici")
    async def rapport(self,ctx,*,rapport:str):
        embed=discord.Embed(
            description="Votre idée a été bien enregistrée puis anonymisée",
            colour = discord.Colour.dark_gold()
        )
        print(rapport)
        user=message.get_user(363711838690476034)
        await ctx.send(embed=embed)
        await user.send(f"Il y a une nouvelle proposition : {rapport}")


    @commands.command(brief="Check me !")
    async def aqua(self,ctx):
        aqua = discord.Embed(
            title ="Hi it's me !",
            description ="The first completly useless bot !!",
            url="https://discord.gg/HbbCZTr",
            colour = discord.Colour.blue()
        )
        aqua.add_field(name="Music",value="High quality music")
        aqua.add_field(name="Card Game",value="Show your strength !")
        aqua.set_footer(text=f'made by Itstrike#5496  discord.py 1.3.3')
        aqua.set_image(url="https://static.zerochan.net/Aqua.%28KonoSuba%29.full.1962810.jpg")
        await ctx.send(embed=aqua)
"""
    @commands.command(pass_context=True)
    async def help(self,ctx):
       
        page1= discord.Embed(
            title="Liste des commandes catégorie fun !",
            colour = 0x56668
        )
        page1.add_field(name="📸",value="avatar")
        page1.add_field(name="⚜️",value="eight_ball")
        page1.add_field(name="📚",value="wiki",inline=True)
        page1.add_field(name="🖐️",value="add_answ")
        
        
        page2=discord.Embed(
            title='Page 2/3',
            description='Description',
            colour=discord.Colour.orange()
        )
        page3=discord.Embed(
            title='Page 3/3',
            description='Description',
            colour=discord.Colour.orange()
        )

        pages=[page1,page2,page3]
        message = await ctx.send(embed=page1)
        await message.add_reaction('\u25c0')
        await message.add_reaction('\u25b6')

        i = 0
        emoji = ''
        while True:
            if emoji == '\u25c0':
                 if i>0:
                    i-=1
                    await message.edit_message(embed=pages[i])

            if emoji == '\u25b6':
                 if i<2:
                    i+=1
                    await message.edit_message(embed=pages[i])
            
            res=await bot.wait_for('reaction_add',message=message,timeout=30)
            if res == None:
                break 
            if str(res[1]) != 'Aqua':
                emoji = str(res[0].emoji)
                await message.remove_reaction(res[0].emoji,res[1])
            await message.clear_reaction(message)
"""

def setup(bot):
    bot.add_cog(Initialisation(bot))

    