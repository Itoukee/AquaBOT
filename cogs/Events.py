import discord
from discord.ext import commands
import random

Emojis = [":yaranaika:616016997159010304",":WTF:616020008744648737",":Non:616020140571754506",":Chiiscared:633405566680563743",":PeepoWeird:635859190790750208",
          ":peepogay:588744372837810177",":KannaFuck:616019093581070336"]

emos = [":yaranaika:616016997159010304",":WTF:616020008744648737",":KannaFuck:616019093581070336"]

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Events are ready')
        


    @commands.Cog.listener()
    async def on_message(self,message):
        
         reaction = random.choice(Emojis)
         emo = random.randint(1,200)
         trigger = random.randint(1,20)
         if emo == 24:
            await message.add_reaction(reaction)
            await self.bot.process_commands(message)
         
         
         if trigger==5 and "^^" in message.content:
            channel = message.channel
            embed = discord.Embed(
                title = "HAAAAAAA",
                color = discord.Colour.darker_grey()
            )
            embed.set_image(url ="https://media.giphy.com/media/vk7VesvyZEwuI/giphy.gif")


def setup(bot):
    bot.add_cog(Events(bot))
    
