import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import re
import os

Client = discord.Client()
bot = commands.Bot(command_prefix = "j.")



@bot.event
async def on_ready():
    print("I'm ready, beatch!")
    bot.trigger = True

@bot.command(pass_context=True)
async def commands():
    await bot.say("""Wanna know the commands, {0}? Oh, OK
```LMAO NO COMMANDS
jk, there is one command uwu```
`j.calc bal bet tries`
```Bal is your current balance.
bet is the minimal bet, the bet you're gonna start with, ya feel me?
tries is the amount of coinflips ya gonna do with my killer tactic ok?```
```wait lol there's another command, I almost forgot```
`j.tactic`
```describes my KILLER tactic lol.```
""".format(ctx.message.author))
                  
@bot.command(pass_context=True)
async def tactic(ctx):
    await bot.say("""Here's my killer tactic {0}. So, don't question how it works, you can figure it out if you have brains lmao.
    ```So, first, choose a minimal bet, that's the lowest you'll bet. It should be small enough, compared to the balance.
    After that, flip the coin, placing the minimal bet. If you lose - double the bet. Keep doing that till you win, and return to the minimal bet.
    Doe you shouldn't double the bet if you win, ever. Use the j.calc command to calculate the chance of not fucking up. 
    Ye I'll do the math for ya, walnut, ya better be thankful. Type j.commands to see how the command works lol.```""".format(ctx.message.author))
    
@bot.group(pass_context=True)
async def hey(ctx):
    if ctx.invoked_subcommand is None:
        await bot.say("hWat owo")

@role.command(act="stahp")
async def hey_stahp(act):
    await bot.say("No u")
    if ctx.message.author == "383307469402931210":
        bot.say("*jAYAYHFNSAOIhiaosfhoaissaoifhasoif*\nOK I stahp uwu")
        bot.trigger = False
    else:
        bot.say("don't tell me hwat to do uwu. Ur not my ass-daD uwu.")
        
@role.command(act="annoy")
async def hey_stahp(act):
    await bot.say("lol why")
    if ctx.message.author == "383307469402931210":
        bot.say("*jAYAYHFNSAOIhiaosfhoaissaoifhasoif*\nUnderstood lmao")
        bot.trigger = True
    else:
        bot.say("i'll annoy you in DMs, not here fq. Ur not my ass-daD uwu.")
           

    

@bot.event
async def on_message(mes):
    if mes.author.id == "406847337277947934":
        pass
    elif mes.author.id == "11037":
        pass
    else:
        print(bot.trigger)
        if bot.trigger:
            if re.search(r"porps", mes.content.lower()):
                ID = mes.author.id
                await bot.send_message(mes.channel, "what do you want from porps, <@{0}> ? he's a busy man ya know".format(ID))
            if re.search(r"david", mes.content.lower()):
                ID = mes.author.id
                await bot.send_message(mes.channel, "who said dat name? was it you? what do you want? ask me, I'll tell him in DMs <@{0}>.".format(ID))
            if re.search(r"wood", mes.content.lower()):
                ID = mes.author.id
                await bot.send_message(mes.channel, "lol wood makes me go :eggplant::sweat_drops: <@{0}>.".format(ID))
            if re.search(r"\bgay", mes.content.lower()):
                ID = mes.author.id
                await bot.send_message(mes.channel, "random fan fact: people who use the word 'gay' too often are more likely to be gay lmao <@{0}>.".format(ID))
            if re.search(r"brb pee", mes.content.lower()):
                ID = mes.author.id
                await bot.send_message(mes.channel, "HAHA YES VERY FUNNY MEME (sarcasm) <@{0}>.".format(ID))
            if re.search(r"fuck", mes.content.lower()):
                ID = mes.author.id
                await bot.send_message(mes.channel, "~~I'm not allowed to stop you from cursing anymore so go on uwu~~ <@{0}>.".format(ID))
            if re.match(r"\bi'm", mes.content.lower()):
                ID = mes.author.id
                await bot.send_message(mes.channel, "lol, I miss DadBOT <@{0}>.".format(ID))
            if re.search(r"\blol\b", mes.content.lower()):
                ID = mes.author.id
                await bot.send_message(mes.channel, "lmao <@{0}>.".format(ID))
            if mes.content.lower().startswith("hi"):
                ID = mes.author.id
                res = mes.content.split(" ")
                await bot.send_message(mes.channel, "I ain't no \"{0}\" lmao. <@{1}> u gay as fuck lol.".format(" ".join(res[1:]), ID))
            if mes.content.lower().startswith("what"):
                ID = mes.author.id
                res = mes.content.split(" ")
                await bot.send_message(mes.channel, "whatwhatwhatwhat. what is it? stop with the fucking what questions ffs <@{0}> u bad".format(ID))
            if re.search(r"lmao", mes.content.lower()):
                ID = mes.author.id
                await bot.send_message(mes.channel, "ye laughing my ass off too lol <@{0}>.".format(ID))
            if re.search(r"josh nichols", mes.content.lower()):
                ID = mes.author.id
                await bot.send_message(mes.channel, "fucker don't use my name, copyRIgHt inFRinGEmEnt <@{0}>.".format(ID))
            if re.search(r"\bi’m", mes.content.lower()):
                ID = mes.author.id
                await bot.send_message(mes.channel, "you think if you use that weird ass ’ symbol 'stead of ', you'll get away with starting the message with an 'I'm'? Lol think again *you walnut* <@{0}>.".format(ID))
            if re.search(r"porn", mes.content.lower()):
                ID = mes.author.id
                await bot.send_message(mes.channel, "porn? lol y u so horny <@{0}>.".format(ID))
            if re.search(r":thonking:", mes.content.lower()):
                ID = mes.author.id
                await bot.send_message(mes.channel, "so ya like thonking huh <@{0}>.".format(ID))
            if re.search(r"annoying", mes.content.lower()):
                ID = mes.author.id
                await bot.send_message(mes.channel, "ur mahm is annoying <@{0}>.".format(ID))
            if re.search(r"\bdie\b", mes.content.lower()):
                ID = mes.author.id
                await bot.send_message(mes.channel, "no u <@{0}>.".format(ID))
            if re.search(r"roleplay", mes.content.lower()) or re.search(r"\brp\b", mes.content.lower()):
                ID = mes.author.id
                await bot.send_message(mes.channel, "what's a roleplay lol <@{0}>.".format(ID))
            if re.search(r"\boof", mes.content.lower()):
                ID = mes.author.id
                await bot.send_message(mes.channel, "***o o f*** indeed uwu <@{0}>.".format(ID))
            if re.search(r"^no u\b", mes.content.lower()):
                ID = mes.author.id
                await bot.send_message(mes.channel, "no u <@{0}>.".format(ID))
            if re.search(r"\brape", mes.content.lower()):
                ID = mes.author.id
                await bot.send_message(mes.channel, "wtf rape is bad >:O <@{0}>.".format(ID))
            if re.search(r"\bi ser\b", mes.content.lower()):
                ID = mes.author.id
                await bot.send_message(mes.channel, "that meme is so old :\<@{0}>.".format(ID))
            if re.search(r"\bken\b", mes.content.lower()):
                ID = mes.author.id
                await bot.send_message(mes.channel, "lmao 10/10 roleplay <@{0}>.".format(ID))
            if re.search(r"\blove\b", mes.content.lower()):
                ID = mes.author.id
                await bot.send_message(mes.channel, "what is love? baby don't hurt me  owo<@{0}>.".format(ID))
            
            
           
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
                    await bot.send_message(mes.channel, "You ***can't even fucking lose all your money with {0} tries, you'll have {1} dollars even if you lose every single time wtf <@{2}> you ok?".format(str(total_tries), str(bal-tries*bet), ID))
                elif total_tries <= 0 or bal <=0 or bet <=0:
                    await bot.send_message(mes.channel, "What the fuck, you can't even start the game like that smh. <@{0}>.".format(ID))
                elif bet > bal:
                    await bot.send_message(mes.channel, "lmao the bet is bigger than the balance, ye sure good luck with that lol. <@{0}>.".format(ID))
                else:
                    chance = 100-((1-((1-(0.5**tries))**(total_tries/tries)))*100)
                    await bot.send_message(mes.channel, "The chance that you won't lose all your money in the end is {0}%, <@{1}>.".format(chance, ID))
                    if chance >= 99:
                        await bot.send_message(mes.channel, "Oof, that's a pretty high chance. I wish you lose lmao, that'd be funny af. jk I don't care uwu")
                    elif chance >= 75:
                        await bot.send_message(mes.channel, "Hmmm, at least it's more than 75%. I'd risk it but lmao I'm not you and I'm JOSH NICHOLS!")
                    elif chance >= 50:
                        await bot.send_message(mes.channel, "Do you rly wanna risk it? Although, the probability is not smaller than 50%, which is good enough. You could just go all in, the probability would be close. Still, whatevs, good luck I guess? :thinking:")
                    elif chance >= 25:
                        await bot.send_message(mes.channel, "Nah man not worth it, unless you totes desperate lmao. I'd still advise tryin' to tweak the numbers ya see?")
                    elif chance >= 10:
                        await bot.send_message(mes.channel, "Lmao don't even try")
                    else:
                        await bot.send_message(mes.channel, "wtf, you can't be considering that, that'd be the stupidest thing ever rly")
            else:
                await bot.send_message(mes.channel, "wtf that's not how the command works lol. r u blind <@{0}>?\n`j.calc bal bet tries`      this is the syntax. use ***fucking numbers***, jesus christ.".format(mes.author.id))

bot.run(os.getenv('TOKEN'))
