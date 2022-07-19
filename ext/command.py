
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

    #hello&bye
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == 'hello':
            await message.channel.send('Hewro UwU')
        if message.content == 'bye':
            await message.channel.send(f'UwU Goodbye {message.author}')

 
#  ===================================================================================================
    #counting server
    # @commands.Cog.listener()
    # async def on_ready(self):
    #     server_count = 0
    #     for guild in self.guilds:
	# 	        print(f"- {guild.id} (name: {guild.name})")
    #         server_Count = server_count + 1
    #     print("UwU Bot is in  " + str(server_count) + " server.")

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

#    =================================================================================================== 
    
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
