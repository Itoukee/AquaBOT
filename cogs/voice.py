import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
from mutagen import mp3
import asyncio

class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('Music is Ready')
    
    @commands.command(brief="Arrive dans le vocal",pass_context=True,aliases=['j','jo'])
    async def join(self,ctx):
        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients,guild=ctx.guild)
        voice = await channel.connect()
        await ctx.send("Je suis connectée !")
    
    
    @commands.command(brief="Quitte le vocal",pass_context=True, aliases=['l', 'lea'])
    async def leave(self,ctx):
         channel = ctx.message.author.voice.channel
         voice = get(self.bot.voice_clients, guild=ctx.guild)

         if voice and voice.is_connected():
             await voice.disconnect()
             print(f"J'ai quitté {channel}")
             await ctx.send(f"Je suis partie de : {channel}")
         else:
             await ctx.send("Je ne suis pas dans un vocal")

    @commands.command(brief="Joue de la musique ytb",pass_context=True,aliases=['p','pl'])
    async def play(self,ctx,url):
        auteur = ctx.message.author
        avatar_auteur = auteur.avatar_url
        song_there = os.path.isfile("song.mp3")
        try:
             if song_there:
                 os.remove("song.mp3")
                 print("Removed old song file")
        except PermissionError:
             print("Trying to delete song file, but it's being played")
             await ctx.send("ERROR: Je joue déjà une musique")
             return

        await ctx.send("Je te prépare ça !")

        voice = get(self.bot.voice_clients, guild=ctx.guild)

        ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
             print("Downloading audio now\n")
             ydl.cache.remove()
             ydl.download([url])
        info = ydl.extract_info(url,download=False)

        for file in os.listdir("./"):
             if file.endswith(".mp3"):
                 name = file
                 print(f"Renamed File: {file}\n")
                 os.rename(file, "song.mp3")
        
        voice.play(discord.FFmpegPCMAudio("song.mp3"), after= lambda e:print("Song Done !"))
        
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.9
        nname = name.rsplit("-", 2)
        embed = discord.Embed(
            title = f"{nname[0]}",
            url = url,
            color = discord.Color.dark_orange()
            
        )
        embed.set_author(name = "Écoute du :",icon_url="https://imgur.com/k8jUvcZ")
        if info['duration']/60 < 1 :
            embed.add_field(name="durée (s):play_pause:",value=info['duration'])
        else:
            embed.add_field(name="durée (min) :play_pause:",value=info['duration']/60)
        embed.add_field(name=":thumbsup::",value=info['like_count'])
        embed.set_footer(icon_url=f"{avatar_auteur}",text=f"Demandé par {auteur}")
        await ctx.send(embed = embed)
        print("playing\n")

       

    
    @commands.command(brief = "un mix d'1h30 d'op !")        
    async def animix1(self,ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        voice.play(discord.FFmpegPCMAudio("mixs/animix.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.9
        embed = discord.Embed(
            title = "Bonne séance d'op !"

        )
        embed.add_field(name="1.Kimetsu no yaiba",value='Gurenge')
        embed.add_field(name="2.Shingeki no Kyojin",value="Shokei to Shikabane",inline=True)
        embed.add_field(name="3.DanMachi ",value="HELLO to DREAM")
        embed.add_field(name="4.Mob Psycho 100 ",value="99.9",inline=True)
        embed.add_field(name="5.Psycho-Pass ",value="Who-ya Extended")
        embed.add_field(name="6.Fairy Tail",value="MORE THAN LIKE",inline=True)
        embed.add_field(name="7.Shokugeki No Soma",value="Chronos")
        embed.add_field(name="8.Black Clover",value="RIGHT NOW",inline=True)
        embed.add_field(name="9.Dororo",value="Kaen")
        embed.add_field(name="10. Kanata no Astra ",value="Star*frost",inline=True)
        embed.add_field(name="11.Dr.Stone",value="Sangenshoku",inline=True)
        embed.add_field(name="12.SAO",value="Resolution")
        embed.add_field(name="13.Kakegurui",value="Kono Yubi Tomare",inline=True)
        embed.add_field(name="14.No Guns Life",value="MOTOR CITY")
        embed.add_field(name="15.Kaguya-sama: Love is War",value="Love Dramatic",inline=True)
        embed.add_field(name="16.One Punch Man",value="Seijaku no Apostle")
        embed.add_field(name="17.Yakusoku no Neverland",value="Touch off",inline=True)
        embed.add_field(name="18.Radiant",value="Naraku")
        embed.add_field(name="19.Tate no Yuusha no Nariagari",value="RISE",inline=True)
        embed.add_field(name="20.Boku no Hero",value="Polaris")
        embed.add_field(name="21.Jojo",value="Uragirimono no Requiem",inline=True)
        embed.add_field(name="22.Bungou Stray Dogs",value="Setsuna no Ai")
        embed.add_field(name="23.Vinland Saga",value="MUKANJYO",inline=True)
        embed.add_field(name="24.Nanatsu no Taizai",value="ROB THE FRONTIER")
        embed.add_field(name="25.Fate/Grand Order",value="Phantom Joke",inline=True)
        await ctx.send(embed = embed)
    

    @commands.command()
    async def animix2(self,ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        voice.play(discord.FFmpegPCMAudio("mixs/animix2.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.9
        embed = discord.Embed(
            title = "Bonne séance d'op !"

        )
       # embed.add_field(name="1.Kimetsu no yaiba",value='Gurenge')
       # embed.add_field(name="2.Shingeki no Kyojin",value="Shokei to Shikabane",inline=True)
        #embed.add_field(name="3.DanMachi ",value="HELLO to DREAM")
        #embed.add_field(name="4.Mob Psycho 100 ",value="99.9",inline=True)
        #embed.add_field(name="5.Psycho-Pass ",value="Who-ya Extended")
       # embed.add_field(name="6.Fairy Tail",value="MORE THAN LIKE",inline=True)
        ##embed.add_field(name="7.Shokugeki No Soma",value="Chronos")
     #   embed.add_field(name="8.Black Clover",value="RIGHT NOW",inline=True)
      #  embed.add_field(name="9.Dororo",value="Kaen")
       # embed.add_field(name="10. Kanata no Astra ",value="Star*frost",inline=True)
     #   embed.add_field(name="11.Dr.Stone",value="Sangenshoku",inline=True)
      #  embed.add_field(name="12.SAO",value="Resolution")
     #  # embed.add_field(name="13.Kakegurui",value="Kono Yubi Tomare",inline=True)
      #  embed.add_field(name="14.No Guns Life",value="MOTOR CITY")
       # embed.add_field(name="15.Kaguya-sama: Love is War",value="Love Dramatic",inline=True)
      #  embed.add_field(name="16.One Punch Man",value="Seijaku no Apostle")
       ## embed.add_field(name="17.Yakusoku no Neverland",value="Touch off",inline=True)
       # embed.add_field(name="18.Radiant",value="Naraku")
        #embed.add_field(name="19.Tate no Yuusha no Nariagari",value="RISE",inline=True)
        #embed.add_field(name="20.Boku no Hero",value="Polaris")
        #embed.add_field(name="21.Jojo",value="Uragirimono no Requiem",inline=True)
        #embed.add_field(name="22.Bungou Stray Dogs",value="Setsuna no Ai")
        #embed.add_field(name="23.Vinland Saga",value="MUKANJYO",inline=True)
       # embed.add_field(name="24.Nanatsu no Taizai",value="ROB THE FRONTIER")
       # embed.add_field(name="25.Fate/Grand Order",value="Phantom Joke",inline=True)
        await ctx.send(embed = embed)


    @commands.command(brief="Un mix d'1h de musique pour jouer !")
    async def gamemix(self,ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        voice.play(discord.FFmpegPCMAudio("mixs/gamemix.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.9
        embed = discord.Embed(
            title = "Bonne séance de jeu !"

        )
        await ctx.send(embed = embed)

    @commands.command(brief="Un mix d'1h de musique pour jouer !")
    async def rollback(self,ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        voice.play(discord.FFmpegPCMAudio("song.mp3"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.9
        embed = discord.Embed(
            title = "Désolé de l'erreur !"

        )
        await ctx.send(embed = embed)


    @commands.command(brief="Met en pause la musique")
    async def pause(self,ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        voice.pause()
        await ctx.send(":pause_button: Song stopped")

    @commands.command(brief="La reprend")
    async def resume(self,ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        voice.resume()
        await ctx.send(":arrow_forward: Song resumed")

    @commands.command(brief="Arrête la musique")
    async def stop(self,ctx):
        global loop
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        loop = False
        voice.stop()
        await ctx.send(":stop_button: Song stopped")


def setup(bot):
    bot.add_cog(Music(bot))