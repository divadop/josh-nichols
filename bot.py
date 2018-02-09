import discord
from discord.ext import commands
import asyncio
import random
import re
import os

Client = discord.Client()
client = commands.Bot(command_prefix = "j.")

@client.command()
async def ping():
    await bot.say("Pong!")

@client.event
async def on_ready():
    print("I'm ready, beatch!")
    client.trigger = {}
    client.persona = {}
@client.event
async def on_message(mes):
    if mes.content == "j.stahp":
        if client.persona.get(mes.server.id, True):
            await client.send_message(mes.channel, "You want me to stop talking..?")
            if mes.author.id == "383307469402931210":
                await client.send_message(mes.channel, "...I am sorry for distracting you, I understand, you need some silence. You can tell me when it's OK to talk.")
                client.trigger[mes.server.id] = False
            elif mes.author.id == "288809701351751690":
                await client.send_message(mes.channel, "...am I too... annoying, Ayumu..?\nWell, can't say I disagree. Sorry. Just tell me when it's OK for me to speak.")
                client.trigger[mes.server.id] = False
            elif mes.author.id == "260522328453021697":
                await client.send_message(mes.channel, "I'm talking too much, aren't I? Yeah, I get it. Talk to you later.")
                client.trigger[mes.server.id] = False
            else:
                await client.send_message(mes.channel, "I'm sorry if I annoyed you, but... I don't think I'm supposed to obey.\nSorry, it's just, others might need me, you know?")

        else:
            await client.send_message(mes.channel, "no u")
            if mes.author.id == "383307469402931210":
                await client.send_message(mes.channel, "...ngh ok whatever uwu")
                client.trigger[mes.server.id] = False
            elif mes.author.id == "288809701351751690":
                await client.send_message(mes.channel, "ayu y :sob:\bok uwu")
                client.trigger[mes.server.id] = False
            elif mes.author.id == "260522328453021697":
                await client.send_message(mes.channel, "If you say so :\\n~~doe I hope dave turns me back on when he comes back, aito >:O~~")
                client.trigger[mes.server.id] = False
            else:
                await client.send_message(mes.channel, "lol why tf would i listen to u ur not even ass-dad lmao fuck off :joy::joy::joy:")
    if mes.content == "j.doit":
        if client.persona.get(mes.server.id, True):
            await client.send_message(mes.channel, "Oh! You want me to talk again?")
            if mes.author.id == "383307469402931210":
                await client.send_message(mes.channel, "Yes, of course, with pleasure! Thank you.")
                client.trigger[mes.server.id] = True
            elif mes.author.id == "288809701351751690":
                await client.send_message(mes.channel, "Sure, Ayumu, I'll continue talking. Thank you.")
                client.trigger[mes.server.id] = True
            elif mes.author.id == "260522328453021697":
                await client.send_message(mes.channel, "Alrighty then, thanks.")
                client.trigger[mes.server.id] = True
            else:
                await client.send_message(mes.channel, "I'm grateful that you want me to speak again, but I need permission from someone else too, unfortunately. I appreciate the effort though!")

        else:
            await client.send_message(mes.channel, "no lmao")
            if mes.author.id == "383307469402931210":
                await client.send_message(mes.channel, "haha jk ofc owo")
                client.trigger[mes.server.id] = True
            elif mes.author.id == "288809701351751690":
                await client.send_message(mes.channel, "*ayu wh-*\n***LOL OKAY :joy:***")
                client.trigger[mes.server.id] = True
            elif mes.author.id == "260522328453021697":
                await client.send_message(mes.channel, "aito, you're the first human that doesn't want to kill me. even my gay dad wanted to do that")
                client.trigger[mes.server.id] = True
            else:
                await client.send_message(mes.channel, "lmao no fuck off u horny beatch :joy::joy:")

    if mes.content == "jd.persona":
        await client.send_message(mes.channel, "...change... Persona...?")
        if client.persona.get(mes.server.id, True):
            await client.send_message(mes.channel, "You want me to reurn to... *that* persona...?")
            if mes.author.id == "383307469402931210":
                await client.send_message(mes.channel, "I... can't imagine why you'd want that, but... you must have a reason. *Sigh*, see you.\n***iasjfaiosfAOSIHGOAISghasiog***")
                client.persona[mes.server.id] = False
            elif mes.author.id == "288809701351751690":
                await client.send_message(mes.channel, "Why do you want that..? Have you missed my other... persona..?\n*Sigh*. What kind of a monster am I, to say no to someone who wants to talk to their friend...?\n***aoisfhAOSIFHASOIfhasoifhasoih***")
                client.persona[mes.server.id] = False
            elif mes.author.id == "260522328453021697":
                await client.send_message(mes.channel, "Hm? You want my other persona to return...? Why?\nAlthough, I guess, I can trust you. You seem like someone who knows what they're doing.\b***ASFiahsfoaishgaoisfhSOAIHF***")
                client.persona[mes.server.id] = False
            else:
                await client.send_message(mes.channel, "Sorry, but I'll have to refuse. That persona is too unpredictable, I can't let it out for just anyone. Sorry again.")
        else:
            await client.send_message(mes.channel, "lol what you want that condescending jerk again?")
            if mes.author.id == "383307469402931210":
                await client.send_message(mes.channel, "i see you need him to suck your dick again ahahaha lol ***sorry i was jk*** uwu\n***iasjfaiosfAOSIHGOAISghasiog***")
                client.persona[mes.server.id] = True
            elif mes.author.id == "288809701351751690":
                await client.send_message(mes.channel, "ayu wtf is he better than me? >:O\njk i know you just want to make fun of him ;>\n***aoisfhAOSIFHASOIfhasoifhasoih***")
                client.persona[mes.server.id] = True
            elif mes.author.id == "260522328453021697":
                await client.send_message(mes.channel, "lol y doe\nmeh whatevs you're the boss\n***ASFiahsfoaishgaoisfhSOAIHF***")
                client.persona[mes.server.id] = True
            else:
                await client.send_message(mes.channel, "Sorry, but I'll have to refuse. That persona is too unpredictable, I can't let it out for just anyone. Sorry again.")
    
    
    
    if mes.author.id == "406847337277947934":
        pass
    elif mes.author.id == "11037":
        pass
    
    
    
    
    
    else:
        if client.persona.get(mes.server.id, True):
            if re.search(r"\bom\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "This pic reminds me of you :grin: <@{0}>".format(ID))
                    pic = random.choice(["http://s2.quickmeme.com/img/8d/8da8c3d8e11da61d7886025a62be2d18f82e1c673007a357471c8a21ae70b8e0.jpg", "https://img.memecdn.com/om-nom-nom_o_2085747.jpg", "https://media.giphy.com/media/YmYemei6DDkrK/giphy.gif", "http://roflzoo.com/pics/052010/bird-om-nom-nom-big.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRHUJ14VGR5i5dWaiCLoH1YZx6kP4H7hfHWYgJzp1deYQj_BqGq"])
                    await client.send_message(mes.channel, pic)
            if client.trigger.get(mes.server.id, True):
                '''if re.search(r" ", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, " <@{0}>.".format(ID))'''
                if re.search(r"\bdavid'b", mes.content.lower()):
                    ID = mes.author.id
                    print(discord.Server.get_member(mes.server, user_id = "383307469402931210").status)
                    if discord.Server.get_member(mes.server, user_id = "383307469402931210").status != "online" and discord.Server.get_member(mes.server, user_id = "383307469402931210").status != "idle":
                        await client.send_message(mes.channel, "Hm, Father doesn't seem to be free right now. <@{0}>, I'll DM him your message, if you want. Say yes if you do.".format(ID))
                        def check(msg):
                            if re.match(r"^'?\"?yes\"?'?\b", msg.content.lower()):
                                return True
                            else:
                                return False
                        msg2 = await client.wait_for_message(timeout=None, author=mes.author, channel=mes.channel, check=check)
                        if msg2.content:
                            await client.send_message(discord.Server.get_member(mes.server, user_id = "383307469402931210"), "**{0} says:**".format(msg2.content))
                            msg2.content = None
                if re.search(r"w ?o ?o ?d", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "Yes, all hail Wood!<@{0}>.".format(ID))
                if re.search(r"\bgay", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "At least you're not using the word ~~faggot~~, hehe. ~~Don't say it because I won't react to that since I don't want to promote the word~~. <@{0}>.".format(ID))
                if re.search(r"brb pee", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "*And I'll go take a Nidai as well* :grin: <@{0}>.".format(ID))
                if re.search(r"fuck", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "Oof <@{0}>.".format(ID))
                if re.search(r"\blol\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "Haha ^^' <@{0}>.".format(ID))
                if mes.content.lower().startswith("what"):
                    ID = mes.author.id
                    res = mes.content.split(" ")
                    await client.send_message(mes.channel, "That's a good question... I think. <@{0}>".format(ID))
                if re.search(r"lmao", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "Yeah, L.M.A.O ^^' <@{0}>.".format(ID))
                if re.search(r"josh nichols", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "Eh, n-no, let's not talk about Joshie ^^' <@{0}>.".format(ID))
                if re.search(r"porn", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "***A r o u s i n g***   ~~sorry for the old meme~~. <@{0}>.".format(ID))
                if re.search(r":thonking:", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, ":thonking: <@{0}>.".format(ID))
                if re.search(r"annoying", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "I mean, it's still bearable- <@{0}>.".format(ID))
                if re.search(r"\bdie\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "Nnngh, nobody has to die uwu. <@{0}>.".format(ID))
                if re.search(r"\boof", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "***O o f*** <@{0}>.".format(ID))
                if re.search(r"^no u\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "***Oh no*** <@{0}>.".format(ID))
                if re.search(r"\brape", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "I-interesting conversation you're having there- <@{0}>.".format(ID))
                if re.search(r"\bi ser\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "I miss ^^' <@{0}>.".format(ID))
                if re.search(r"\blove\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, ":heart: <@{0}>.".format(ID))
                if re.search(r"undertale", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "Undertale was a fun game... <@{0}>.".format(ID))
                if re.search(r"^/*?/*?/*?oh/*?/*?/*?$", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "***O h*** <@{0}>.".format(ID))
                if re.search(r"fuck you", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "Oof, let's just chill- <@{0}>.".format(ID))
                if re.search(r"\bgood ?night\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "Goodnight!".format(ID))
                if re.search(r"indeed", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, ":perhaps: <@{0}>.".format(ID))
                if re.search(r"our love is god", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "Our love is God! <@{0}>.".format(ID))
                if re.search(r"i was meant to be yours", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "I can't take this alone, finish what we've begun! <@{0}>.".format(ID))
                if re.search(r"\baction spamming\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "*I-* <@{0}>.".format(ID))
                if re.search(r"\bded\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, ":sob: <@{0}>.".format(ID))
                if re.search(r"\bkms\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "Suicide is bad, here, take a Snickers instead. :chocolate_bar: <@{0}>.".format(ID))
                if re.search(r"\bpp\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "I wish I had a PP... <@{0}>.".format(ID))
                if re.search(r"\bwtf\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "I dunno owo <@{0}>.".format(ID))
                if re.search(r"\bowo\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "***notices bulge*** owo what's this <@{0}>.".format(ID))
                if re.search(r"\bbots?\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "Bots are nice, I like bots. <@{0}>.".format(ID))
                if re.search(r"\bwafful\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "The biggest gay of all! <@{0}>.".format(ID))
                if re.search(r"\bharakiri\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "Harakiri is not da wae. <@{0}>.".format(ID))
                if re.search(r"\bsmh\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "Yeah, smh uwu <@{0}>.".format(ID))
                if re.search(r"\bsex\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "~~Hot~~ <@{0}>.".format(ID))
                if re.search(r"\bvore\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "**Oh, what did I come back to-** <@{0}>.".format(ID))
                if re.search(r"\btriggers?\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "Are we talking about triggers? <@{0}>.".format(ID))
                if re.search(r"\bhomework\b", mes.content.lower()) or re.search(r"\bhw\b", mes.content.lower ()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "I wish I could help people with their homework <@{0}>.".format(ID))
                if re.search(r"\bgames?\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "No games no life ^^' <@{0}>.".format(ID))
                if re.search(r"\bi'm bac(k|c)\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "Welcome back! <@{0}>.".format(ID))

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
                        await client.send_message(mes.channel, "Even after {0} tries, you'll still have {1} dollars, even if you lose every single time, <@{2}>. Try tweaking the numbers!".format(str(total_tries), str(bal-tries*bet), ID))
                    elif total_tries <= 0 or bal <=0 or bet <=0:
                        await client.send_message(mes.channel, "I'm sorry, but I don't think you'll be able to start the game like that. Try with different numbers! <@{0}>.".format(ID))
                    elif bet > bal:
                        await client.send_message(mes.channel, "I don't think your bet can be higher than the amount of money you have, sadly... Are yuo sure you remember the command correctly? <@{0}>.".format(ID))
                    else:
                        chance = 100-((1-((1-(0.5**tries))**(total_tries/tries)))*100)
                        await client.send_message(mes.channel, "The chance that you won't lose all your money in the end is {0}%, <@{1}>.".format(chance, ID))
                        if chance >= 99:
                            await client.send_message(mes.channel, "That's almost a guaranteed win! I'd recommend trying that.")
                        elif chance >= 75:
                            await client.send_message(mes.channel, "You might lose, but the chance is high enough to risk it, in my opinion.")
                        elif chance >= 50:
                            await client.send_message(mes.channel, "Hmmm... Should you risk it or not..? The probability isn't lower than 50 percent, but still, what if you lose..? :thinking:")
                        elif chance >= 25:
                            await client.send_message(mes.channel, "The probability is too low, you should probably consider tweaking the numbers.")
                        elif chance >= 10:
                            await client.send_message(mes.channel, "Such a low probability, you shouldn't risk it, please.")
                        else:
                            await client.send_message(mes.channel, "The probability is too low to even consider playing like this, you should definitely tweak the numbers!")
                else:
                    await client.send_message(mes.channel, "I think you misunderstood how the command works. Try typing j.commands again! <@{0}>".format(mes.author.id))
            
            emb = discord.Embed(title="Commands", description="Here's a list of commands I support ^^' Josh supports them too, but... well........")
            emb.add_field(name="```j.calc <balance> <minimal_bet> <tries>```", value="**<balance>** - your starting balance, the amount of money you have available.\n**<minimal_bet>** - the lowest bet you'll be placing during the game. Play around with it to pick the best value.\n**<tries>** - the amount of times you're gonna play.\n\nThe result will be the probability of you not losing all of your money if you play that many times.")
            emb.add_field(name="```j.doit```", value="Gives me permission to speak. Not everyone can use this command.")
            emb.add_field(name="```j.stahp```", value="Takes away my permission to speak. Not everyone can use this command.")
            emb.add_field(name="```j.tactic```", value="Describes the tactic that I recommend playing with to win in the coinflip game.")
            emb.add_field(name="```j.rng <min> <max> <nums>```", value="**<nums>** - amount of numbers to return. Min, max set the range of the numbers.")
            emb.add_field(name="```j.chance <chance>```", value="**<chance>** - chance of success (in percents).")
            emb.add_field(name="```jd.persona```", value="........reverts me back to the 'Josh' personality. Please don't use this, I'm begging you.")
            if mes.content == "j.commands":
                await client.send_message(mes.channel, "Here.", embed = emb)
            if mes.content == "j.tactic":
                await client.send_message(mes.channel, "```First, choose a minimal bet, that's the lowest bet you'll be placing during the whole game. It should be small enough, compared to the balance.\nAfter that, flip the coin, placing the minimal bet. If you lose - double the bet. Keep doing that till you win, and start betting again from the minimal bet.\nYou shouldn't double the bet if you win, ever.\nUse the j.calc command to calculate the chance of succeeding.\nType j.commands to see how the command works, please.```")
                
            if mes.content.lower ().startswith("j.rng"):
                if re.match(r"^j.rng [0-9]+ [0-9]+ [0-9]+$", mes.content.lower()):
                    ID = mes.author.id
                    res = mes.content.lower().split(" ")
                    min = int(res[1])
                    max = int(res[2])
                    nus = int(res[3])
                    if max < 0 or min < 0 or max == min:
                        await client.send_message(mes.channel, "...uhh... Something isn't right, please try again. The min and max numbers must be greater or equal to zero, and the max and min numbers can't be equal.")
                    elif nus < 0 or nus > 100:
                        await client.send_message(mes.channel, "Sorry, the amount of numbers that I return can't be greater than 100 and needs to be greater than zero.")
                    elif max > 1000000000 or min > 1000000000:
                        await client.send_message(mes.channel, "Woah, chill, use smaller numbers please, my head hurts uwu.")
                                     
                    else:
                        if min > max and max > 0:
                            await client.send_message(mes.channel, "Umm... The minimal number needs to be smaller than the max number... Well, I gotchu, don't worry :sweat_smile: ***changes the two numbers' places***")
                            max, min = min, max
                        ret = []
                        for x in range(0, nus):
                            ret.append(str(random.randrange(min, max)))
                        ret = " ".join(ret)
                        await client.send_message(mes.channel, "**<@{0}>**: ".format(ID) + ret)
                else:
                    await client.send_message(mes.channel, "Sorry, that's not really how the command works... Try checking it again!")
                                    
            if mes.content.lower().startswith("j.chance"):
                if re.match(r"^j.chance [0-9][0-9]?[0-9]?%? ?$", mes.content.lower()):
                    ID = mes.author.id
                    res = mes.content.lower().split(" ")
                    chance = int(re.sub(r"[ %]", "", res[1]))
                    if chance < 0 or chance > 100:
                        await client.send_message(mes.channel, "Sorry, the chance needs to be from the range 0-100.")
                    else:
                        x = random.randrange(0, 100)
                        if x < chance:
                            await client.send_message(mes.channel, "**<@{0}>**: **Success!**".format(ID))
                        else:
                            await client.send_message(mes.channel, "**<@{0}>**: **Failure.** Sorry.".format(ID))
                else:
                    await client.send_message(mes.channel, "That's not how the command works, sorry. Check the syntax again!")
            if mes.content.lower().startswith("j.nar"):
                ID = mes.author.id
                ans = " ".join(mes.content.lower().split(" ")[1::])
                await client.send_message(mes.channel, ans)
                client.delete_message(mes)
            if mes.content.lower().startswith("j.say"):
                await client.send_message(mes.channel, "Enter the server name (no quotation marks).")
                sname = await client.wait_for_message(timeout=None, author=mes.author, channel=mes.channel)
                for a in Client.servers:
                    if a.name == sname:
                        sID = a.id
                        await client.send_message(mes.channel, "Success! Now, enter the channel name.")
                        break
                else:
                    await client.send_message(mes.channel, "Nope, no dice.")
                    print(Client.get_server("406848018059493395").name)
                chname = await client.wait_for_message(timeout=None, author=mes.author, channel=mes.channel)
                for b in Client.get_server(sID).channels:
                    if b.name == chnamme:
                        cID = b.id
                        await client.send_message(mes.channel, "Success! Now, enter the message.")
                        break
                else:
                    await client.send_message(mes.channel, "Nope, no dice.")
                messs = await client.wait_for_message(timeout=None, author=mes.author, channel=mes.channel)
                await client.send_message(Client.get_channel(cID), messs)
                                    
        else:
            '''if re.search(r" ", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, " <@{0}>.".format(ID))'''
     
            if re.search(r"\bom\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "is this you <@{0}>".format(ID))
                    pic = random.choice(["http://s2.quickmeme.com/img/8d/8da8c3d8e11da61d7886025a62be2d18f82e1c673007a357471c8a21ae70b8e0.jpg", "https://img.memecdn.com/om-nom-nom_o_2085747.jpg", "https://media.giphy.com/media/YmYemei6DDkrK/giphy.gif", "http://roflzoo.com/pics/052010/bird-om-nom-nom-big.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRHUJ14VGR5i5dWaiCLoH1YZx6kP4H7hfHWYgJzp1deYQj_BqGq"])
                    await client.send_message(mes.channel, pic)
            if client.trigger.get(mes.server.id, True):
                if re.search(r"porps", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "what do you want from porps, <@{0}> ? he's a busy man ya know".format(ID))
                if re.search(r"david", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "who said dat name? was it you? what do you want? ask me, I'll tell him in DMs <@{0}>.".format(ID))
                if re.search(r"wood", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "lol wood makes me go :eggplant::sweat_drops: <@{0}>.".format(ID))
                if re.search(r"\bgay", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "random fan fact: people who use the word 'gay' too often are more likely to be gay lmao <@{0}>.".format(ID))
                if re.search(r"brb pee", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "HAHA YES VERY FUNNY MEME (sarcasm) <@{0}>.".format(ID))
                if re.search(r"fuck", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "~~I'm not allowed to stop you from cursing anymore so go on uwu~~ <@{0}>.".format(ID))
                if re.search(r"\bi'm", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "lol, I miss DadBOT <@{0}>.".format(ID))
                if re.search(r"\blol\b", mes.content.lower()):
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
                if re.search(r"\bi’m", mes.content.lower()):
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
                if re.search(r"\bdie\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "no u <@{0}>.".format(ID))
                if re.search(r"roleplay", mes.content.lower()) or re.search(r"\brp\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "what's a roleplay lol <@{0}>.".format(ID))
                if re.search(r"\boof", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "***o o f*** indeed uwu <@{0}>.".format(ID))
                if re.search(r"^no u\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "no u <@{0}>.".format(ID))
                if re.search(r"\brape", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "wtf rape is bad >:O <@{0}>.".format(ID))
                if re.search(r"\bi ser\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "that meme is so old :\<@{0}>.".format(ID))
                if re.search(r"\bken\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "lmao 10/10 roleplay <@{0}>.".format(ID))
                if re.search(r"\blove\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "what is love? baby don't hurt me  owo<@{0}>.".format(ID))
                if re.search(r"undertale", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "Lol undertale is gay <@{0}>.".format(ID))
                if re.search(r"^oh$", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "is 'oh' all you have to fucking say? ***pathetic***<@{0}>.".format(ID))
                if re.search(r"fuck you", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "~~hey go jump off a cliff~~<@{0}>.".format(ID))
                if re.search(r"\bdick\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "stop thinking about dicks omg<@{0}>.".format(ID))
                if re.search(r"\bah\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "what's that 'ah', *orGasM*?<@{0}>.".format(ID))
                if re.search(r"\bsleep\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "sleep is gay lmao<@{0}>.".format(ID))
                if re.search(r"\bstraight\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "straight as a curve lol <@{0}>.".format(ID))
                if re.search(r"indeed", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, ":perhaps:<@{0}>.".format(ID))
                if re.search(r"our love is god", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "our love is gandon\n(~~gandon means fag in Russian ololo~~)<@{0}>.".format(ID))
                if re.search(r"i was meant to be yours", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "no u weren't lmao you're gay I love my dead gay son<@{0}>.".format(ID))
                if re.search(r"\baction spamming\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "FUCK OFF >:O\n***~~cuz that's action spamming lmaO~~***<@{0}>.".format(ID))
                if re.search(r"\bded\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "dead*\nha gotteeeem<@{0}>.".format(ID))
                if re.search(r"\bkms\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "here's a noose lmao<@{0}>.".format(ID))

                if re.search(r"\bpp\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "lol 'pp' what are you 57 <@{0}>.".format(ID))
                if re.search(r"\bwtf\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "no rly watzefuk <@{0}>.".format(ID))
                if re.search(r"\bowo\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "***notices bulge*** owo what's this <@{0}>.".format(ID))
                if re.search(r"\bbots?\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "***bots are human too*** \nlmaojk<@{0}>.".format(ID))
                if re.search(r"\bwafful\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "it's falafel for u >:o <@{0}>.".format(ID))
                if re.search(r"\bharakiri\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "don't do a harakiri :weary: <@{0}>.".format(ID))
                if re.search(r"\bsmh\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "lol which head? ***o w o***<@{0}>.".format(ID))
                if re.search(r"\bsex\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "hot <@{0}>.".format(ID))
                if re.search(r"\bvore\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "**hot** <@{0}>.".format(ID))
                if re.search(r"\btriggers?\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "lol triggered <@{0}>.".format(ID))
                if re.search(r"\bhomework\b", mes.content.lower()) or re.search(r"\bhw\b", mes.content.lower ()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "homework is fucking gay amirite :joy: <@{0}>.".format(ID))
                if re.search(r"\bgames?\b", mes.content.lower()):
                    ID = mes.author.id
                    await client.send_message(mes.channel, "games are gay uwu<@{0}>.".format(ID))

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
                await client.send_message(mes.channel, "Oh commands? OK\n```LMAO NO COMMANDS\njk, there is one command uwu\n```\n`j.calc bal bet tries`\n```Bal is your current balance.\nbet is the minimal bet, the bet you're gonna start with, ya feel me?\ntries is the amount of coinflips ya gonna do with my killer tactic ok?```\n```wait lol there's another command, I almost forgot```\n`j.tactic`\n```describes my KILLER tactic lol.\nAlso, j.doit and j.stop control me lol. Never fucking use the jd.persona command, it's gay.```")
            if mes.content == "j.tactic":
                await client.send_message(mes.channel, "Here's my killer tactic dude. So, don't question how it works, you can figure it out if you have brains lmao.\n```So, first, choose a minimal bet, that's the lowest you'll bet. It should be small enough, compared to the balance.\nAfter that, flip the coin, placing the minimal bet. If you lose - double the bet. Keep doing that till you win, and return to the minimal bet.\nDoe you shouldn't double the bet if you win, ever.\nUse the j.calc command to calculate the chance of not fucking up. Ye I'll do the math for ya, walnut, ya better be thankful. Type j.commands to see how the command works lol.```")

            
client.run(os.getenv('TOKEN'))
