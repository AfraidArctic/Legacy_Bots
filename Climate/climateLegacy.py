import discord
from discord.ext import commands
import random
import asyncio
import os, sys


# Lista del clima: START!
soleimg = ["https://1.bp.blogspot.com/-ITpOmLQVycc/UbHro0HHa6I/AAAAAAAAA4I/tPS1gJaURwE/w1200-h630-p-k-no-nu/Sky+Anime+Landscape+08.jpg"]
precimg = ["https://images-ext-2.discordapp.net/external/Y65gejL-DQsVfkfgAxKRiXGOu9FU3dSw-Rq379310i4/https/i.pinimg.com/originals/7c/d2/31/7cd231e9446006464022047c21ff6dbb.jpg?width=835&height=425", "https://cdn.discordapp.com/attachments/742484116599078972/742484455595311245/1512148350_original.gif"]
tormimg = ["https://cdn.discordapp.com/attachments/742484116599078972/742485562291781793/3meD.gif"]
nublimg = ["https://i.pinimg.com/originals/8b/5d/83/8b5d8356af651e1d3dc4493585714595.jpg"]

soleado = discord.Embed(title='Dia soleado', description='¡Hoy es un dia soleado!. Esto es un gran alivio para aquellos al norte de Laigho, asi que seria un bonito dia en la zona nevada. Para aquellos en los campos, es solamente otro dia de arduo trabajo en el sol... ', 
colour=0xFFC856)
soleado.set_image(url=random.choice(soleimg))

lluvia = discord.Embed(title='Dia lluvioso / nevado', description='¡El dia de hoy llueve!. Es bastante relajante para aquellos que han pasado un dia soleado, o un dolor para aquellos que han tenido que soportar el frio.\n\n Para el dia de hoy, en los lugares frios cae nieve. En otra nota, para aquellos que no viven en climas frios esto no deberia de ser un problema ya que en vez de nieve hay lluvia.', 
colour=0x0799D4)
lluvia.set_image(url=random.choice(precimg))

tormenta = discord.Embed(title='Dia tormentoso', description='El dia de hoy llueve y caen rayos; ¡Una tormenta!. Recomendamos al menos llevar una cota de malla, para no arriesgarse a sufrir algun daño, por otro lado, mucho menos recomendamos alzar algun objeto metalico al aire. ', 
colour=0x43829A)
tormenta.set_image(url=random.choice(tormimg))

neblina = discord.Embed(title='Dia nublado', description='Hoy hay algo de neblina en los bosques, campos y las cercanias de las montañas (y en las montañas en si tambien). Tal vez los viajes den algo de miedo, pero no se preocupen,  una linterna deberia de ser suficiente para evitar perderse, y tambien les recomendamos que sigan los caminos y no se aventuren demasiado en el bosque.', 
colour=0xC8DAE9)
neblina.set_image(url=random.choice(nublimg))

LISTatmos = [soleado, lluvia, tormenta, neblina]
# Lista del clima: END!


# Hora: START!

diaimg = [""]

nocimg = ["https://media.discordapp.net/attachments/876152970109124658/876153274405883925/IMG_20210814_141501.JPG?width=608&height=425"]

dia = discord.Embed(title='Ciclo de dia', 
description='', 
colour=0xFEF567)
dia.set_image(url=random.choice(diaimg))

noche = discord.Embed(title='Ciclo de noche', 
description='', 
colour=0x133052)
noche.set_image(url=random.choice(nocimg))

LISThora = [dia, noche]
#  Hora: END!

my_secret = os.environ['TOKEN']
bot = commands.Bot(command_prefix=">c ", help_command=None)

async def clima():
    await bot.wait_until_ready()
    channel = bot.get_channel(id=866396545381040148)
    while not bot.is_closed():
        await channel.send(embed=random.choice(LISTatmos))
        await asyncio.sleep(86400) #Configurado en segundos


# Iniciando
@bot.event
async def on_ready():
  print(f"Python version: {sys.version}\n")
  print(f'El bot: {bot.user.name} ha iniciado')
  print(f'Bot id: {bot.user.id}')
  print(f'Actualmente en: {len(bot.guilds)} servidores')
  print(f'Ping: {round(bot.latency * 1000)} ms')


bot.loop.create_task(clima())
bot.run(os.getenv('TOKEN'))
