from discord.ext import commands
import discord

import random
import responses

#the abundacne of lists
msgList = [" "]
bannedWords = ["nigger", "nigga", ">send", ">help", ">repeat"]
noises = ["\*squawk*", "\*chirp*", "\*caw*", "\*tweet*", "\*caw caw*"]

bot = commands.Bot(command_prefix=">", intents=discord.Intents.all())

def addToList(msg):
    global msgList
    lower = msg.lower()

    for banned in bannedWords:
        if lower.find(banned) != -1:
            return
        
    msgList.append(msg)

def getMessage():
    txt = random.choice(msgList)
    noise = random.choice(noises)

    if random.randint(1, 2) == 1:
        return txt + " " + noise
    else:
        return noise + " " + txt

@bot.event
async def on_ready():
    print("bot olnine")
    channel = bot.get_channel(1161098199260471306)
    await channel.send(random.choice(noises))

@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return

    if bot.user.mentioned_in(msg):
        await msg.reply(msg.author.mention + " " + responses.handlePing(msg))
    elif random.randint(1, 20) == 1:
        await msg.channel.send(getMessage())
        addToList(msg.content)
    elif random.randint(1, 100) == 1:
        await msg.channel.send("$100 bills")
        addToList(msg.content)
    else:
        addToList(msg.content)

    await bot.process_commands(msg)

@bot.command()
async def send(ctx):
    if ctx.message.author.id == 804463117232242748:
        await ctx.send(getMessage())

@bot.command()
async def repeat(ctx, *msg):
    if ctx.message.author.id == 804463117232242748:
        await ctx.send(" ".join(msg))

#no token for you :)
bot.run(token="")