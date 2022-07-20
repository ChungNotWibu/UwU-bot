
from ast import parse
from cgi import test
from datetime import datetime
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

snipe_message_author = {}
snipe_message_content = {}

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
            await message.channel.send('Hewro UwU')
        if message.content == 'bye':
            await message.channel.send(f'UwU Goodbye {message.author}')
        if message.content == 'mom':
            await message.channel.send(f'UwU {message.author} mom taste good like night')
        if message.content == 'daddy':
            await message.channel.send('what do u need son, money or me uwu')
        if message.content == 'primogems':
            await message.channel.send('such a pain ụnu')
        if message.content == 'good night':
            await message.channel.send(f'sweet dream UwU {message.author}')

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





def setup(client):
    client.add_cog(Command(client))       
