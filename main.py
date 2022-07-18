from http import client
import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix='uwu ')

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

















client.run('OTk2Nzc3NjAwNzc1MDk4NDI4.GX1uTb.kZxpYO8Pzpm8OUpufwFC_aOHTNMeazG_SaHMaA')


