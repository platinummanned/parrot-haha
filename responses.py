from discord.ext import commands
import discord

import random

a = False

#bird
noises = ["\*squawk*", "\*chirp*", "\*caw*", "\*tweet*", "\*caw caw*"]

#on ping
greetings = ["hihihi!!!", "hi!!!!!", "hiya", "SHUT UP", "https://media.discordapp.net/attachments/832893472356302868/1091790331437121648/piong_again_n_sex.gif", "im gonna jack ur box"]
positive = ["YAY UR ONLINE", "I LOVE U", "U THE GOAT FR", "this guy is a massive W", "sex pls"]
negative = ["fuck you man", "i hate you", "this guy sucks", "i dont like you bro"]

#on question
questions = ["why u ping!?!?!?", "wut u want?", "what u need???", "u has question?"]
yesno = ["yes", "yeah", "yup", "yuh uh", "no", "nope", "nah", "nuh uh"]
rather = ["option 1", "#1 for sure", "first one seems good", "ill take #1", "option 2", "#2 on top", "second one sounds nice", "ill go for #2"]
howto = ["idk man dont ask me", "im just a parrot i cant do this shit", ":man_shrugging:", "you have to like do yknow", "open the jar then take out the cookies and crush it into your face", "you have to jack your box"]

#on ping + msg
accept = ["oh ok", "okie dokie", "ohhhhh", "alr got it"]
decline = ["i dont think so", "are u sure", "idk man", "hmm..."]


def getResponse(t):
    return random.choice(t)

def findLiked(i):
    with open(r"C:\Users\keshi\Documents\thing\Python\parrot\loved.txt", "r") as file: #insert loved list file path
        content = file.read()

        if str(i) in content:
            return True
        else:
            return False

def findHated(i):
    with open(r"C:\Users\keshi\Documents\thing\Python\parrot\hated.txt", "r") as file: #insert hated list file path
        content = file.read()

        if str(i) in content:
            return True
        else:
            return False


def handlePing(ctx):
    global a

    msg = ctx.content
    i = ctx.author.id

    if findLiked(i) and not findHated(i):
        return getResponse(positive)
    elif findHated(i) and not findLiked(i):
        return getResponse(negative)

    if msg == "<@1161070845934960900>":
        return getResponse(greetings)
    elif msg.find("?") != -1 and msg.find(" or ") == -1 and msg.find("how ") == -1:
        return getResponse(yesno)
    elif msg.find(" or ") != -1 and msg.find("how ") == -1:
        return getResponse(rather)
    elif msg.find(" or ") == -1 and msg.find("how ") != -1:
        return getResponse(howto)
    elif msg.find("?") == -1 and msg.find(" or ") == -1 and msg.find("how ") == -1:
        if a == False:
            a = True
            return getResponse(questions)
        elif a == True:
           a = False
           return getResponse(accept) 
    else:
        return "idk wut ur tryna tell me rn"
