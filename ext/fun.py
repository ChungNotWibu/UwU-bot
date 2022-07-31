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