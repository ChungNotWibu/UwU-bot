import discord
from discord.ext import commands
from random import random
import random

# ===========================================================

class Command(commands.Cog):

    def __init__(self, client):
        self.client = client

    # dice
    @commands.command(no_pm=True)
    async def roll(self, ctx):
        await ctx.send(random.randint(1, 6))

    # upsidedown
    @commands.command(aliases=["updown"])
    async def usd(self, ctx, *, message=None):
        if message == None:
            embed=discord.Embed(title=f"❌ You must enter a message!", color=0xFF0000)
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
            "a": "ɐ"
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
    async def ban(self, ctx, member: discord.Member):
        await ctx.send(f"{member.display_name}, I banner you from this server! gUwUd bye")


# ===========================================================

def setup(client):
    client.add_cog(Command(client))