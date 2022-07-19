
from turtle import title
import discord
from discord.ext import commands

snipe_message_author = {}
snipe_message_content = {}

class Command(commands.Cog):

    def __init__(self, client):
        self.client = client

    #event
    #status
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.idle, activity=discord.Game('uwu help'))
        print('Bot ready!!!')

    #hello
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == 'hello':
            await message.channel.send('Hewro UwU')
        if message.content == 'bye':
            await message.channel.send(f'UwU Goodbye {message.author}')
    
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
