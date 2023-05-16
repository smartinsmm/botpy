import discord
import asyncio
import json
import random
import os
from googletrans import Translator
from discord.ext import commands
from liste import historique_commandes, classeur

translator = Translator()
intents = discord.Intents.all()
intents.typing = False
intents.presences = False
History = historique_commandes()
client = commands.Bot(command_prefix="<", intents = intents)
Classeur = classeur()

User = None

'''shop_items = {
        'article 1 ': {
            'name': 'point_bonus',
            'price': 1000
        },
        'article 2 ': {
            'name': 'une_année_à_ynov',
            'price': 7000
        },
        'article 3 ': {
            'name': 'bougie',
            'price': 15
        },
        'article 4 ': {
            'name': 'figurine_warhammer',
            'price': 80
        }
    }'''

#########################          HISTORIQUE          #########################

@client.command(name="full_history")
async def full_history(ctx):
    all_commands = History.get_all_commands()
    for command in all_commands:
        await ctx.channel.send(command)
    await ctx.channel.send(Classeur)
    History.add_command("full_history ")
    
        
@client.command(name="last_command")
async def full_history(ctx):
    last_command = History.get_last_command()
    await ctx.channel.send("la dernière commande taper est : "+ last_command)

#########################      FIN DE L'HISTORIQUE      #########################


@client.command(name="del")
async def delete(ctx, number):
    await ctx.channel.purge(limit=int(number))
    History.add_command("del")
    print("test1")

@client.command(name="scoobi")
async def scoobi(ctx):
    user = await client.fetch_user(353516010621370375)
    # Envoie l'autocollant dans le canal
    sticker = await ctx.channel.send("<:scoobido:1234567890>")
    # Ping l'utilisateur qui a utilisé la commande
    await ctx.send(f"{user.mention} voici l'autocollant Scooby Doo !")


@client.command(name="portem")
async def portem(ctx):
    user = str(ctx.author.id)
    with open('portem.json', 'r') as f:
        if os.stat('portem.json').st_size == 0:
            portem = {}
        else:
            portem = json.load(f)

    if user not in portem:
        portem[user] = 0

    await ctx.send(f"Ton solde actuel est : {portem[user]}")

@client.command(name="loto")
async def loto(ctx):
    user = str(ctx.author.id)
    with open('portem.json', 'r') as f:
        if os.stat('portem.json').st_size == 0:
            portem = {}
        else:
            portem = json.load(f)

    if user not in portem:
        portem[user] = 0

    earnings = random.randint(100000000, 10000000000)
    portem[user] += earnings

    with open('portem.json', 'w') as f:
        json.dump(portem, f)

    await ctx.send(f"Tu as gagné {earnings} ! Ton solde actuel est : {portem[user]}")


@client.event
async def on_ready():
    print("Le bot est prêt !")

'''@client.event
async def on_typing(channel, user, when):
     await channel.send(user.name+" is typing")'''

'''@client.event
async def on_member_join(member):
    general_channel = client.get_channel(900121118621450283)
    await general_channel.send("Bienvenue sur le serveur ! "+ member.name)'''

        
@client.event
async def on_message(message):
    
    
    if message.author == client.user:
        return
    
    await client.process_commands(message)
    
    if message.content.startswith("hello"):
        await message.channel.send("hello")
    
    if message.channel.id == 1107399764544335922 and message.content.startswith("<"):
        User = message.author.name
        message_content = message.content[1:]
        test = [User, message_content]
       
        Classeur.all_command_user(test)
        last_c = Classeur.get_all()
        output = "\n".join(" ".join(map(str, row)) for row in last_c)
        
##################### opt1#################################   
    if message.content.startswith('<rappel'):
        await handle_reminder(message)
        History.add_command("rappel ")
##################### opt2#################################   
    if message.content.startswith('<traduire'):
        await translate_message(message)
#####################rappel#################################   
async def handle_reminder(message):
    reminder_time = 0
    reminder_message = ""

    try:
        # Extraire le temps du rappel en secondes depuis le message
        reminder_time = int(message.content.split()[1])
        reminder_message = ' '.join(message.content.split()[2:])
    except (IndexError, ValueError):
        await message.channel.send("Format de commande incorrect. Utilisation : !rappel <temps en secondes> <message>")
        return

    await message.channel.send(f"Je te rappellerai '{reminder_message}' dans {reminder_time} seconde(s).")

    await asyncio.sleep(reminder_time)
    await message.channel.send(f"{message.author.mention}, tu m'as demandé de te rappeler '{reminder_message}' !")
#####################rappel fin#################################   
#####################Trad #################################   
async def translate_message(message):
    try:
        text_to_translate = ' '.join(message.content.split()[1:])
        translated_text = translator.translate(text_to_translate, dest='fr').text
        await message.channel.send(f"Traduction : {translated_text}")
    except Exception as e:
        await message.channel.send("Une erreur s'est produite lors de la traduction.")        
#####################Trad fin#################################   
##########################Poker test############################

@client.command()
async def poker(ctx, mise: int, joueurs: int):
    if joueurs < 2:
        await ctx.send("Le jeu de poker nécessite au moins deux joueurs.")
        return

    if mise <= 0:
        await ctx.send("La mise doit être supérieure à zéro.")
        return

    joueurs_list = ctx.message.mentions[:joueurs]

    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
    cartes_joueur = {joueur: random.sample(deck, 2) for joueur in joueurs_list}

    await ctx.send("Les cartes ont été distribuées !")
    for joueur, cartes in cartes_joueur.items():
        await ctx.send(f"{joueur.name}: {', '.join(cartes)}")

    # Les tours d'enchères
    tour = 1
    mises = {joueur: 0 for joueur in joueurs_list}
    pot = 0

    while tour <= 3:
        await ctx.send(f"--- Tour {tour} ---")

        for joueur in joueurs_list:
            if mises[joueur] < mise:
                await ctx.send(f"{joueur.name}, à toi de jouer ! (Mise actuelle : {mises[joueur]})")
                try:
                    message = await bot.wait_for('message', check=lambda m: m.author == joueur and m.channel == ctx.channel, timeout=30)
                    mise_joueur = int(message.content)

                    if mise_joueur > (mise - mises[joueur]):
                        await ctx.send("Mise invalide. Tu ne peux pas miser plus que ce qu'il te reste.")
                        continue

                    mises[joueur] += mise_joueur
                    pot += mise_joueur
                except asyncio.TimeoutError:
                    await ctx.send(f"{joueur.name} n'a pas répondu à temps et est éliminé du jeu.")
                    joueurs_list.remove(joueur)

        tour += 1

    # Détermination du gagnant
    combinaisons = {joueur: obtenir_combinaison(cartes) for joueur, cartes in cartes_joueur.items()}
    meilleur_combinaison = max(combinaisons.values())
    gagnants = [joueur for joueur, combinaison in combinaisons.items() if combinaison == meilleur_combinaison]

    if len(gagnants) == 1:
        gagnant = gagnants[0]
        await ctx.send(f"{gagnant.name} remporte le pot de {pot} !")
        with open('balances.json', 'r') as f:
            balances = json.load(f)

        balances[str(gagnant.id)] += pot
        with open('balances.json', 'w') as f:
            json.dump(balances, f)
    else:
        await ctx.send("s")
#####################Poker test fin#######################
#####################Shop#################################
shop_items = {
    'article 1': {
        'name': 'point_bonus',
        'price': 1000
    },
    'article 2': {
        'name': 'une_année_à_ynov',
        'price': 7000
    },
    'article 3': {
        'name': 'bougie',
        'price': 15
    },
    'article 4': {
        'name': 'figurine_warhammer',
        'price': 80
    }
}

@client.command(name="boutique")
async def boutique(ctx):
    items_list = '\n'.join([f"{item}: {shop_items[item]['name']} - {shop_items[item]['price']} pièces" for item in shop_items])
    await ctx.send(f"Voici les articles disponibles :\n{items_list}")

@client.command(name="acheter")
async def acheter(ctx, *, item):
    user = str(ctx.author.id)
    with open('portem.json', 'r') as f:
        portem = json.load(f)

    with open('inventaire.json', 'r') as f:
        if os.stat('inventaire.json').st_size == 0:
            inventaire = {}
        else:
            inventaire = json.load(f)

    if user not in portem:
        portem[user] = 0

    item_data = None
    for key, value in shop_items.items():
        if item.lower() == value['name']:
            item_data = value
            break

    if item_data is None:
        await ctx.send("Cet article n'existe pas dans la boutique.")
        return

    if portem[user] < item_data['price']:
        await ctx.send("Tu n'as pas assez de pièces pour acheter cet article.")
        return

    portem[user] -= item_data['price']

    if user not in inventaire:
        inventaire[user] = []

    inventaire[user].append(item_data['name'])

    with open('portem.json', 'w') as f:
        json.dump(portem, f)

    with open('inventaire.json', 'w') as f:
        json.dump(inventaire, f)

    await ctx.send(f"Tu as acheté {item_data['name']} ! Ton solde actuel est de {portem[user]} pièces.")

@client.command(name="inventaire")
async def inventaire(ctx):
    user = str(ctx.author.id)
    with open('inventaire.json', 'r') as f:
        inventaire = json.load(f)

    if user not in inventaire or not inventaire[user]:
        await ctx.send("Ton inventaire est vide.")
    else:
        items_list = '\n'.join(inventaire[user])
        await ctx.send(f"Voici ton inventaire :\n{items_list}")
#####################Shop fin#################################


client.run("je suis trop con")
