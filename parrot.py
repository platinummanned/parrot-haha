from discord.ext import commands
import discord
import random

msgList = ["five dollar fake dollar"]
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
    channel = bot.get_channel(1161098199260471306) #testing channel
    await channel.send(random.choice(noises))

@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return
    
    addToList(msg.content)

    if random.randint(1, 20) == 1:
        await msg.channel.send(getMessage())
    elif random.randint(1, 100) == 1:
        await msg.channel.send("$100 bills")

    await bot.process_commands(msg)

@bot.command()
async def send(ctx):
    if ctx.message.author.id == 804463117232242748: #decided to make this command owner only
        await ctx.send(getMessage())

@bot.command()
async def repeat(ctx, *msg):
    await ctx.send(" ".join(msg))


bot.run(token="INSERT TOKEN HERE")
