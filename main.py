from http import client
import discord
from discord.ext import commands
import os

# ======================================================================================

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

# ======================================================================================

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


@client.event
async def on_ready():
    guild_count = 0
    for guild in client.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        guild_count = guild_count + 1
    print("UwU Bot is in " + str(guild_count) + " guilds.")




# ======================================================================================

@client.command(name="whois")
async def whois(ctx,user:discord.Member=None):
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
  
# ======================================================================================








client.run('OTk2Nzc3NjAwNzc1MDk4NDI4.GX1uTb.kZxpYO8Pzpm8OUpufwFC_aOHTNMeazG_SaHMaA')


