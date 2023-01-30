# Importando
import asyncio
import discord
from discord import member, guild
from discord.ext import commands
import random
import json

import os

# Write and read de la base de datos
os.chdir("C:/Users/hendrix/Desktop/Abraham_Programacion/BotRPG_backup")

# NOTA IMPORTANTE
# "r" = read
# "w" = write
# NOTA IMPORTANTE

# Setup
bot = commands.Bot(command_prefix=">r ", help_command=None)

# Paginas aventurero
adpage1 = discord.Embed(title='Graduacion clase I', description='Requisitos:\n```- Haber matado 1 bestia rango 1 y traido sus restos.\n- Tener como minimo 14 años de edad.```', colour=0xFFFAFA)
adpage2 = discord.Embed(title='Ascenso a clase H', description='Requisitos:\n```- Haber matado 10 bestias rango 2 y traido sus restos.```', colour=0xFFFAFA)
adpage3 = discord.Embed(title='Ascenso a clase G', description='Requisitos:\n```- Haber matado 10 bestias rango 3 y traido sus restos.\n- Explorar una dungeon por primera vez y haberla despejado.```', colour=0xFFFAFA)
adpage4 = discord.Embed(title='Ascenso a clase F', description='Requisitos:\n```- Haber matado 20 bestias rango 4 y traido sus restos.\n- Explorar 2 dungeons rango E y haberlas despejado / realizar 3 misiones.```', colour=0xFFFAFA)
adpage5 = discord.Embed(title='Ascenso a clase E', description='Requisitos:\n```- Haber matado 50 bestias rango 3 / 25 bestias rango 4 / matar a un club de bandidos y traido sus restos.\n- Explorar 5 dungeons rango D y haberlas despejado / realizar 6 misiones.```', colour=0xFFFAFA)
adpage6 = discord.Embed(title='Ascenso a clase D', description='Requisitos:\n```- Haber matado 100 bestias rango 5 y traido sus restos.\n- Explorar 20 dungeons rango D y haberlas despejado. \n- Realizar 10 misiones.```', colour=0xFFFAFA)
adpage7 = discord.Embed(title='Ascenso a clase C', description='Requisitos:\n```- Haber matado 100 bestias rango 6 y traido sus restos.\n- Explorar 3 dungeons rango C y haberlas despejado.\n- Realizar 15 misiones.```', colour=0xFFFAFA)
adpage8 = discord.Embed(title='Ascenso a clase B', description='Requisitos:\n```- Haber matado 250 bestias rango 7 / 80 bestias rango 9 y traido sus restos.\n- Explorar 5 dungeon rango B y haberla despejado.```', colour=0xFFFAFA)
adpage9 = discord.Embed(title='Ascenso a clase A', description='Requisitos:\n```- Haber matado 1000 bestias rango 9 / 100 bestias rango 10 y traido sus restos.\n- Explorar 2 dungeon rango A y haberla despejado.\n- Haber defendido una ciudad de un desbordamiento.\n- Obtener descenso del espitiru familiar.```', colour=0xFFFAFA)
adpage10 = discord.Embed(title='Ascenso a clase S', description='Requisitos:\n```- Haber matado una bestia rango 11, 12 y otra rango 13 y traido sus restos.\n- Haber participado en una guerra. \n- Ser seleccionado por un dios.```', colour=0xFFFAFA)

bot.ad_pages = [adpage1, adpage2, adpage3, adpage4, adpage5, adpage6, adpage7, adpage8, adpage9, adpage10]

# Paginas mago
mapage1 = discord.Embed(title='', description='', colour=0xFFFAFA)

bot.ma_pages = [mapage1]

# Paginas domador
dopage1 = discord.Embed(title='', description='', colour=0xFFFAFA)

bot.do_pages = [dopage1]

# Paginas comerciante
copage1 = discord.Embed(title='Iniciado', description='Requisitos:\n```- Tener un negocio que sea sostenible luego de 3 meses.\n- Tener como minimo 16 años de edad```', colour=0xFFFAFA)
copage2 = discord.Embed(title='Ascenso a Nacional', description='Requisitos:\n```- Tener varios locales que sean importantes para el comercio.```', colour=0xFFFAFA)
copage3 = discord.Embed(title='Ascenso a Multinacional', description='Requisitos:\n```- Tener locales tanto en Nikocinis como en Lunubris.```', colour=0xFFFAFA)

bot.co_pages = [copage1, copage2, copage3]

# Bot en linea
@bot.event
async def on_ready():
    print(f'El bot: {bot.user.name} ha iniciado')
    print(f'Bot id: {bot.user.id}')
    print(f'Actualmente en: {len(bot.guilds)} servidores')
    for guild in bot.guilds:
        print(guild.name)
    print(f'Ping: {round(bot.latency * 1000)} ms')
    await bot.change_presence(activity=discord.Game(name='Prefix: ">r"'))

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
@bot.command(aliases=["ms"])
async def ping(ctx):
    await ctx.send(f'Ping: {round(bot.latency * 1000)} ms')


# LISTA DE COMANDOS
@bot.command(aliases=["comandos", "help"])
async def info(ctx):
    embed = discord.Embed(title='Lista de comandos', description='Si sucede algun error, reportar el bug al DM de Afraid Taiko#9792!', colour=0xFFFAFA)
    embed.set_author(name="Teriventium")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/866413781181792266/867493430237724672/Libro_negativo.png")
    embed.add_field(name='Comandos offrol', value='```>ping / ms```', inline=False)
    embed.add_field(name='Comandos inrol', value='```>map / mapa\n>puntos_de_habilidad / surplusxp\n>gremio nombre_del_gremio\n>rng\n>rfg```', inline=False)
    embed.add_field(name='Comandos del staff', value='```>gain_surXP```', inline=False)
    embed.set_footer(text='Si tienes alguna duda, consulta al staff en el canal de recomendaciones y dudas con un ping a @Ayudante')
    await ctx.send(embed=embed)



# Mapa embed
@bot.command(aliases=["map"])
async def mapa(ctx):
    embed = discord.Embed(title='Mapa de Teriventium', description=f"", colour=0xFFFAFA)
    user = ctx.author
    await user.send(embed=embed)


# Random Number Generator
@bot.command()
async def rng(ctx, arg0, arg1):
    nmr0 = int(arg0)
    nmr1 = int(arg1)
    num = random.randint(nmr0, nmr1)
    await ctx.send(f'{arg0} - {arg1} = {num}')


# Random Float Generator
@bot.command()
async def rfg(ctx, arg0, arg1):
    nmr0 = float(arg0)
    nmr1 = float(arg1)
    num = random.uniform(nmr0, nmr1)
    await ctx.send(f'{arg0} - {arg1} = {num}')


# Guia de niveles
@bot.group(name='gremio', invoke_without_command=True)
async def gremio(ctx):
    await ctx.send("**Subcomandos:** ```aventurero ; mago ; domador ; comercio```")


@gremio.command(name='aventurero')
@commands.has_any_role('inrol', 'Dungeon master')
async def aventurero_subcommand(ctx):
        buttons0 = [u"\u21A9", u"\u2B05", u"\u274E", u"\u27A1", u"\u21AA"]
        current0 = 0
        msg0 = await ctx.send(embed=bot.ad_pages[current0])

        for button in buttons0:
            await msg0.add_reaction(button)

        while True:
            try:
                reaction, user = await bot.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons0, timeout=60.0)

            except asyncio.TimeoutError:
                embed = bot.ad_pages[current0]
                embed.set_footer(text='ERROR: Timed out')
                await msg0.clear_reactions()
                await msg0.edit(embed=bot.ad_pages[current0])

            else:
                previous_page = current0

                if reaction.emoji == u"\u21A9":
                    current0 = 0

                elif reaction.emoji == u"\u2B05":
                    if current0 > 0:
                        current0 -= 1

                elif reaction.emoji == u"\u274E":
                    await ctx.message.delete()
                    await msg0.delete()

                elif reaction.emoji == u"\u27A1":
                    if current0 < len(bot.ad_pages)-1:
                        current0 += 1

                elif reaction.emoji == u"\u21AA":
                    current0 = len(bot.ad_pages)-1

                for button in buttons0:
                    await msg0.remove_reaction(button, ctx.author)

                if current0 != previous_page:
                    await msg0.edit(embed=bot.ad_pages[current0])


@gremio.command(name='comercio')
@commands.has_any_role('inrol', 'Dungeon master')
async def comercio_subcommand(ctx):
    buttons1 = [u"\u2B05", u"\u274E", u"\u27A1"]
    current1 = 0
    msg1 = await ctx.send(embed=bot.co_pages[current1])

    for button in buttons1:
        await msg1.add_reaction(button)

    while True:
        try:
            reaction, user = await bot.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons1, timeout=60.0)

        except asyncio.TimeoutError:
            embed = bot.co_pages[current1]
            embed.set_footer(text='ERROR: Timed out')
            await msg1.clear_reactions()
            await msg1.edit(embed=bot.co_pages[current1])

        else:
            previous_page = current1

            if reaction.emoji == u"\u2B05":
                if current1 > 0:
                    current1 -= 1

            elif reaction.emoji == u"\u274E":
                await ctx.message.delete()
                await msg1.delete()

            elif reaction.emoji == u"\u27A1":
                if current1 < len(bot.co_pages)-1:
                    current1 += 1

            for button in buttons1:
                await msg1.remove_reaction(button, ctx.author)

            if current1 != previous_page:
                await msg1.edit(embed=bot.co_pages[current1])


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



bot.run("ODY1OTg3MDM5NzY1MjAwOTE2.YPL_Rw.FGVw2RFKGb4PFDsHSP6l4_QdNe4")
