import discord
import random
import asyncio 
import youtube_dl
from discord.ext import commands, tasks
import random
import mysql.connector
import datetime
import config 








bot = commands.Bot(command_prefix="*")




@bot.event
async def on_ready():
	 activity = discord.Game(name="en construction", type=3)
	 await bot.change_presence(activity=discord.Game(name="*help | que voulez faire ?"))
	 print("Je suis là !")


 

@bot.event
async def on_message(message):
	channel=message.channel
	if bot.user.mentioned_in(message) and message.mention_everyone is False:
		await channel.send("Hey ! Tu peux taper *help si tu as besoin d'aide ! Si tu galères vraiment, ajoute mon créateur en ami : Runger#1422 ! Il se fera une joie de t'aider !")
	await bot.process_commands(message) 












@bot.command()
async def update(ctx):
	embed = discord.Embed(title = "**MISE A JOUR**", description = "Tu veux en savoir plus sur quoi je travaille ? Je travaille pour le moment sur le quizz de ce bot. De plus il sera bientot hébergé, et tu pourras profiter de ce bot 24h/24 :)",  color=000000)
	await ctx.send(embed = embed)










@bot.command()
async def serverinfo(ctx):
	server = ctx.guild
	numberOfTextChannels = len(server.text_channels)
	numberOfVoiceChannels = len(server.voice_channels)
	serverDescription = server.description
	numberOfPerson = server.member_count
	serverName = server.name
	message = f"Le serveur **{server.name}** contient pour l'instant **{numberOfPerson}** personnes. \nVoici sa description : **{serverDescription}** \nCe serveur posssède **{numberOfTextChannels}** salon(s) textuel(s) et **{numberOfVoiceChannels}** salon(s) vocal(aux)."
    
	await ctx.send(message)




@bot.command()
async def avatar(ctx, user: discord.User):
    await ctx.send(user.avatar_url)





@bot.command()
async def say(ctx, *texte):
	await ctx.send(" ".join(texte))

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, limit: int):
        await ctx.channel.purge(limit=limit + 1)


        
       
   


@bot.command()
@commands.has_permissions(administrator = True)
async def ban(ctx, user : discord.User, *reason):
	reason  =  " ".join(reason)
	await  ctx.guild.ban(user, reason  =  reason)
	embed = discord.Embed(title = "**Banissement**", description = "Un ban à eu lieu !",  color=000000)
	embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
	embed.add_field(name = "Membre banni", value = user.name, inline = True)
	embed.add_field(name = "Raison", value = reason, inline = True)
	embed.add_field(name = "Modérateur", value = ctx.author.name, inline = True)
	await ctx.send(embed = embed)

	



@ bot.command()
@commands.has_permissions(administrator = True)
async  def  unban(ctx , user , *reason):
	reason  =  " ".join(reason)
	userName, userId  =  user.split("#")
	bannedUsers  =  await  ctx.guild.bans()
	for  i  in bannedUsers :
		if  i.user.name  ==  userName  and  i.user.id  ==  userId :
			await  ctx.guild.unban( i.user , reason  =  raison )
			await  ctx . send (f":white_check_mark: {user} à été unban !")
			return
	
	await  ctx.send (f":x: L'utilisateur {user} que vous avez demandé n'est pas dans la liste des bans.")



@ bot.command()
@commands.has_permissions(administrator = True)
async  def  kick ( ctx , user : discord.User, *reason):
	reason  =  " ".join(reason)
	await  ctx.guild.kick(user, reason  =  reason)
	embed = discord.Embed(title = "**Expulsion**", description = "Un kick à eu lieu !",  color=000000)
	embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
	embed.add_field(name = "Membre expulsé", value = user.name, inline = True)
	embed.add_field(name = "Raison", value = reason, inline = True)
	embed.add_field(name = "Modérateur", value = ctx.author.name, inline = True)
	await ctx.send(embed = embed)
	
 





async def createMutedRole(ctx):
    mutedRole = await ctx.guild.create_role(name = "Muted",
                                            permissions = discord.Permissions(
                                                send_messages = False,
                                                speak = False),
                                            reason = "Creation du role Muted pour mute des gens.")
    for channel in ctx.guild.channels:
        await channel.set_permissions(mutedRole, send_messages = False, speak = False)
    return mutedRole

async def getMutedRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Muted":
            return role
    
    return await createMutedRole(ctx)

@bot.command()
@commands.has_permissions(administrator = True)
async def mute(ctx, member : discord.Member, *, reason = "Aucune raison n'a été renseigné"):

    mutedRole = await getMutedRole(ctx)
    await member.add_roles(mutedRole, reason = reason)
    embed = discord.Embed(title = "**MUTE**", description = f"{member.mention} vient d'être mute.",  color=000000)
    embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
    await ctx.send(embed = embed)

@bot.command()
@commands.has_permissions(administrator = True)
async def unmute(ctx, member : discord.Member, *, reason = "Aucune raison n'a été renseigné"):
    mutedRole = await getMutedRole(ctx)
    await member.remove_roles(mutedRole, reason = reason)
    embed = discord.Embed(title = "**UNMUTE**", description = f"{member.mention} vient d'être unmute.",  color=000000)
    embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
    await ctx.send(embed = embed)














@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}".format(user.name), description="Membre de ce serveur", color= 000000)
    embed.add_field(name="Nom", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Statut", value=user.status, inline=True)
    embed.add_field(name="Role le plus important", value=user.top_role)
    embed.add_field(name="Rejoint", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)






























@bot.command()
async def invite(ctx):
	await ctx.send("Voici le lien d'invitation du bot ^^ :\nhttps://discord.com/api/oauth2/authorize?client_id=729316323871424552&permissions=8&scope=bot")


























@bot.command()
async def quizz(ctx):

	message = await ctx.send(f"Voulez vous vraiment commencer un quizz ?\n Cliquez sur la réaction ✅ pour le commencer, ou ❌ pour l'annuler.\n `LE QUIZZ AURA LIEU DANS CE SALON !`")
	await message.add_reaction("✅")
	await message.add_reaction("❌")


	def checkEmoji(reaction, user):
		return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")

	try:
		reaction, user = await bot.wait_for("reaction_add", timeout = 10, check = checkEmoji)
		if reaction.emoji == "✅":
			await ctx.send(f"✅ Le quizz va bientot commancer ! **Choississez votre catégorie** :\n\n`Animés/mangas :`\n*mangastart\n\n`Célébrités :`\n*peoplestart\n\n`Géographie :`\n*geostart\n\n`Jeux vidéos :`\n*gamestart\n\n`Histoire :`\n*storystart\n\n`Films/dessins animés :`\n*filmstart\n\n*plus de catégories à venir*")
		else:
			await ctx.send(":x: Vous avez annulé le quizz !")
	except:
		await ctx.send(":x: Vous avez annulé le quizz !")




@bot.command()
async def mangastart(ctx):
	await ctx.send(f"Vous avez choisis la catégorie **mangas et animés !**\nChoississez **votre difficulté** : *débutant*, *medium*, ou *confirmé*, en envoyant\n *<nom de la difficulté>manga\nhttps://tenor.com/view/saitama-one-punch-man-reading-manga-gif-13955562")



@bot.command()
async def débutantmanga(ctx):
	await ctx.send("✅ Le quizz va commencer, en **catégorie** *manga* et en **difficulté** *débutant* !\n\n**Première question**\n`Qui est le rival/meilleur ami de Naruto dans la série du même nom ?`\n A- *Naruto*         B- *Sasuke*\nC- *Sakura*         D- *Kakashi* ")











	









































































@bot.command()
@commands.has_permissions(administrator = True)
async def sondage(ctx):

	await ctx.send("✅ Envoyez votre sondage ici !\n *Note : j'inclus directement la mention here.*")

	def checkMessage(message):
		return message.author == ctx.message.author and ctx.message.channel == message.channel

	try:
		recette = await bot.wait_for("message", timeout = 45, check = checkMessage)
	except:
		await ctx.send(":x: Aie, vous avez mis trop de temps à répondre. Veuillez recommencer le sondage.")
		return
	message = await ctx.send(f"{recette.content} Si vous êtes d'accord, validez en réagissant avec ✅. Sinon réagissez avec ❌\n **LE SONDAGE DURE 15 MINUTES**\n*Mention* : @here ")
	await message.add_reaction("✅")
	await message.add_reaction("❌")


	
	def checkEmoji(reaction, user):
		return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")


	try:
		reaction, user = await bot.wait_for("reaction_add", timeout = 900, check = checkEmoji)
		if reaction.emoji == "✅":
			await ctx.send(timeout = 900) ("@here ✅ La majorité des personnes présentes sont d'accord !")
		else:
			await ctx.send(timeout = 900) ("@here :x: La majorité des personnes présentes ne sont pas d'accord !")
	except:
		await ctx.send(timeout = 900) ("@here :x: La majorité des personnes présentes ne sont pas d'accord !")
















bot.remove_command('help')
@bot.command()
async def help(ctx):
    embed=discord.Embed(title="**HELP**")
    embed.add_field(title = "**MODERATION** *toutes ces commandes nécessite un role administrateur*" )
    embed.add_field(name="BAN",value="Permet de ban quelqu'un - *ban [personne]",inline=False)
    embed.add_field(name="UNBAN",value="Permet de unban une personne déjà banni - *unban [personne]",inline=False)
    embed.add_field(name="KICK",value="Permet d'expulser quelqu'un - *kick [personne]", inline=False)
    embed.add_field(name="CLEAR",value="Nettoie des messages envoyés - *clear [nombres de messages]",inline=False)
    embed.add_field(name="MUTE",value="Permet de mute quelqu'un - *mute [personne]", inline=False)
    embed.add_field(name="UNMUTE",value="Permet d'unmute quelqu'un déjà mute auparavant - *unmute [personne]", inline=False)
    embed.add_field(title = "**MUSIQUE**" )
    embed.add_field(name="A VENIR",value="à venir", inline=False)
    embed.add_field(title = "**AUTRES** *certaines commandes seront précédées de :no_entry:, et elle ne seront executable que par un administrateur*" )
    embed.add_field(name="SERVERINFO",value="Permet d'avoir des informations sur le serveur", inline=False)
    embed.add_field(name="AVATAR",value="Permet d'envoyer l'avatar d'une personne - *avatar [personne]", inline=False)
    embed.add_field(name="SAY",value="Répète ce que vous avez dit - *say [ce que vous voulez dire]", inline=False)
    embed.add_field(name="INVITE",value="Envoie le code d'invitation du bot", inline=False)
    embed.add_field(name="QUIZZ",value="Envoie un quizz", inline=False)


    await ctx.send(embed=embed)












@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send(":x: Cette commande n'existe pas !")

	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(":x: Il manque des arguments\n\n`astuce : rajoutez un nombre, ou le nom d'un membre de ce serveur`")
	elif isinstance(error, commands.MissingPermissions):
		await ctx.send(":x: Vous n'avez pas les permissions requises pour effectuer cette commande !")
	if isinstance(error.original, discord.Forbidden):
		await ctx.send(":x: Je n'ai pas les permissions nécéssaires pour faire cette commmande !\n\nhttps://tenor.com/view/gif-17950188")




		
bot.run("TOKEN")
