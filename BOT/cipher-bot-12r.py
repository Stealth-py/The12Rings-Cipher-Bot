import discord
from discord.ext import commands
import dynamic_cipher
import secret_cipher
import the_infinity_cipher
import tw_cipher

token = '<your-token-here>'

something = commands.Bot(command_prefix='!', case_insensitive=True)
something.remove_command('help')


@something.command()
async def help(ctx):
    p1 = discord.Embed(title="Help", color=0x6c0101)
    p2 = discord.Embed(title="Encoding", color=0x6c0101)
    p3 = discord.Embed(title="Decoding", color=0x6c0101)
    msg1 = "I am the Cipher Bot. \nThere are currently 4 cipher records recorded in my entry. \n1) Clock cipher(12 Cipher); \n2) Infinity Cipher; \n3) Secret Cipher; \n4) Dynamic Cipher; \nYou can get your results by using the prefix **!** before the required cipher name.\n"
    msg2 = "1) Clock cipher: `!declock <your ciphertext>`; \n2) Infinity cipher: `!deinfinity <your ciphertext>`; \n3) Secret cipher: `!desecret <your ciphertext>`; \n4) Dynamic cipher: `!dedynamic <your ciphertext>`; \n"
    msg3 = "For clock cipher: should be separated by a period(`.`)\nFor infinity cipher: should be separated by a period(`.`)\nFor secret cipher: should be separated by a period(`.`)\nFor dynamic cipher: should be separated by a comma and a space(`,`)\n"
    msg4 = "1) Clock cipher: `!enclock <your ciphertext>`; \n2) Infinity cipher: `!eninfinity <your ciphertext>`; \n3) Secret cipher: `!ensecret <your ciphertext>`; \n4) Dynamic cipher: `!endynamic <your ciphertext>`; \n"
    msg5 = "For encoding your plaintext into any ciphertext, please separate the words using a period(`.`)"
    p1.add_field(name="Info", value=msg1, inline=False)
    p2.add_field(name="Commands for Encoding", value=msg4, inline=False)
    p2.add_field(name="Format for Encoding", value = msg5, inline=False)
    p3.add_field(name="Commands for Decoding", value=msg2, inline=False)
    p3.add_field(name="Format for Decoding", value=msg3, inline=False)

    msg = await ctx.channel.send(embed=p1)

    pages = [p1, p2, p3]
    # message = await something.say(embed=p1)
    await msg.add_reaction('\u23ee')
    await msg.add_reaction('\u25c0')
    await msg.add_reaction('\u25b6')
    await msg.add_reaction('\u23ed')

    i = 0
    emoji = ''

    while True:
        if emoji == '\u23ee':
            i = 0
            await msg.edit(embed=pages[i])
        if emoji == '\u25c0':
            if i > 0:
                i -= 1
                await msg.edit(embed=pages[i])
        if emoji == '\u25b6':
            if i < 2:
                i += 1
                await msg.edit(embed=pages[i])
        if emoji == '\u23ed':
            i = 2
            await msg.edit(embed=pages[i])

        res, u = await something.wait_for('reaction_add', check=lambda r, us: (r.emoji == '⏮' or r.emoji == '◀' or r.emoji == '▶' or r.emoji == '⏭' and r.message.id == msg.id) and msg.id == r.message.id and r.message.guild.id == msg.guild.id)
        if res is None:
            break
        if u.id != something.user.id:
            emoji = str(res.emoji)
            await msg.remove_reaction(res.emoji, u)
    await msg.clear_reactions()


@something.command()
async def declock(ctx):
    x = ctx.message.content.strip('!declock ')
    await ctx.send("Here are your results: \n")
    res = tw_cipher.dclock_cipher((str(x)))
    for i in res:
        await ctx.send("```{}```".format(i))


@something.command()
async def enclock(ctx):
    x = ctx.message.content.strip('!enclock ')
    await ctx.send("Here is your ciphertext: \n")
    res = tw_cipher.eclock_cipher(str(x))
    await ctx.send("```{}```".format(res))


@something.command()
async def deinfinity(ctx):
    x = ctx.message.content.strip('!deinfinity ')
    await ctx.send("Here are your results: \n")
    res = the_infinity_cipher.dinf_cipher((str(x)))
    for i in res:
        await ctx.send("```{}```".format(i))


@something.command()
async def eninfinity(ctx):
    x = ctx.message.content.strip('!eninfinity ')
    await ctx.send("Here is your ciphertext: \n")
    res = the_infinity_cipher.einf_cipher(str(x))
    await ctx.send("```{}```".format(res))


@something.command()
async def desecret(ctx):
    x = ctx.message.content.strip('!desecret ')
    await ctx.send("Here are your results: \n")
    res = secret_cipher.desec_cipher((str(x)))
    for i in res:
        await ctx.send("```{}```".format(i))


@something.command()
async def ensecret(ctx):
    x = ctx.message.content.strip('!ensecret ')
    await ctx.send("Here is your ciphertext: \n")
    res = secret_cipher.ensec_cipher(str(x))
    await ctx.send("```{}```".format(res))


@something.command()
async def dedynamic(ctx):
    x = ctx.message.content.strip('!dedynamic ')
    await ctx.send("Here are your results: \n")
    res = dynamic_cipher.dedyna_cipher((str(x)))
    for i in res:
        await ctx.send("```{}```".format(i))


@something.command()
async def endynamic(ctx):
    x = ctx.message.content.strip('!endynamic ')
    await ctx.send("Here is your ciphertext: \n")
    res = dynamic_cipher.endyna_cipher(str(x))
    await ctx.send("```{}```".format(res))


something.run(token)
