import discord
from random import random
from discord.ext import commands
import os
import random
from discord.ext.commands import MissingPermissions

# ======================================================================================

client = commands.Bot(command_prefix='uwu ', help_command=None)
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
    else:
        print(f'Unable to load {filename[:-3]}')

# ======================================================================================

@client.event
async def on_ready():
    guild_count = 0
    for guild in client.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        guild_count = guild_count + 1
    print("UwU Bot is in " + str(guild_count) + " guilds.")

@client.event
async def on_message(message):
    message.author.guild_permissions.manage_messages
# ======================================================================================

# tictactoe
player1 = ""
player2 = ""
turn = ""
gameOver = True
board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


@client.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:",":white_large_square:",":white_large_square:",
                ":white_large_square:",":white_large_square:",":white_large_square:",
                ":white_large_square:",":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0
        player1 = p1
        player2 = p2

        line = ""
        for x in range(len(board)):
            if x == 3 or x == 6 : line = line + "\n"
            line += "" + board[x]
            if x == 8: await ctx.send(line)

        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn (๑˃̵ᴗ˂̵)ﻭ.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn (๑˃̵ᴗ˂̵)ﻭ.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one uwu.")


@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
                board[pos - 1] = mark
                count += 1

                line = ""
                for x in range(len(board)):
                    if x == 3 or x == 6 : line = line + "\n"
                    line += "" + board[x]
                    if x == 8: await ctx.send(line)

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " <@" + str(player1.id) + "> Wins! (/◕ヮ◕)/ ヽ(^o^)/")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("(゜o゜) Tie! Do you want to play again? ")

                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn ¯\_(ツ)_/¯")
    else:
        await ctx.send("Plz start a new game using the uwu tictactoe command.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@client.command()
async def end(ctx):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver
    
    count = 0
    player1 = ''
    player2 = ''
    gameOver = True
    embed = discord.Embed(
        title='End Game', 
        description = 'The game has been restart UwU',   
        color= discord.Colour.green()      
    )
    await ctx.send(embed=embed)

    
     



@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Plz mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Plz make sure to mention/ping players (ie. <@688534433879556134>).")


@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Plz enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Plz make sure to enter an integer.")


# ======================================================================================

@client.command(name="kick", pass_context=True)
@commands.has_permissions(manage_roles=True)
async def kick(ctx, member:discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send (f'{member.mention} was kicked ụnu !')

@kick.error
async def kick_error(error, ctx):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await client.send_message(ctx.message.channel, text)


@client.command()
@commands.has_permissions(manage_roles=True)
async def ban (ctx, member:discord.Member = None, *, reason=None):
    if member == None:
        await ctx.send("Could you please enter a valid user?")
        return
    try:
        await member.ban(reason=reason)
        await ctx.send (f'Thuck u ! Banned {member.mention} !')
    except Exception as error :
        if isinstance(error):
            await ctx.send("Looks like you don't have the permissions to use this command.")
        else:
            await ctx.send(error)

@client.command()
@commands.has_permissions()
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name , member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name , member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}!')
            return











client.run('OTk2Nzc3NjAwNzc1MDk4NDI4.GX1uTb.kZxpYO8Pzpm8OUpufwFC_aOHTNMeazG_SaHMaA')



