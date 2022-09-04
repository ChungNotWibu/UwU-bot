import discord
from discord.ext import commands
from random import random
import random


# ===========================================================

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    # dice
    @commands.command(no_pm=True)
    async def roll(self, ctx):
        embed = discord.Embed(title="Tung xúc xắc từ 1 đến 6", description=f"{ctx.author} đã nhận được số:",color=0xff2222)
        embed.set_thumbnail(url="https://uxwing.com/wp-content/themes/uxwing/download/sport-and-awards/dice-game-icon.png")
        embed.add_field(name= random.randint(1, 6), value= 'Bạn may mắn đấy uwu')
        await ctx.send(embed=embed)

    # upsidedown
    @commands.command(aliases=["updown"])
    async def usd(self, ctx, *, message=None):
        if message == None:
            embed = discord.Embed(title=f"❌ Bạn phải nhập tin nhắn!", color=0xFF0000)
            await ctx.reply(embed=embed, mention_author=False)
            return
        letters = {
            "z":"z",
            "y": "ʎ",
            "x": "x",
            "w": "ʍ",
            "v": "ʌ",
            "u": "n",
            "t": "ʇ",
            "s": "s",
            "r": "ɹ",
            "q": "b",
            "p": "d",
            "o": "o",
            "n": "u",
            "m": "ɯ",
            "l": "l",
            "k": "ʞ",
            "j": "ɾ",
            "i": "ı",
            "h": "ɥ",
            "g": "ɓ",
            "f": "ɟ",
            "e": "ǝ",
            "d": "p",
            "c": "ɔ",
            "b": "q",
            "a": "ɐ",
                }
        message = message.lower()
        NewMessage = []
        for letter in message:
            if letter in letters:
                NewMessage.append(letters[letter])
            else:
                NewMessage.append(letter)
        await ctx.reply(("").join(reversed(NewMessage)), mention_author=False)

    # fakeban
    @commands.command(no_pm=True)
    async def fakeban(self, ctx, member: discord.Member):
        await ctx.message.delete()
        await ctx.send(f"{member.mention}, Tao ban mày khỏi máy chủ này! gUwUd bye")


# ===========================================================

def setup(client):
    client.add_cog(Fun(client))
    