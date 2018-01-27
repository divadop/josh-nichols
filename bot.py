import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import re
import os

Client = discord.Client()
client = commands.Bot(command_prefix = "j.")

@client.event
async def on_ready():
    print("I'm ready, beatch!")

@client.event
async def on_message(mes):
    if mes.author.id == "406847337277947934":
        pass
    elif mes.author.id == "11037":
        pass
    else:
        if re.search(r"porps", mes.content.lower()):
            ID = mes.author.id
            await client.send_message(mes.channel, "what do you want from porps, <@{0}> ? he's a busy man ya know".format(ID))
        if re.search(r"david", mes.content.lower()):
            ID = mes.author.id
            await client.send_message(mes.channel, "who said dat name? was it you? what do you want? ask me, I'll tell him in DMs <@{0}>.".format(ID))
        if re.search(r"wood", mes.content.lower()):
            ID = mes.author.id
            await client.send_message(mes.channel, "lol wood makes me go :eggplant::sweat_drops: <@{0}>.".format(ID))
        if re.search(r"[^a-zA-Z]?gay", mes.content.lower()):
            ID = mes.author.id
            await client.send_message(mes.channel, "random fan fact: people who use the word 'gay' too often are more likely to be gay lmao <@{0}>.".format(ID))
        if re.search(r"brb pee", mes.content.lower()):
            ID = mes.author.id
            await client.send_message(mes.channel, "HAHA YES VERY FUNNY MEME (sarcasm) <@{0}>.".format(ID))
        if re.search(r"fuck", mes.content.lower()):
            ID = mes.author.id
            await client.send_message(mes.channel, "~~I'm not allowed to stop you from cursing anymore so go on uwu~~ <@{0}>.".format(ID))
        if re.match(r"i'm", mes.content.lower()):
            ID = mes.author.id
            await client.send_message(mes.channel, "lol, I miss DadBOT <@{0}>.".format(ID))
        if re.search(r"[^a-zA-Z]?lol[^a-zA-Z]?", mes.content.lower()):
            ID = mes.author.id
            await client.send_message(mes.channel, "lmao <@{0}>.".format(ID))
        if mes.content.lower().startswith("hi"):
            ID = mes.author.id
            res = mes.content.split(" ")
            await client.send_message(mes.channel, "I ain't no \"{0}\" lmao. <@{1}> u gay as fuck lol.".format(" ".join(res[1:]), ID))
        if mes.content.lower().startswith("what"):
            ID = mes.author.id
            res = mes.content.split(" ")
            await client.send_message(mes.channel, "whatwhatwhatwhat. what is it? stop with the fucking what questions ffs <@{0}> u bad".format(ID))
        if re.search(r"lmao", mes.content.lower()):
            ID = mes.author.id
            await client.send_message(mes.channel, "ye laughing my ass off too lol <@{0}>.".format(ID))
        if re.search(r"josh nichols", mes.content.lower()):
            ID = mes.author.id
            await client.send_message(mes.channel, "fucker don't use my name, copyRIgHt inFRinGEmEnt <@{0}>.".format(ID))
        if re.search(r"[^a-zA-Z]?i’m", mes.content.lower()):
            ID = mes.author.id
            await client.send_message(mes.channel, "you think if you use that weird ass ’ symbol 'stead of ', you'll get away with starting the message with an 'I'm'? Lol think again *you walnut* <@{0}>.".format(ID))
        if re.search(r"porn", mes.content.lower()):
            ID = mes.author.id
            await client.send_message(mes.channel, "porn? lol y u so horny <@{0}>.".format(ID))
        if re.search(r":thonking:", mes.content.lower()):
            ID = mes.author.id
            await client.send_message(mes.channel, "so ya like thonking huh <@{0}>.".format(ID))
        if re.search(r"annoying", mes.content.lower()):
            ID = mes.author.id
            await client.send_message(mes.channel, "ur mahm is annoying <@{0}>.".format(ID))
        if re.search(r"[^a-zA-Z]?die[^a-zA-Z]?", mes.content.lower()):
            ID = mes.author.id
            await client.send_message(mes.channel, "no u <@{0}>.".format(ID))
        if re.search(r"roleplay", mes.content.lower()) or re.search(r"[^a-zA-Z]?rp[^a-zA-Z]?", mes.content.lower()):
            ID = mes.author.id
            await client.send_message(mes.channel, "what's a roleplay lol <@{0}>.".format(ID))
        if re.search(r"[^a-zA-Z]?oof", mes.content.lower()):
            ID = mes.author.id
            await client.send_message(mes.channel, "***o o f*** indeed uwu <@{0}>.".format(ID))
        if re.search(r"^no u$", mes.content.lower()):
            ID = mes.author.id
            await client.send_message(mes.channel, "no u <@{0}>.".format(ID))
        if re.search(r"[^a-zA-Z]rape", mes.content.lower()):
            ID = mes.author.id
            await client.send_message(mes.channel, "wtf rape is bad >:O <@{0}>.".format(ID))
        if re.search(r"[^a-zA-Z]?i ser[^a-zA-Z]?", mes.content.lower()):
            ID = mes.author.id
            await client.send_message(mes.channel, "that meme is so old :\<@{0}>.".format(ID))
        if re.search(r"[^a-zA-Z]?ken[^a-zA-Z]?", mes.content.lower()):
            ID = mes.author.id
            await client.send_message(mes.channel, "lmao 10/10 roleplay <@{0}>.".format(ID))
        if re.search(r"[^a-zA-Z]?love[^a-zA-Z]?", mes.content.lower()):
            ID = mes.author.id
            await client.send_message(mes.channel, "what is love? baby don't hurt me  owo<@{0}>.".format(ID))
            
        if mes.content.lower().startswith("j.calc"):
            if re.match(r"^j.calc [0-9]+ [0-9]+ [0-9]+$", mes.content):
                ID = mes.author.id
                res = mes.content.split(" ")
                bal = int(res[1])
                bet = int(res[2])
                total_tries = int(res[3])
                tries = 0
                temp = bet
                while temp <= bal:
                    tries += 1
                    temp *= 2

                if total_tries<=tries and bal-tries*bet > 0:
                    await client.send_message(mes.channel, "You ***can't even fucking lose all your money with {0} tries, you'll have {1} dollars even if you lose every single time wtf <@{2}> you ok?".format(str(total_tries), str(bal-tries*bet), ID))
                elif total_tries <= 0 or bal <=0 or bet <=0:
                    await client.send_message(mes.channel, "What the fuck, you can't even start the game like that smh. <@{0}>.".format(ID))
                elif bet > bal:
                    await client.send_message(mes.channel, "lmao the bet is bigger than the balance, ye sure good luck with that lol. <@{0}>.".format(ID))
                else:
                    chance = 100-((1-((1-(0.5**tries))**(total_tries/tries)))*100)
                    await client.send_message(mes.channel, "The chance that you won't lose all your money in the end is {0}%, <@{1}>.".format(chance, ID))
                    if chance >= 99:
                        await client.send_message(mes.channel, "Oof, that's a pretty high chance. I wish you lose lmao, that'd be funny af. jk I don't care uwu")
                    elif chance >= 75:
                        await client.send_message(mes.channel, "Hmmm, at least it's more than 75%. I'd risk it but lmao I'm not you and I'm JOSH NICHOLS!")
                    elif chance >= 50:
                        await client.send_message(mes.channel, "Do you rly wanna risk it? Although, the probability is not smaller than 50%, which is good enough. You could just go all in, the probability would be close. Still, whatevs, good luck I guess? :thinking:")
                    elif chance >= 25:
                        await client.send_message(mes.channel, "Nah man not worth it, unless you totes desperate lmao. I'd still advise tryin' to tweak the numbers ya see?")
                    elif chance >= 10:
                        await client.send_message(mes.channel, "Lmao don't even try")
                    else:
                        await client.send_message(mes.channel, "wtf, you can't be considering that, that'd be the stupidest thing ever rly")
            else:
                await client.send_message(mes.channel, "wtf that's not how the command works lol. r u blind <@{0}>?\n`j.calc bal bet tries`      this is the syntax. use ***fucking numbers***, jesus christ.".format(mes.author.id))

        if mes.content == "j.commands":
            await client.send_message(mes.channel, "Oh commands? OK\n```LMAO NO COMMANDS\njk, there is one command uwu\n```\n`j.calc bal bet tries`\n```Bal is your current balance.\nbet is the minimal bet, the bet you're gonna start with, ya feel me?\ntries is the amount of coinflips ya gonna do with my killer tactic ok?```\n```wait lol there's another command, I almost forgot```\n`j.tactic`\n```describes my KILLER tactic lol.```")
        if mes.content == "j.tactic":
            await client.send_message(mes.channel, "Here's my killer tactic dude. So, don't question how it works, you can figure it out if you have brains lmao.\n```So, first, choose a minimal bet, that's the lowest you'll bet. It should be small enough, compared to the balance.\nAfter that, flip the coin, placing the minimal bet. If you lose - double the bet. Keep doing that till you win, and return to the minimal bet.\nDoe you shouldn't double the bet if you win, ever.\nUse the j.calc command to calculate the chance of not fucking up. Ye I'll do the math for ya, walnut, ya better be thankful. Type j.commands to see how the command works lol.```")

bot.run(os.getenv('TOKEN'))
