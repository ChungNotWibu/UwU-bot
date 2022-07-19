from http import client
import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix='uwu ', description='đang chạy thử nghiệm UwU')
client.remove_command('help')

@client.command()
async def load(ctx, extensions):
    client.load_extension(f'ext.{extensions}')

@client.command()
async def unload(ctx, extensions):
    client.unload_extension(f'ext.{extensions}')

@client.command()
async def reload(ctx, extensions):
    client.reload_extension(f'ext.{extensions}')

for filename in os.listdir('./ext'):
    if filename.endswith('.py'):
        client.load_extension(f'ext.{filename[:-3]}')

#help
@client.command(pass_context=True)
async def help(ctx):
        author = ctx.message.author
        embed = discord.Embed(
            colour = discord.Colour.orange()
        )
        embed.set_author(name="Help")
        embed.add_field(name="Bạn cần giúp j",value="prefix = uwu",inline=False)
        channel = await author.create_dm()
        await channel.send(author,embed=embed)
        await ctx.message.channel.send("Message sent to your DMs")















client.run('OTk2Nzc3NjAwNzc1MDk4NDI4.GX1uTb.kZxpYO8Pzpm8OUpufwFC_aOHTNMeazG_SaHMaA')


