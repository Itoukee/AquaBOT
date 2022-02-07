import discord
from discord.ext import commands
import requests, json
import random
from random import randint

api_key = API_KEY
base_url = "http://api.openweathermap.org/data/2.5/weather?"
pays_dict = {"Afghanistan":0,"Albanie":1,"Algérie":2,"Argentine":6,"Arménie":7,"Australie":8,
             "Belgique":16,"Brésil":23,"Canada":30,"Chine":35,"Danemark":46,"Egypte":51,"France":59,"Allemagne":63,
             "Inde":76,"Italie":82,"Japon":84}


class Tools(commands.Cog):
    
    def __init__(self, bot):
        print('Tools are ready !')

    @commands.command()
    async def meteo(self,ctx,*,ville):
        city_name = ville
        complete_url = base_url+"appid="+api_key+"&q="+city_name
        response = requests.get(complete_url)
        x = response.json()

        if x["cod"] != "404":
            y = x["main"]
            current_temp = y ["temp"]
            current_press = y["pressure"]
            current_hum = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
        elif x["cod"] == "404":
            await ctx.send("Ville non trouvée ! Vous devriez donner le nom international !")
        emoji = "☁️"
        miss_meteo = discord.Embed(
            title = f"Météo de {ville} {emoji}",
            color = 0x48963,
            timestamp=ctx.message.created_at
        )
        miss_meteo.set_author(name="Miss Aqua",icon_url="https://imgur.com/k8jUvcZ")
        miss_meteo.add_field(name="__Température :__",value=f"{round(current_temp-273.15)}°C")
        miss_meteo.add_field(name="__Humidité :__",value=f"{current_hum}%")
        miss_meteo.add_field(name="__Temps :__",value=f"{weather_description}")
        miss_meteo.add_field(name="__Pression :__",value=f"{current_press} hPa")
        await ctx.send(embed = miss_meteo)

    @commands.command()
    async def corona(self,ctx,pays):
        url = 'https://api.covid19api.com/summary'
        response = requests.get(url).json()
        if pays in pays_dict:
            y = pays_dict[pays]
            x = response["Countries"][y]
            Coun =   x['Country']
            new_confirmed = x['NewConfirmed']
            total = x['TotalConfirmed']
            new_deaths = x['NewDeaths']
            total_deaths = x['TotalDeaths']
            new_rec = x['NewRecovered']
            total_recov = x['TotalRecovered']
            date = x['Date']
            ratio_d = ((total_deaths*100)/total)
            ratio_r = ((total_recov*100)/total)
            ratio_d = int(ratio_d)
            ratio_r = int(ratio_r)
            coron = discord.Embed(
                title = f"Coronavirus en {pays}",
                color = 0x14857

            )
            coron.add_field(name="Total contaminés",value=f"{total} pers.")
            coron.add_field(name="Nouveaux contaminés ",value=f"{new_confirmed} pers.")
            coron.add_field(name="Nouveaux décès ",value=f"{new_deaths} pers.")
            coron.add_field(name="Total décès",value=f"{total_deaths} pers.")
            coron.add_field(name="Total soignés",value=f"{total_recov} pers.")
            coron.add_field(name="Nouveaux soignés",value=f"{new_rec} pers.")
            coron.add_field(name="Ratio %",value=f"{ratio_d}% Décès, {ratio_r}% Soignés",inline=True)
            coron.set_footer(text=f"Mis à jour le {date}, API:covid19API")
            coron.set_image(url="https://media.wuerth.com/source/eshop/stmedia/wuerth/images/std.lang.all/resolutions/category/576px/3909940.jpg")
            await ctx.send(embed=coron)
        else:
            await ctx.send("Ce pays n'est pas encore répertorié, merci de demander à mon créateur !")
            return
        
        
      
    @commands.command()
    async def joke(self,ctx,tag):
        if tag == 'any':
            url = 'https://sv443.net/jokeapi/v2/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist'
            response = requests.get(url).json()
            category = response["category"]
            typee = response["type"]
            if typee == "twopart":
                setup = response["setup"]
                delivery = response["delivery"]
            else:
                jokes = response["joke"]
            
            
            clown = discord.Embed(
                color = 0x93654,
                description=f"Joke {category}"
            )
            if typee == "twopart":
                clown.add_field(name="Aqua's Jokes",value=f"{setup} \n {delivery}")
            else:
                clown.add_field(name="Aqua's Jokes",value=f"{jokes}")
            clown.set_footer(text="made with JokeAPI")
            await ctx.send(embed=clown)
            return
        else:
            await ctx.send("Tag non disponible pour le moment, utilisez `%joke any`")

    @commands.command()
    async def whichmeme(self,ctx):
        y = random.randint(0,100)
        y = int(y) 
        url ="https://api.imgflip.com/get_memes"
        response = requests.get(url).json()
        memes = response["data"]["memes"][y]
        name = memes["name"]
        urlmeme = memes["url"]
        urlmeme = urlmeme.lstrip("\£")
        embed = discord.Embed(
            title = "Meme finder",
            color = 0x05969,
            description=name,
            timestamp = ctx.message.created_at
        )
        embed.set_image(url=urlmeme)
        embed.set_footer(text="made with imgflip API")
        await ctx.send(embed=embed)
     


        

    @commands.command()
    async def trad(self,ctx,langue,text):
        if langue == 'anglais':
            p = 'D:\AquaBOT\langues\english.json'
            with open(p,'r') as write_file:
                data = json.load(write_file)
                if text in data:
                    a = data[text]
                    
                    trade = discord.Embed(
                        colour = 0x69874,
                        timestamp = ctx.message.created_at
                    )
                    trade.add_field(name="Input :",value=text)
                    trade.add_field(name="Output :",value=a)
                    trade.set_author(name=f"asked by {ctx.message.author}",icon_url=ctx.message.author.avatar_url)
                    await ctx.send(embed=trade)
                elif text not in data:
                    data[text]=0
                    write_file.close()
                    with open(p,'w') as new:
                        json.dump(data,new)
                    await ctx.send("Le mot a bien été envoyé et sera traduit d'ici ce soir !")
        else :
            await ctx.send("Cette langue n'est pas encore disponible !")          
            return        

               
            

def setup(bot):
    bot.add_cog(Tools(bot))
