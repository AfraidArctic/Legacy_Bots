import discord
from discord.ext import commands
import random
from asyncio import sleep
import os

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!g ', intents = intents)
bot.remove_command('help')
my_secret = os.environ['contrasena']

# Iniciando
@bot.event
async def on_ready():
  print(f'El bot: {bot.user.name} ha iniciado')
  print(f'Bot id: {bot.user.id}')
  print(f'Actualmente en: {len(bot.guilds)} servidores')
  print(f'Ping: {round(bot.latency * 1000)} ms')


# Ping check
@bot.command(aliases=['ms'])
async def ping(ctx):
  await ctx.send(f'Ping: `{round(bot.latency * 1000)} ms`')


# Lista de comandos
@bot.command(aliases=["comandos", "info"])
async def help(ctx):
  embed = discord.Embed(title='Lista de comandos', description='Si sucede algun error, reportar el bug al DM de Afraid Taiko#9792!', colour=0xFF000)
  embed.set_thumbnail(url="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/b8/b8ba4185551e528c01bacd4aba58cf25fa458596_full.jpg")

  embed.add_field(name='Comandos de moderacion', value='```alarm, ban, kick, ping, unban, userlist, user```', inline=False)
  embed.add_field(name='Reacciones', value='```angry, cringe, cry, dance, dies, everyone, happy, hug, kill, leave, lewd, like, love, nod, pain, pat, pog, pognt, punch, run, sad, scream, shrug, simp, slap, sleep, suicide, think, thot, trolling, what```', inline=False)

  embed.set_footer(text='https://www.youtube.com/watch?v=AbG6u86t4bA')
  await ctx.send(embed=embed)


# Bienvenida custom
@bot.event
async def on_member_join(member):
  channel = bot.get_channel(866394647357947945)

  offrol = discord.utils.get(member.guild.roles, id=876218996188393482)
  await member.add_roles(offrol)
  embed = discord.Embed(title='Un nuevo usuario se ha unido al servidor!', colour=0xFF000)
  embed.set_thumbnail(url=member.avatar_url)
  embed.add_field(name=f'Bienvenido/a {member.mention}, espero que disfrutes tu estadia!')
  embed.set_footer(text=f'Recuerda leer las reglas en:{bot.get_channel(866395029697069076).mention} \nLas instrucciones en: {bot.get_channel(866395683534667787).mention} \nY si tienes una duda, sientete libre de preguntar en {bot.get_channel(866395972964057088).mention}')

  await channel.send(embed=embed)


@bot.event
async def on_member_leave(member):
  channel = bot.get_channel(866394647357947945)

  embed = discord.Embed(title='Un usuario se ha largado del servidor', colour=0xFF000)
  embed.add_field(name=f'Adios {member.mention}!')

  await channel.send(embed=embed)


# Kick
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.User, *, reason):

  channel_auth = ["bans-y-expulsados"]

  if str("message.channel") in channel_auth:
    await user.kick(reason=reason)
    await ctx.send(f'{user.mention} ha sido kickeado del servidor por {ctx.message.author.mention}, porque: {reason}')
    await ctx.user.send(f'{ctx.message.author} te ha kickeado de {ctx.guild.name} por {reason}')
  else:
    await ctx.send(f'ERROR_HANDLER: No has enviado el comando en {bot.get_channel(869683491657379870).mention}')

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send(f'ERROR_HANDLER: Te ha faltado mencionar al usuario, o no tienes los permisos, o no has escrito en el canal {bot.get_channel(869683491657379870).mention}.')


# Ban
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.User, *, reason):

  channel_auth = ["bans-y-expulsados"]

  if str("message.channel") in channel_auth:
    await user.ban(reason=reason)
    await ctx.send(f'{user.mention} ha sido baneado del servidor por {ctx.message.author.mention}, porque: {reason}')
    await ctx.user.send(f'{ctx.message.author} te ha baneado de {ctx.guild.name} por {reason}')
  else:
    await ctx.send(f'ERROR_HANDLER: No has enviado el comando en {bot.get_channel(869683491657379870).mention}')

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send(f'ERROR_HANDLER: Te ha faltado mencionar al usuario, o no tienes los permisos, o no has escrito en el canal {bot.get_channel(869683491657379870).mention}.')


# Unban
@bot.command()
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()

  member_name, member_discriminator = member.split('#')
  for ban_entry in banned_users:
    user = ban_entry.user
  
  if (user.name, user.discriminator) == (member_name, member_discriminator):
    await ctx.guild.unban(user)
    await ctx.send(f"{user} ha sido desbaneado")

@bot.command(aliases=["reminder"])
async def alarm(ctx):
  pass
  print("")

# Obtener la cantidad de usuarios
@bot.command(aliases=["userlist"])
async def usuarios(ctx):
  id = bot.get_guild(866380305656971304)
  
  await ctx.send(f'Usuarios en el servidor: `{id.member_count}`')


# info del usuario
@bot.command()
async def user(ctx, member: discord.Member=None):
  if member is None:
    embed = discord.Embed(title=f'{ctx.message.author}', colour=0xFF000)
    embed.set_thumbnail(url=ctx.message.author.avatar_url)
    embed.add_field(name='ID de usuario:', value=f'`{ctx.message.author.id}`', inline=False)
    embed.add_field(name='Fecha de creacion:', value=f'`{ctx.author.created_at}`', inline=False)
    embed.add_field(name='Fecha de entrada:', value=f'`{ctx.author.joined_at}`', inline=False)
    embed.set_footer(text='')
    await ctx.send(embed=embed)

  else:
    embed = discord.Embed(title=f'{member.name}', colour=0xFF000)
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name='ID de usuario:', value=f'`{member.id}`', inline=False)
    embed.add_field(name='Fecha de creacion:', value=f'`{member.created_at}`', inline=False)
    embed.add_field(name='Fecha de entrada:', value=f'`{member.joined_at}`', inline=False)
    embed.set_footer(text='')
    await ctx.send(embed=embed)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# COÑO
@bot.command(aliases=["rage"])
async def angry(ctx, user: discord.User=None):
  COÑO0 = ["https://c.tenor.com/qP7Z51UusggAAAAC/girls-frontline.gif", "https://c.tenor.com/cc1EzfBVr4oAAAAC/yandere-tagged.gif", "https://c.tenor.com/L17xILFOlPoAAAAC/anime-yandere.gif", "https://media.tenor.com/images/0c38d94d83ed1c9a3f4d8ad8e7da2372/tenor.gif", "https://c.tenor.com/n6KTyBeNqD8AAAAd/yakuza-kazuma-kiryu.gif", "https://media.discordapp.net/attachments/523282321303142400/676254788022960148/ora-0001.gif", "https://media.tenor.com/images/feb7cffa98dd1abc4dd29d644189a1b1/tenor.gif", "https://lpix.org/3074883/popuko.gif", "https://thumbs.gfycat.com/DelectableTallAplomadofalcon-max-1mb.gif", "https://c.tenor.com/pLCNBQ-t3A4AAAAC/popute.gif", "https://c.tenor.com/7Xlq-Jo24k4AAAAC/anime-pop-team-epic.gif", "https://img.fireden.net/co/image/1490/89/1490891932968.gif", "https://c.tenor.com/e3ioAUfYVlQAAAAd/blade-runner2049-agent-k.gif"]

  COÑO1 = ["https://64.media.tumblr.com/20fb67283e3c062060dfe3fe40783f1f/tumblr_p5axaiHmWN1tx45yjo1_500.gif", "https://media1.tenor.com/images/577ba320b18d3fd10897b9384e0ba509/tenor.gif", "https://c.tenor.com/pLCNBQ-t3A4AAAAC/popute.gif", "https://lpix.org/3074883/popuko.gif", "https://media.discordapp.net/attachments/523282321303142400/676254788022960148/ora-0001.gif", "https://media.tenor.com/images/0c38d94d83ed1c9a3f4d8ad8e7da2372/tenor.gif", "https://c.tenor.com/qP7Z51UusggAAAAC/girls-frontline.gif", "https://thumbs.gfycat.com/ThirstyJaggedAzurevasesponge-max-1mb.gif"]

  if user is None:
    embed = discord.Embed(description=f'{ctx.message.author.mention} se ha enfadado', colour=0xFF000)
    embed.set_image(url=random.choice(COÑO0))
    await ctx.send(embed=embed)

  else:
    embed = discord.Embed(description=f'A {ctx.message.author.mention} le molesta {user.mention}', colour=0xFF000)
    embed.set_image(url=random.choice(COÑO1))
    await ctx.send(embed=embed)


# *cringes*
@bot.command()
async def cringe(ctx, user: discord.User=None):
  CRINGE0 = ["https://media1.tenor.com/images/5fc568729ede3645080391e871bce197/tenor.gif", "https://media.tenor.com/images/b269fa092b9713aff7ddf1f35959bf9e/tenor.gif", "https://media.tenor.com/images/6de2680734e525ee362b90bd6d21ba30/tenor.gif", "https://media1.tenor.com/images/302cbbdb7044cb0f2bfbe5b3853d81c9/tenor.gif", "https://media1.tenor.com/images/5c9ec0f439308a42ec0437f5422069b7/tenor.gif", "https://c.tenor.com/2M5qB16Bf2YAAAAd/dies-of-cringe.gif", "https://c.tenor.com/G8CAbEte1McAAAAC/lego-indiana.gif", "https://c.tenor.com/7crd2si0YkkAAAAC/hu-tao-genshin.gif", "https://c.tenor.com/ayqM4Ki15BYAAAAC/cringe-dies-from-cringe.gif", "https://c.tenor.com/8GFi8iQubQ0AAAAC/cringe-when-the-cringe-is-too-strong.gif", "https://c.tenor.com/A6iWuIvhjT4AAAAC/thanos-dies-of-cringe.gif", "https://c.tenor.com/4sfXGcQkA5sAAAAC/dies-from.gif"]

  CRINGE1 = ["https://cdn.discordapp.com/attachments/358651360985743381/676176653092651028/image0.png", "https://c.tenor.com/haHsODXehBgAAAAC/cringy-cringe.gif", "https://c.tenor.com/AawBjdNtT3AAAAAC/anime-cringe.gif", "https://c.tenor.com/iUKBLIh1eRkAAAAd/sonic-eggman.gif", "https://c.tenor.com/10DSZtcgaV0AAAAC/cringe-sakura-miko.gif", "https://c.tenor.com/PkPmu6bc0C8AAAAd/hotel-mario-bro-you-just-posted-cringe.gif", "https://c.tenor.com/ou5ppQPHm0IAAAAS/bro-just-posted-cringe-xd.gif", "https://c.tenor.com/XkmB0k_L4DkAAAAd/aether-genshin.gif", "https://c.tenor.com/4p1sI8zG3sMAAAAd/bro-you-just-posted-cringe-cringe.gif", "https://c.tenor.com/RXCsVWvqAMcAAAAd/make-you-doo.gif", "https://c.tenor.com/G_JnarmdHEYAAAAd/not-funny-dont-laugh.gif", "https://c.tenor.com/C-8axhfNOXQAAAAC/hatsune-miku-hatsume.gif"]

  if user is None:
    embed = discord.Embed(description=f'{ctx.message.author.mention} siente cringe', colour=0xFF000)
    embed.set_image(url=random.choice(CRINGE0))
    await ctx.send(embed=embed)

  else:
    embed = discord.Embed(description=f'{user.mention} da cringe', colour=0xFF000)
    embed.set_image(url=random.choice(CRINGE1))
    await ctx.send(embed=embed)

# Doktor, deactivate my pain inhibitors
@bot.command()
async def cry(ctx, user: discord.User=None):
  CRY = ["https://c.tenor.com/O900ohih6RkAAAAS/girls-frontline-m4.gif", "https://c.tenor.com/m7V6RjaMm-wAAAAC/rals-bruhgette.gif", "https://2.bp.blogspot.com/-Y9r7A16hq80/W76onqmnQ5I/AAAAAAAMMp0/cZ7Y0jVXlwkza80Imy7yHK403knfOaKfwCLcBGAs/s1600/AS0004490_00.gif", "https://danbooru.donmai.us/data/0ff2dbf73e676063279160886e0eeebf.gif", "https://c.tenor.com/EE1SLJuxBL4AAAAd/cry-about-it-cry.gif", "https://2.bp.blogspot.com/-222zO0PqC3A/Wr7Vd-MY4CI/AAAAAAAADXE/MZs49gfdTDI-9mJSO29u0SF4C2lSLv6uACLcBGAs/s1600/tumblr_p3ol40ySuD1x42ntdo1_500.gif"]

  if user is None:
    embed = discord.Embed(description=f'{ctx.message.author.mention} esta llorando', colour=0xFF000)
    embed.set_image(url=random.choice(CRY))
    await ctx.send(embed=embed)

  else:
    embed = discord.Embed(description=f'{user.mention} ha hecho llorar a {ctx.message.author.mention}', colour=0xFF000)
    embed.set_image(url=random.choice(CRY))
    await ctx.send(embed=embed)

# LET'S DANCE
@bot.command(aliases=["baila"])
async def dance(ctx, user: discord.User=None):
  DANCE0 = ["https://thumbs.gfycat.com/WeeLateKagu-max-1mb.gif", "https://media.tenor.com/images/0232df4ad0e9d6d702ec811345acb26a/tenor.gif", "https://media.tenor.com/images/6ad39d4da4990af07243edf823986126/tenor.gif", "https://i.makeagif.com/media/1-22-2017/8dFmQh.gif" "https://i.kym-cdn.com/photos/images/original/001/354/444/5c7.gif", "https://media.tenor.com/images/ff740631beb25d8e634ac1143377bfe0/tenor.gif", "https://media1.tenor.com/images/409f990affb4cb835c54f79a4fa120da/tenor.gif", "https://media0.giphy.com/media/l1J9GvFN6YEXYfqjm/giphy.gif", "https://64.media.tumblr.com/a434355d559a9d79927c0817b6426a6e/tumblr_inline_neeep6o4Re1sgtn17.gif", "https://66.media.tumblr.com/03e417a49f3d91af116c842c7a77f489/tumblr_inline_nx0x5dSAQt1sgtn17_250.gif", "https://cdn.discordapp.com/attachments/346522004763049984/667531931960737792/1579147185591.gif", "https://cdn.discordapp.com/attachments/638738711965859880/672106894482997269/Action_Dance_Light_Blue.gif", "https://media1.tenor.com/images/84525bdae52d87f3ae61110fe218e232/tenor.gif", "https://cdn.discordapp.com/attachments/439462022669926414/529472463122464799/048849d0f9758ba46ea7e725afdb8a54.gif", "https://cdn.discordapp.com/attachments/357001028769546252/674409862217859092/1568946153251.gif", "https://thumbs.gfycat.com/AntiquePreciousHumpbackwhale-max-1mb.gif", "https://66.media.tumblr.com/55393600484c90cbf1d8d6b97e76e872/tumblr_p5uvt4UdqB1x42ntdo1_400.gif", "https://cdn.discordapp.com/attachments/552282404635672576/676510785064927238/1581334115994.gif", "https://thumbs.gfycat.com/AggressiveGlumAuklet-max-1mb.gif", "https://cdn.discordapp.com/attachments/573522481445339140/744386770120081408/image0-8.gif", "https://media.tenor.com/images/b61108767ceaa389af65421802227c86/tenor.gif", "https://64.media.tumblr.com/7f583844a2c41fa4c860dcc207593a73/tumblr_inline_p5r6w6iNvk1r2vvqk_540.gif", "https://media.tenor.com/images/252a2dd8832ae93029d49be0c3d317d7/tenor.gif", "https://i.makeagif.com/media/3-28-2018/wgNt-w.gif", "https://thumbs.gfycat.com/LastingDigitalKookaburra-max-1mb.gif", "https://c.tenor.com/QQoT25duHp0AAAAd/yakuza-disco.gif", "https://i0.wp.com/68.media.tumblr.com/449923a0a9c07f5f14f8aba5f907b266/tumblr_nz8bsfA9Sl1v10ftpo1_500.gif", "https://pa1.narvii.com/7778/53bf1111341540a4fafd91cdc9774be2e101d7b3r1-800-450_hq.gif", "https://media.tenor.com/images/ff1c27839eea64fed86435a38a12d400/tenor.gif", "https://i0.wp.com/66.media.tumblr.com/1c8f98989692e60dbc56135df140dfd8/2e6df65c3c80521c-ae/s540x810/237ac6b330d3b95a7f8e028dc481bf48838f01af.gif", "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/1f76da86-e856-4175-8fa3-14b527189c7b/ddhto6c-f8b7dfae-d5df-47d9-91f0-70964c623e7a.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzFmNzZkYTg2LWU4NTYtNDE3NS04ZmEzLTE0YjUyNzE4OWM3YlwvZGRodG82Yy1mOGI3ZGZhZS1kNWRmLTQ3ZDktOTFmMC03MDk2NGM2MjNlN2EuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.xKgen5rPRLjRLBW-YBZ60xLurkWBmXUJZfa_PNh-uzc", "https://c.tenor.com/RqZJvoAM-acAAAAS/morgana-persona.gif", "https://c.tenor.com/_yPsablxEtUAAAAS/girls-frontline-ump9.gif", "https://c.tenor.com/D3Hx4ZFuDT0AAAAS/g11-girls-frontline.gif", "https://c.tenor.com/xCUx_u3SBo4AAAAd/girls-frontline-ump45.gif", "https://c.tenor.com/oAhg7b-RqHcAAAAC/m14.gif", "https://c.tenor.com/t_OAc5sk5eMAAAAC/hk416-mememe.gif", "https://c.tenor.com/hZyhTUvhZyYAAAAC/girlsfrontline.gif", "https://c.tenor.com/MpW1X2C-byAAAAAd/dark-souls3-dancing.gif", "https://c.tenor.com/IP2H6h1nii4AAAAC/dark-souls-dance.gif", "https://i.pinimg.com/originals/5f/67/47/5f6747a5c09b7c1786dc986cbcd0c97d.gif"]

  DANCE1 = ["https://thumbs.gfycat.com/AggressiveGlumAuklet-max-1mb.gif", "https://i.makeagif.com/media/6-16-2015/SoaIPU.gif", "https://media1.tenor.com/images/95612b6cbbf434b619957e31c362aa71/tenor.gif", "https://i2.wp.com/novocom.top/image/aS5pbci5jbWd1ci5jb20=/UKwVMzx.gif", "https://c.tenor.com/bqUfCBZS1c4AAAAC/gfl-girls-frontline.gif", "https://c.tenor.com/_Ty5Q5UrjdMAAAAC/dark-souls-dance.gif", "https://c.tenor.com/UwvoJVTOdXcAAAAC/wheel-skeleton-pruld.gif"]

  if user is None:
    embed = discord.Embed(description=f'{ctx.message.author.mention} baila', colour=0xFF000)
    embed.set_image(url=random.choice(DANCE0))
    await ctx.send(embed=embed)

  else:
    embed = discord.Embed(description=f'{ctx.message.author.mention} baila junto a {user.mention}', colour=0xFF000)
    embed.set_image(url=random.choice(DANCE1))
    await ctx.send(embed=embed)

# demoted
@bot.command()
async def demoted(ctx, user: discord.User=None):
  DEMOTED = ["https://c.tenor.com/fJG4U7gUuaMAAAAC/saguskycord-darksouls.gif", "https://c.tenor.com/rro-1Ntj5IEAAAAC/okbr-demoted.gif", "https://c.tenor.com/mY9-8hutejAAAAAd/dark-souls-demoted.gif", "https://c.tenor.com/iI0jGfFuoREAAAAC/okbr-mohammad-okbr.gif"]

  if user is None:
    embed = discord.Embed(description='Te han quitado un rol', colour=0xFF000)
    embed.set_image(url=random.choice(DEMOTED))
    await ctx.send(embed=embed)

  else:
    embed = discord.Embed(description=f'Le han reducido de cargo a {user.mention}', colour=0xFF000)
    embed.set_image(url=random.choice(DEMOTED))
    await ctx.send(embed=embed)  

# AUGH
@bot.command(aliases=["die"])
async def dies(ctx, user: discord.User=None):
  DIE = ["https://i.makeagif.com/media/7-24-2018/7cwn65.gif", "https://risibank.fr/cache/stickers/d1562/156290-full.gif", "https://64.media.tumblr.com/92119a55951346c8d90ba75c158f69db/tumblr_nwggh5anE11riwt83o6_540.gif", "https://i.imgur.com/lyqWHjg.gif", "https://thumbs.gfycat.com/FineEmbellishedHarlequinbug-size_restricted.gif", "https://media1.tenor.com/images/d99bfb4d11845934e33304b1b00b350a/tenor.gif", "https://c.tenor.com/E96hOC51vAgAAAAC/girls-frontline-coffin-dance.gif", "https://c.tenor.com/C-m4WeNjxu4AAAAC/blade-runner-snow.gif", "https://c.tenor.com/YPHsyL-B2UAAAAAd/dies-of-death.gif", "https://c.tenor.com/241bDDSBddUAAAAd/dark-souls.gif","https://thumbs.gfycat.com/AggressiveGlumAuklet-max-1mb.gif"]

  if user is None:
    embed = discord.Embed(description=f' {ctx.message.author.mention} ha finjido su muerte.', colour=0xFF000)
    embed.set_image(url=random.choice(DIE))
    await ctx.send(embed=embed)

  else:
    embed = discord.Embed(description=f'{ctx.message.author.mention} y {user.mention} han muerto', colour=0xFF000)
    embed.set_image(url=random.choice(DIE))
    await ctx.send(embed=embed)


# @everyone
@bot.command()
async def everyone(ctx, user: discord.User=None):
  TAG = ["https://emoji.gg/assets/emoji/angeryping.gif", "https://thumbs.gfycat.com/FocusedFreshAlaskanhusky-size_restricted.gif", "https://media1.tenor.com/images/cd3b97b9e4f304434e90c1769bf8497b/tenor.gif", "https://media1.tenor.com/images/8321feec94d16f15bd2c800118f376fd/tenor.gif", "https://media.discordapp.net/attachments/488834046177181717/636002118876135434/image0-14.gif", "https://cdn.discordapp.com/attachments/369906418926747658/512288503652941824/ooooof.gif", "https://media.discordapp.net/attachments/292848355187359744/658580491703812097/BJtjMwVs-.gif", "https://i.giphy.com/media/M9Om8L6UYigE6E7Ak8/giphy.webp", "https://64.media.tumblr.com/356adfda47dcdaf4c2db7930f43ce7f7/tumblr_pjdtv8ZGCd1wa0ak9o1_400.gif"]

  if user is None:
    embed = discord.Embed(colour=0xFF000)
    embed.set_image(url=random.choice(TAG))
    await ctx.send(embed=embed)

  else:
    embed = discord.Embed(description=f'Deja de usar @everyone {user.mention}. Es molesto', colour=0xFF000)
    embed.set_image(url=random.choice(TAG))
    await ctx.send(embed=embed)


# YEY
@bot.command(aliases=["yey"])
async def happy(ctx, user: discord.User=None):
  HAPPY = ["https://c.tenor.com/Vz1VRXL58NYAAAAC/dance-hk416.gif", "https://c.tenor.com/_yPsablxEtUAAAAS/girls-frontline-ump9.gif", "https://c.tenor.com/4hxi0CQKangAAAAC/affea-girls-frontline.gif", "https://c.tenor.com/_yPsablxEtUAAAAd/girls-frontline-ump9.gif", "https://cdn.discordapp.com/attachments/473619129308282904/871896147306881054/676292130028912651.gif", "https://media1.tenor.com/images/a737187638ddbf82979ed2b39ce55ac3/tenor.gif", "https://media.tenor.com/images/2801410c4dff2f169ebedddacb55dc70/tenor.gif", "https://31.media.tumblr.com/tumblr_ltcb2gIvn11r1rrxzo1_500.gif", "https://img02.fireden.net/cm/image/1537/60/1537602229606.gif"]

  if user is None:
    embed = discord.Embed(description=f'{ctx.message.author.mention} se siente feliz', colour=0xFF000)
    embed.set_image(url=random.choice(HAPPY))
    await ctx.send(embed=embed)

  else:
    embed = discord.Embed(description=f'{user.mention} ha hecho feliz a {ctx.message.author.mention}', colour=0xFF000)
    embed.set_image(url=random.choice(HAPPY))
    await ctx.send(embed=embed)


# *hugs*
@bot.command(aliases=["abraza"])
async def hug(ctx, user: discord.User=None):
  HUG = ["https://64.media.tumblr.com/0a287f7f0a521bf736dc95df89c48321/tumblr_pt2kua8ypl1r7ib92o1_540.gif", "https://thumbs.gfycat.com/GiganticFrighteningAlpineroadguidetigerbeetle-max-1mb.gif", "https://c.tenor.com/g_-S6op8aCwAAAAC/girls-frontline-sopmod.gif"]

  if user is None:
    embed = discord.Embed(description=f'{ctx.message.author.mention} toma un abrazo de mi parte. No te preocupes, no tengo ningun microfono oculto jaja', colour=0xFF000)
    embed.set_image(url=random.choice(HUG))
    await ctx.send(embed=embed)

  else:
    embed = discord.Embed(description=f'{ctx.message.author.mention} abraza a {user.mention}!', colour=0xFF000)
    embed.set_image(url=random.choice(HUG))
    await ctx.send(embed=embed)


# Goodbye, Captain Price
@bot.command(aliases=["mata"])
async def kill(ctx, user: discord.User=None):
  KILL = ["https://thumbs.gfycat.com/WavyFormalGalapagossealion-max-1mb.gif", "https://c.tenor.com/ciwCvUr9h7MAAAAC/soldier-anime.gif", "https://c.tenor.com/BYS85XWJ8gQAAAAd/joker-joker-laugh.gif", "https://media.tenor.com/images/23619505479c9dade9a3b474f9b93d4d/tenor.gif", "https://64.media.tumblr.com/16d83fb33d17b862ceee7dc77cb43320/tumblr_inline_pb3ijkKSTG1rcsyym_540.gif"]

  if user is None:
    embed = discord.Embed(description=f'{ctx.message.author.mention} ha matado a alguien', colour=0xFF000)
    embed.set_image(url=random.choice(KILL))
    await ctx.send(embed=embed)

  else:
    embed = discord.Embed(description=f'{ctx.message.author.mention} asesino a {user.mention}', colour=0xFF000)
    embed.set_image(url=random.choice(KILL))
    await ctx.send(embed=embed)


# Byeee
@bot.command(aliases=["leave"])
async def bye(ctx, user: discord.User=None):
  BYE = ["https://c.tenor.com/O_oxKYFTaqwAAAAC/good-bye-chat-good-bye-yakuza.gif", "https://c.tenor.com/etRsyIAAJpAAAAAC/goodbye-chat-chat.gif", "https://c.tenor.com/tcjp-PpW4boAAAAS/wachi-wachi-wa-flying.gif", "https://media1.tenor.com/images/eb7109efa7cf45439dd5e4706e2c13e0/tenor.gif", "https://media.tenor.com/images/c0fb4d572bc92fffb4510839f05b9065/tenor.gif", "https://media3.giphy.com/media/Ru9sjtZ09XOEg/giphy.gif", "https://c.tenor.com/Kz-H0N2nFMsAAAAd/what-leaving.gif"]

  if user is None:
    embed = discord.Embed(description=f'{ctx.message.author.mention} se va', colour=0xFF000)
    embed.set_image(url=random.choice(BYE))
    await ctx.send(embed=embed)

  else:
    embed = discord.Embed(description=f'{ctx.message.author.mention} se alejo de {user.mention}', colour=0xFF000)
    embed.set_image(url=random.choice(BYE))
    await ctx.send(embed=embed)


# What the fuck is wrong with you
@bot.command(aliases=["horny"])
async def lewd(ctx, user: discord.User=None):
  LEWD = ["https://c.tenor.com/brn_miOxJPgAAAAC/ump-ump9.gif", "https://c.tenor.com/6RVmRMNOPH8AAAAC/ump45.gif", "https://c.tenor.com/MRVjc5l7HvoAAAAC/seseren-girls-frontline.gif", "https://c.tenor.com/uj7mC9o7yLQAAAAC/girls-frontline-sex.gif", "https://pa1.narvii.com/7532/2bb894ee6e4380c51c71564e5c37194f603c76aar1-514-506_hq.gif", "https://c.tenor.com/ouUxqKbKGNMAAAAC/lewd-anime.gif", "https://c.tenor.com/njdAbTl1SfcAAAAC/lewd-anime.gif", "https://c.tenor.com/dlyirnM2OHUAAAAC/azur-lane-lewd.gif", "https://cdn.discordapp.com/attachments/357001028769546252/674113329295261726/651977419380752429.gif", "https://cdn.discordapp.com/emojis/861677883163148308.gif?v=1", "https://c.tenor.com/QbwrYV8s1bcAAAAS/horny-die.gif"]

  if user is None:
    embed = discord.Embed(description=f'No hace falta que lo describa, ¿verdad?', colour=0xFF000)
    embed.set_image(url=random.choice(LEWD))
    await ctx.send(embed=embed)

  else:
    embed = discord.Embed(description=f'A {user.mention} y {ctx.message.author.mention} no conocen el significado de "decencia"', colour=0xFF000)
    embed.set_image(url=random.choice(LEWD))
    await ctx.send(embed=embed)


# niceee
@bot.command(aliases=["nice", "approve"])
async def like(ctx, user: discord.User=None):
  LIKE = ["https://c.tenor.com/RyWvmjS_XyUAAAAC/kazuma-kiryu.gif", "https://c.tenor.com/4fkBoyjubOIAAAAd/doom-slayer-doom-marine.gif", "https://c.tenor.com/lG25A_WFbJ8AAAAC/seseren-head-bang.gif", "https://media.discordapp.net/attachments/454721287290355716/837653220011802684/received_780844935910410.gif", "https://cdn.discordapp.com/attachments/473657277241622528/703159790305804348/snakethumbsup.gif", "https://c.tenor.com/hueVHCR4PxEAAAAC/doom-slayer-doomguy.gif", "https://pa1.narvii.com/6955/9fafea47833e268db4a3c66fa8dba71b788822c1r1-356-294_hq.gif"]

  if user is None:
    embed = discord.Embed(description=f'{ctx.message.author.mention} aprueba esto', colour=0xFF000)
    embed.set_image(url=random.choice(LIKE))
    await ctx.send(embed=embed)

  else:
    embed = discord.Embed(description=f'{ctx.message.author.mention} concuerda con {user.mention}', colour=0xFF000)
    embed.set_image(url=random.choice(LIKE))
    await ctx.send(embed=embed)


# What is love?
@bot.command()
async def love(ctx, user: discord.User=None):
  LOVE = ["https://c.tenor.com/-z2RGFfsedkAAAAC/girls-frontline-m4sopmod-ii.gif", "https://c.tenor.com/nZSJS7M4UXMAAAAC/anime-girlsfrontline.gif", "https://i.pinimg.com/originals/7c/03/21/7c0321677251066b8ee4e7b429b7bbf9.gif", "https://i.pinimg.com/originals/e4/bd/b8/e4bdb81317f7d2f1feb233c4d0164737.gif", "https://c.tenor.com/g_-S6op8aCwAAAAC/girls-frontline-sopmod.gif", "https://64.media.tumblr.com/15597240b5ad790e7fd026921a2126d3/tumblr_owbevnFrnI1vltj92o3_500.gif", "https://media1.tenor.com/images/c862f4624b778240908dadd0b90d1647/tenor.gif"]

  if user is None:
    embed = discord.Embed(description=f'A {ctx.message.author.mention} le hace falta amor y aprecio')
    embed.set_image(url=random.choice(LOVE))
    await ctx.send(embed=embed)

  else:
    embed = discord.Embed(description=f'{ctx.message.author.mention} te quiere mucho, {user.mention}!', colour=0xFF000)
    embed.set_image(url=random.choice(LOVE))
    await ctx.send(embed=embed)


# Uhum
@bot.command()
async def nod(ctx, user: discord.User=None):
  NOD = ["https://media1.tenor.com/images/26ae595ebedda776119b7490a5f5d29a/tenor.gif", "https://c.tenor.com/lG25A_WFbJ8AAAAC/seseren-head-bang.gif"]

  if user is None:
    embed = discord.Embed(description=f'{ctx.message.author.mention} concuerda con esto', colour=0xFF000)
    embed.set_image(url=random.choice(NOD))
    await ctx.send(embed=embed)
  else:
    embed = discord.Embed(description=f'{ctx.message.author.mention} aprueba lo que dijo {user.mention}', colour=0xFF000)
    embed.set_image(url=random.choice(NOD))
    await ctx.send(embed=embed)


@bot.command()
async def pain(ctx, user: discord.User=None):
  pass
  PAIN = ["https://c.tenor.com/e3ioAUfYVlQAAAAd/blade-runner2049-agent-k.gif"]

  if user is None:
    embed = discord.Embed(description=f'{ctx.message.author.mention} siente un dolor inconmesurable', colour=0xFF000)
    embed.set_image(url=random.choice(PAIN))
    await ctx.send(embed=embed)
    
  else:
    embed = discord.Embed(description=f'{user.mention}, le estas causando dolor a {ctx.message.author.mention}', colour=0xFF000)
    embed.set_image(url=random.choice(PAIN))
    await ctx.send(embed=embed)

# *pat pat*
@bot.command()
async def pat(ctx, user: discord.User=None):
  PAT = ["https://c.tenor.com/Df9dzdzLKMMAAAAd/girls-frontline-gfl.gif", "https://c.tenor.com/hyZ_Xj9gWkYAAAAd/m14-girls-frontline.gif", "https://c.tenor.com/aJUSgcD3IXwAAAAS/girls-frontline-m14.gif", "https://c.tenor.com/UlzbZhNBWHkAAAAd/pat-pat.gif", "https://i.pinimg.com/originals/29/a6/5c/29a65c7d6e453679e60e26134d3e0e10.gif", "https://pa1.narvii.com/6767/06df43a44b6cbef9d23808e02f85dc9845340e53_00.gif", "https://2.bp.blogspot.com/-222zO0PqC3A/Wr7Vd-MY4CI/AAAAAAAADXE/MZs49gfdTDI-9mJSO29u0SF4C2lSLv6uACLcBGAs/s1600/tumblr_p3ol40ySuD1x42ntdo1_500.gif", "https://twitter.com/i/status/1303407780561383424", "https://c.tenor.com/pmOaHKmXbpYAAAAi/beanies-astolfo-petpet-astolfo.gif"]

  if user is None:
    embed = discord.Embed(description=f'{ctx.message.author.mention} te hace falta afecto, no es asi?', colour=0xFF000)
    embed.set_image(url=random.choice(PAT))
    await ctx.send(embed=embed)

  else:
    embed = discord.Embed(description=f'pat pat {user.mention}', colour=0xFF000)
    embed.set_image(url=random.choice(PAT))
    await ctx.send(embed=embed)


# poggers
@bot.command(aliases=["poggers"])
async def pog(ctx):
  POG = ["https://c.tenor.com/O57kNANydMIAAAAS/pogchamp-pog.gif", "https://c.tenor.com/jL0Sbz7Jw1cAAAAS/pog-fish.gif", "https://c.tenor.com/-0s0ZOCr_3kAAAAC/pogchamp-loop.gif", "https://c.tenor.com/AB482er5iEYAAAAd/axolotl-among-us.gif", "https://c.tenor.com/12CDAijGO1YAAAAd/pog-poggers.gif", "https://c.tenor.com/pdFBIuEzZIUAAAAC/pog-poggers.gif", "https://cdn.discordapp.com/attachments/808729592638078976/864704195767697449/maxresdefault.png", "https://cdn.discordapp.com/attachments/808729592638078976/851211038145118238/IMG_20210606_182807.JPG", "https://cdn.discordapp.com/attachments/808729592638078976/808729728998572082/ab4.jpg", "https://cdn.discordapp.com/attachments/808729592638078976/808729719490871316/images.jpg", "https://cdn.discordapp.com/attachments/808729592638078976/808729718639689748/w5e0x0stooa51.png", "https://cdn.discordapp.com/attachments/808729592638078976/808729718424600636/8be.jpg", "https://cdn.discordapp.com/attachments/808729592638078976/808729717468954624/vkt08pw2jw151.png", "https://cdn.discordapp.com/attachments/808729592638078976/808729638527434772/eeb.jpg", "https://cdn.discordapp.com/attachments/808729592638078976/808729638037225534/rqsfpm9l3u241.png", "https://cdn.discordapp.com/attachments/808729592638078976/875181833992695808/a1ylobfpsmi51.png", "https://cdn.discordapp.com/attachments/808729592638078976/875181885821706270/1f272465f1c318bfe175efb70bd9a04bfd67546c.png", "https://cdn.discordapp.com/attachments/808729592638078976/875181921003536434/1418464_takoto_pog-quog-quagsire.png", "https://loginportal.funnyjunk.com/comments/I+can+now+call+2+additional+witnesses+from+my+deckcomment+_acaf5810994626284a383b330fe71e59.png", "https://c.tenor.com/zQVlFfU6VoUAAAAC/ump45-dance.gif"]

  embed = discord.Embed(description='poggers', colour=0xFF000)
  embed.set_image(url=random.choice(POG))
  await ctx.send(embed=embed)


# unpog
@bot.command()
async def pognt(ctx):
  POGNT = ["https://c.tenor.com/KM7S189SwtwAAAAd/pognt.gif", "https://c.tenor.com/r4o5Qk4-7ZUAAAAS/pognt-soldier-tf2.gif", "https://c.tenor.com/gLgXKUTKNU0AAAAd/jetstream-sam-pognt.gif"]

  embed = discord.Embed(description="pogn't", colour=0xFF000)
  embed.set_image(url=random.choice(POGNT))
  await ctx.send(embed=embed)


# Nanomachines son
@bot.command(aliases=["golpea"])
async def punch(ctx, user: discord.User=None):
  PUNCH0 = ["https://64.media.tumblr.com/c5310d7e13daa32b3a31d38859b81488/tumblr_p3yax7kmbQ1wga4wmo2_500.gif", "https://64.media.tumblr.com/b3d761c1241f3f0e83d799fd336eaba3/tumblr_p3yax7kmbQ1wga4wmo1_500.gif", "https://media.tenor.com/images/cf5bd9650df69b8772fb1784ab59265d/tenor.gif", "https://media1.tenor.com/images/2a80b9428fc3210afb8edddc4f0084cf/tenor.gif", "https://media1.tenor.com/images/bc79a051d81a50fa3a577f6b08a9eb80/tenor.gif", "https://media1.tenor.com/images/fdffda109b08ab5395afdcffd5ab581f/tenor.gif", "https://giffiles.alphacoders.com/358/35893.gif", "https://c.tenor.com/HgAlhB5ByKkAAAAS/g11-hk416.gif", "https://c.tenor.com/yKBFgK4rmjAAAAAC/hk416-punch.gif", "https://c.tenor.com/UEF4khH2Ye0AAAAC/yakuza-kiryu.gif"]

  PUNCH1 = ["https://cdn.discordapp.com/attachments/638738711965859880/874395026677960704/1522264710_1515356060_p0L0xe.gif", "https://c.tenor.com/PQfA6Yj08IYAAAAd/tyler1-tyler1autism.gif"]

  if user is None:
    embed = discord.Embed(description=f'{ctx.message.author.mention} esta golpeando al aire', colour=0xFF000)
    embed.set_image(url=random.choice(PUNCH1))
    await ctx.send(embed=embed)

  else:
    embed = discord.Embed(description=f'{ctx.message.author.mention} ha golpeado a {user.mention}', colour=0xFF000)
    embed.set_image(url=random.choice(PUNCH0))
    await ctx.send(embed=embed)


# NIGERUNDAYO SMOKIE
@bot.command(aliases=["corre"])
async def run(ctx, user: discord.User=None):
  RUN0 = ["https://media1.tenor.com/images/ecccfdcdc5d25b957275467066ad5752/tenor.gif", "https://i.4pcdn.org/s4s/1537055730901.gif"]

  RUN1 = ["https://i.imgur.com/8CwQD2G.gif", "https://i.pinimg.com/originals/5b/b8/7e/5bb87e846afc822a35dbad5b6e8f2118.gif"]

  if user is None:
    embed = discord.Embed(description=f'{ctx.message.author.mention} se ha pirado', colour=0xFF000)
    embed.set_image(url=random.choice(RUN0))
    await ctx.send(embed=embed)

  else:
    embed = discord.Embed(description=f'{ctx.message.author.mention} huye de {user.mention}', colour=0xFF000)
    embed.set_image(url=random.choice(RUN1))
    await ctx.send(embed=embed)


# :(
@bot.command()
async def sad(ctx, user: discord.User=None):
  SAD = ["https://cdn.discordapp.com/attachments/473657277241622528/870803825898958918/1613205424617.gif", "https://c.tenor.com/5EgBYns_4L4AAAAd/lizard-dancing-lizard.gif", "https://media.tenor.com/images/d5176f6f3e632a409ec93769b77f8ddf/tenor.gif", "https://c.tenor.com/ft1nNFOW6pQAAAAd/the-sound-of-pogger-the-sound-of-poggers.gif"]

  if user is None:
    embed = discord.Embed(description=f'{ctx.message.author.mention} se siente triste', colour=0xFF000)
    embed.set_image(url=random.choice(SAD))
    await ctx.send(embed=embed)

  else:
    embed = discord.Embed(description=f'{user.mention} has hecho que {ctx.message.author.mention} se sienta mal, deberias de reflexionar sobre tus acciones.')
    embed.set_image(url=random.choice(SAD))
    await ctx.send(embed=embed)

# AAAAAAAAAAAAAAAAAA
@bot.command()
async def scream(ctx, user: discord.User=None):

  SCREAM = ["https://thumbs.gfycat.com/CostlyEntireAustraliansilkyterrier-max-1mb.gif", "https://thumbs.gfycat.com/LeafyLargeFireant-max-1mb.gif", "https://media1.tenor.com/images/f4504b29fdf29fac1e2445c5e073aa4f/tenor.gif", "https://c.tenor.com/7AX9wsT8lIEAAAAC/doktor-turn.gif"]

  if user is None:
    embed = discord.Embed(description=f'¡{ctx.message.author.mention} ESTA GRITANDO!', colour=0xFF000)
    embed.set_image(url=random.choice(SCREAM))
    await ctx.send(embed=embed)
    
  else:
    embed = discord.Embed(description=f'{ctx.message.author.mention} le esta gritando a {user.menion}', colour=0xFF000)
    embed.set_image(url=random.choice(SCREAM))
    await ctx.send(embed=embed)

# *shrugs*
@bot.command()
async def shrug(ctx):
  SHRUG = ["https://media1.tenor.com/images/6344aa952d017d0a1fcdcb1892ccb17b/tenor.gif", "https://c.tenor.com/MnD_Mbr7JWsAAAAC/fgo-astolfo.gif"]

  embed = discord.Embed(colour=0xFF000)
  embed.set_image(url=random.choice(SHRUG))
  await ctx.send(embed=embed)


# Twitch user
@bot.command()
async def simp(ctx, user: discord.User=None):
  SIMP = ["https://media1.tenor.com/images/7a1b5d9748f3dd6ac410eacd2d82474c/tenor.gif?itemid=19441660", "https://media1.tenor.com/images/4a89e4c19b9ecf24bef8a281b34c49ea/tenor.gif?itemid=20975015", "https://media1.tenor.com/images/a7144d0f9fd09e97ddb43f955c8f2d58/tenor.gif?itemid=20277662", "https://media1.tenor.com/images/8a2edb8f539d6a93b2a4c1557e9bd399/tenor.gif?itemid=17237416", "https://media1.tenor.com/images/f2902e32b15b540ed68ddd5f94365dee/tenor.gif?itemid=16717852", "https://media.tenor.com/images/5931602a07e495ba7bbfbe988d834832/tenor.gif", "https://media.tenor.com/images/85fd4b200758cfc78a7b637def81f500/tenor.gif", "https://thumbs.gfycat.com/FrightenedShallowHoverfly-max-1mb.gif"]

  if user is None:
    embed = discord.Embed(description=f'{ctx.message.author} ha visto a alguien caer bajo.', colour=0xFF000)
    embed.set_image(url=random.choice(SIMP))
    await ctx.send(embed=embed)

  else:
    embed = discord.Embed(description=f'{user.mention} es un asqueroso simp', colour=0xFF000)
    embed.set_image(url=random.choice(SIMP))
    await ctx.send(embed=embed)


# Tipico de las telenovelas
@bot.command()
async def slap(ctx, user: discord.User):
  SLAP = ["https://i.imgur.com/W47m4e7.gif", "https://pa1.narvii.com/6767/b18ba6d76afb77f6186b8ee7feb4fcf4abf45182_hq.gif"]

  embed = discord.Embed(description=f'{ctx.message.author.mention} le dio una cachetada a {user.mention}', colour=0xFF000)
  embed.set_image(url=random.choice(SLAP))
  await ctx.send(embed=embed)


# We do a little sleeping
@bot.command()
async def sleep(ctx):
  SLEEP = ["https://c.tenor.com/VWr1ZRMNblMAAAAd/g11-sleeping.gif", "https://c.tenor.com/m7V6RjaMm-wAAAAC/rals-bruhgette.gif", "https://c.tenor.com/YAZwuJXWFMoAAAAd/fumo-reimu-fumo.gif", "https://3.bp.blogspot.com/-9rina1vVOHs/WIoEqqLxmNI/AAAAAAANRDk/tSyEIwKZosQzssQThbISaBkFaOPN_gkzACLcB/s1600/AS002279_06.gif"]

  embed = discord.Embed(description=f'{ctx.message.author.mention} se va a dormir', colour=0xFF000)
  embed.set_image(url=random.choice(SLEEP))
  await ctx.send(embed=embed)


# To die as much as one pleases
@bot.command()
async def suicide(ctx):
  SUSSYDIE = ["https://media.tenor.com/images/c7495a89f62a3b130dd56f03390d9718/tenor.gif", "https://c.tenor.com/YTWHmcGTfu8AAAAC/persona-persona3.gif", "https://c.tenor.com/FDF8HXTcH00AAAAd/mortal-kombay.gif", "https://c.tenor.com/kdNA2sR6X0wAAAAd/suicide.gif", "https://c.tenor.com/JLI2HCaXs94AAAAd/shin-hokuto-no-ken.gifv", "https://c.tenor.com/3WRKCYqnYEsAAAAC/kermit-suicide.gif", "https://c.tenor.com/kdNA2sR6X0wAAAAd/suicide.gif", "https://c.tenor.com/sc_5mF38qNIAAAAd/suicide-bullet.gif", "https://c.tenor.com/3CA1O15WnSsAAAAC/suicide-me.gif", "https://c.tenor.com/MlVnsXkBl3EAAAAd/keanu-reeves-the-matrix.gif", "https://c.tenor.com/bd2R1k8zp20AAAAS/filthy-frank.gif", "https://c.tenor.com/QZofDok44NEAAAAC/emo-suicide.gif", "https://thumbs.gfycat.com/ConventionalChiefIrishsetter-max-1mb.gif", "https://c.tenor.com/241bDDSBddUAAAAd/dark-souls.gif"]

  embed = discord.Embed(description=f'{ctx.message.author.mention} ha cometido suicidio', colour=0xFF000)
  embed.set_image(url=random.choice(SUSSYDIE))
  await ctx.send(embed=embed)


# :thinking:
@bot.command(aliases=["thonk"])
async def think(ctx):
  THONK = ["https://media.giphy.com/media/CaiVJuZGvR8HK/giphy.gif", "https://i.imgur.com/mhoXGgs.gif", "https://media0.giphy.com/media/2H67VmB5UEBmU/giphy.gif", "https://media.tenor.com/images/eec1d9b948dc0e226b49ce16df6cdfd6/tenor.gif", "https://media1.giphy.com/media/IQ47VvDzlzx9S/giphy.gif", "https://thumbs.gfycat.com/LightheartedZigzagAtlasmoth-small.gif", "https://c.tenor.com/OIfGRTnGSfAAAAAd/girls-frontline-ak12.gif", "https://media1.tenor.com/images/9be7127ce0affaa596768cf05ce50efa/tenor.gif", "https://i.imgur.com/iIvwJRX.gif", "https://4.bp.blogspot.com/-ugf11u-jgkM/W3JR-HVpLVI/AAAAAAALn30/2-AMAQlAlLUf6LYc3t0WiOoRl8hQ7oOGgCLcBGAs/s1600/AS0004265_00.gif"]

  embed = discord.Embed(description=f'{ctx.message.author.mention} esta pensando', colour=0xFF000)
  embed.set_image(url=random.choice(THONK))
  await ctx.send(embed=embed)


# THOT PATROL
@bot.command()
async def thot(ctx, user: discord.User):
  THOT = ["https://media1.tenor.com/images/f6cbabb065b338800b680950b5241440/tenor.gif?itemid=14609290", "https://media1.tenor.com/images/54b8a204bf50ab045933ac727b411a50/tenor.gif?itemid=11326734", "https://i.makeagif.com/media/5-24-2018/OCRl2G.gif", "https://thumbs.gfycat.com/GlamorousSereneAtlasmoth-max-1mb.gif", "https://i.kym-cdn.com/photos/images/original/001/334/916/ff4.gif", "https://thumbs.gfycat.com/GlisteningIllustriousHuemul-size_restricted.gif", "https://c.tenor.com/lpJXvcDAgFIAAAAj/throw-rock-rocks.gif"]

  embed = discord.Embed(description=f'{user.mention} es una zorra', colour=0xFF000)
  embed.set_image(url=random.choice(THOT))
  await ctx.send(embed=embed)


# We did a little
@bot.command(aliases=["trolling"])
async def troll(ctx):
  TROLL = ["https://c.tenor.com/toBNvExLXDcAAAAC/okbr-mohammad-okbr.gif"]

  embed = discord.Embed(description=f'WE did a little bit of trolling', colour=0xFF000)
  embed.set_image(url=random.choice(TROLL))
  await ctx.send(embed=embed)


# ???
@bot.command(aliases=["que", "confused"])
async def what(ctx):
  WHAT = ["https://c.tenor.com/9RYl1Lqm6GkAAAAd/ak12-girls-frontline.gif", "https://c.tenor.com/OIfGRTnGSfAAAAAd/girls-frontline-ak12.gif", "https://c.tenor.com/fLp73EKjWhkAAAAC/m4-girls-frontline.gif", "https://c.tenor.com/xOQvvHU9GrYAAAAC/seseren-stare.gif", "https://thumbs.gfycat.com/LightheartedZigzagAtlasmoth-small.gif", "https://media.discordapp.net/attachments/358651360985743381/670336321553825822/image0-3.gif", "https://thumbs.gfycat.com/AchingHeftyKodiakbear-size_restricted.gif", "https://media1.tenor.com/images/9be7127ce0affaa596768cf05ce50efa/tenor.gif", "https://embers-host.nyc3.digitaloceanspaces.com/uploads/media/5a6dfb31-4b82-49fa-b116-e6133e61fffa.gif", "https://media1.tenor.com/images/f6db4e72bc66658bd641563bd662df7f/tenor.gif", "https://media1.tenor.com/images/2050d3b431fe883c83617983a4688566/tenor.gif", "https://c.tenor.com/dQs_FYOU8zYAAAAC/sus-suspect.gif", "https://c.tenor.com/2_obpMXU_gYAAAAd/joe.gif"]

  embed = discord.Embed(description=f'... Que?', colour=0xFF000)
  embed.set_image(url=random.choice(WHAT))
  await ctx.send(embed=embed)


# COMANDOS "SECRETOS"   ///   COMANDOS "SECRETOS"   ///
# COMANDOS "SECRETOS"   ///   COMANDOS "SECRETOS"   ///


# FUMO IS LIFE
@bot.command()
async def fumo(ctx):
  FUMO = ["https://c.tenor.com/4c8FtjQlmCAAAAAC/cirno-pat-cirno.gif", "https://c.tenor.com/S6hEQHbMuysAAAAS/me-resisting-the-urge-resisting-the-urge.gif", "https://c.tenor.com/s7WoM4BDR5IAAAAS/fumo-touhou-touhou.gif", "https://c.tenor.com/-IQaQNoibIUAAAAS/small-hvh-small.gif", "https://cdn.discordapp.com/attachments/862856502342451210/864704473783074887/znk4j6y0yvr11.png", "https://cdn.discordapp.com/attachments/862856502342451210/867070454975823872/20210717_100319.png", "https://cdn.discordapp.com/attachments/382626005719973888/718871406120534077/EZ0xw26U4AALvzu.png", "https://cdn.discordapp.com/attachments/382626005719973888/739953868137431152/image0_6.png", "https://cdn.discordapp.com/attachments/382626005719973888/747510924717326497/image0-50.jpg", "https://cdn.discordapp.com/attachments/382626005719973888/774729685258076210/20201107_151843.jpg", "https://cdn.discordapp.com/attachments/382626005719973888/801105689694568458/20210119_100503.jpg", "https://cdn.discordapp.com/attachments/382626005719973888/830574202330284032/20210410_131954.jpg", "https://cdn.discordapp.com/attachments/382626005719973888/826717633231454208/20210331_024645.jpg", "https://cdn.discordapp.com/attachments/382626005719973888/838950534777405440/20210503_202921.jpg", "https://cdn.discordapp.com/attachments/382626005719973888/841491209322496000/20210509_175841.jpg", "https://cdn.discordapp.com/attachments/382626005719973888/856568038979796992/20210620_175120.jpg", "https://cdn.discordapp.com/attachments/382626005719973888/782459095076438016/En9ZCmUVoAAQr9a.png", "https://media.tenor.com/images/fc6a0a6b37ae0222f8584e7fe17287a5/tenor.gif", "https://c.tenor.com/ueyS_37jZtYAAAAd/touhou-fumo.gif", "https://c.tenor.com/ZxRJ0mBd5SYAAAAd/cirno-bounce-cirno.gif", "https://c.tenor.com/TajFm9pWBTIAAAAC/touhou-nazrin.gif", "https://c.tenor.com/roV1Rdz5prEAAAAC/touhou-touhou-spin.gif", "https://c.tenor.com/Di28Vu8t80UAAAAd/touhou-touhouproject.gif", "https://media.discordapp.net/attachments/813527204087463997/866689626416087060/image0.gif", "https://media1.tenor.com/images/39556c0ba08afc34038327c836875af2/tenor.gif", "https://c.tenor.com/9KO2hR8C93UAAAAd/hakurei-reimu-fumo.gif", "https://media.discordapp.net/attachments/257310633211461633/716484305362092092/Cirno_Wave.gif", "https://cdn.discordapp.com/attachments/382626005719973888/740025252280795167/653602872952619018.gif", "https://cdn.discordapp.com/attachments/382626005719973888/784123325512548414/ezgif.com-video-to-gif.gif", "https://media.discordapp.net/attachments/257310633211461633/755461120478806106/20200916_014103.gif", "https://cdn.discordapp.com/attachments/382626005719973888/817493661876748290/image0-1.gif", "https://media.discordapp.net/attachments/257310633211461633/838657878541467708/ezgif.com-reverse.gif"]

  embed = discord.Embed(description='Fumo!', colour=0xFF000)
  embed.set_image(url=random.choice(FUMO))
  embed.set_footer(text='Comando secreto: 1 de 4')
  await ctx.send(embed=embed)


@bot.command()
async def taiko(ctx):
  TAIKO = ["https://c.tenor.com/o44X2yAtPs0AAAAd/taiko-no.gif", "https://c.tenor.com/R-hX39T659kAAAAC/taiko-no-tatsujin-taiko.gif", "https://c.tenor.com/zCYT046w49IAAAAC/taikonotatsujin-taiko.gif", "https://c.tenor.com/bRLWidW_AF8AAAAd/taiko-no-tatsujin-donchan.gif", "https://64.media.tumblr.com/a434355d559a9d79927c0817b6426a6e/tumblr_inline_neeep6o4Re1sgtn17.gif", "https://64.media.tumblr.com/03e417a49f3d91af116c842c7a77f489/tumblr_inline_nx0x5dSAQt1sgtn17_250.gif"]

  embed = discord.Embed(description='DA-DON!', colour=0xFF000)
  embed.set_image(url=random.choice(TAIKO))
  embed.set_footer(text='Comando secreto: 2 de 4')
  await ctx.send(embed=embed)

@bot.command()
async def wise(ctx):
  WISE = ["https://cdn.discordapp.com/attachments/473657277241622528/881367817281208340/Thetalibanrightnow_140b922add3527ce61054026b3305f30.jpg", "https://i.imgflip.com/4gna7k.jpg", "https://i1.kym-cdn.com/photos/images/original/001/225/410/fe4.jpg"]

  embed = discord.Embed(colour=0xFF000)
  embed.set_image(url=random.choice(WISE))
  embed.set_footer(text='Comando secreto: 3 de 4')
  await ctx.send(embed=embed)

@bot.command()
async def atf(ctx):
  ATF = ["https://cdn.discordapp.com/attachments/473657277241622528/881379530084872292/D0hsMrKW0AA9WGW.jpeg", "https://cdn.discordapp.com/attachments/473657277241622528/881378838070853702/45f6wz.jpg", "https://cdn.discordapp.com/attachments/473657277241622528/881379119475077140/611e6e04a1d52c608406b5b1e43ad20edbbe9f506b41d3f62af71d612a6d2fb7_1.jpg", "https://cdn.discordapp.com/attachments/473657277241622528/881379942871494706/D0hW6_FWoAA6eWh.jpeg"]

  embed = discord.Embed(colour=0xFF000)
  embed.set_image(url=random.choice(ATF))
  embed.set_footer(text='Comando secreto: 4 de 4')
  await ctx.send(embed=embed)  

bot.run(os.getenv('contrasena'))
