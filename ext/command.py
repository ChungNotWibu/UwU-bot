
from ast import Global, parse
from cgi import test
from datetime import datetime
from dis import dis
from distutils.log import error
from glob import glob
from itertools import count
from operator import not_
import re
from tokenize import Name
from turtle import title
from unicodedata import name
from urllib.request import Request
from aiohttp import request
import discord
from discord.ext import commands
from discord.utils import get
from hikari import Guild
# ===========================================================

# ==========snipe===========
snipe_message_author = {}
snipe_message_content = {}
# ==========================



class Command(commands.Cog):

    def __init__(self, client):
        self.client = client

    #event
    #status&bot_ready
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.idle, activity=discord.Game('uwu help'))
        print('Bot ready!!!')

    #Answer
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == 'hello':
            await message.channel.send('Hewro ◕‿◕')
        if message.content == 'bye':
            await message.channel.send(f'UwU Goodbye {message.author}')
        if message.content == 'mom':
            await message.channel.send(f'UwU {message.author} mom taste good like night')
        if message.content == 'daddy':
            await message.channel.send('what do u need son, money or me ( ͡° ͜ʖ ͡°) uwu')
        if message.content == 'primogems':
            await message.channel.send('such a pain ụnu')
        if message.content == 'good night':
            await message.channel.send(f'sweet dream UwU {message.author}')
        if message.content == 'uwu':
            await message.channel.send('UwU')

#  ===================================================================================================

    #member count
    # @commands.Cog.listener
    # async def on_member_join(self, member):
    #     guild = member.guild
    #     channel = get(guild.channels, name = test)
    #     await channel.edit(name = f'Member Count: {guild.member_count}')

    # @commands.Cog.listener
    # async def on_member_remove(self, member):
    #     guild = member.guild
    #     channel = get(guild.channels, name = test)
    #     await channel.edit(name = f'Member Count: {guild.member_count}')

#  =================================================================================================== 
    

    #command
    #ping
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms ')

    #snipe
    
    @commands.Cog.listener()    
    async def on_message_delete(self, message):
        snipe_message_author[message.channel.id]= message.author
        snipe_message_content[message.channel.id]= message.content
        
    @commands.command() 
    async def snipe(self, ctx):       
        channel = ctx.channel
        try:
            snipeEmbed = discord.Embed(title=f"Tin nhắn cuối cùng bị xóa trong #{channel.name}", description = snipe_message_content[channel.id]) 
            snipeEmbed.set_footer(text=f'Xóa bởi {snipe_message_author[channel.id]}')
            await ctx.send(embed= snipeEmbed)
        except:
            await ctx.send(f'Không có tin nhắn đã xóa trong #{channel.name}')    

    #whois
    @commands.command(name="whois")
    async def whois(self, ctx,user:discord.Member=None):
        if user==None:
            user=ctx.author
        rlist = []
        for role in user.roles:
            if role.name != "@everyone":
                rlist.append(role.mention)
        b = ", ".join(rlist)

        embed = discord.Embed(colour=user.color,timestamp=ctx.message.created_at)
        embed.set_author(name=f"User Info - {user}"),
        embed.set_thumbnail(url=user.avatar_url),
        embed.set_footer(text=f'Requested by - {ctx.author}',
        icon_url=ctx.author.avatar_url)
        embed.add_field(name='ID:',value=user.id,inline=False)
        embed.add_field(name='Name:',value=user.display_name,inline=False)
        embed.add_field(name='Created at:',value=user.created_at,inline=False)
        embed.add_field(name='Joined at:',value=user.joined_at,inline=False)
        embed.add_field(name='Bot?',value=user.bot,inline=False)
        embed.add_field(name=f'Roles:({len(rlist)})',value=''.join([b]),inline=False)
        embed.add_field(name='Top Role:',value=user.top_role.mention,inline=False)
        await ctx.send(embed=embed)    


def setup(client):
    client.add_cog(Command(client))       
