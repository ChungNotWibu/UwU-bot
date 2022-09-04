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
    print("UwU Bot trong " + str(guild_count) + " server.")

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
            await ctx.send("Đến lượt của <@" + str(player1.id) + "> (๑˃̵ᴗ˂̵)ﻭ.")
        elif num == 2:
            turn = player2
            await ctx.send("Đến lượt của <@" + str(player2.id) + "> (๑˃̵ᴗ˂̵)ﻭ.")
    else:
        await ctx.send("❌ Trò chơi vẫn đang trong quá trình thực hiện! Làm ơn hoàn thành nó trước khi bắt đầu 1 ván mới uwu.")


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
                    await ctx.send(mark + "Chúc mừng <@" + str(player1.id) + "> đã chiến thắng! (/◕ヮ◕)/ ヽ(^o^)/")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("(゜o゜) Hòa rồi ! Bạn muốn chơi lại ván mới chứ ? ")

                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Đảm bảo chọn một số nguyên từ 1 đến 9 (vd: uwu place 1).")
        else:
            await ctx.send("❌ Không phải lượt của bạn ¯\_(ツ)_/¯")
    else:
        await ctx.send("Làm ơn hãy bắt đầu trò chơi bằng lệnh `uwu tictactoe` .")


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
        title='Trò chơi kết thúc', 
        description = 'Trò chơi đã được khởi tạo lại UwU',   
        color= discord.Colour.green()      
    )
    await ctx.send(embed=embed)

    
     



@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Xin vui lòng đề cập đến 2 người chơi cho lệnh này.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Vui lòng đảm bảo đề cập đến người chơi / ping (ví dụ: <@996777600775098428>).")


@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Vui lòng nhập một vị trí bạn muốn đánh dấu.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Vui lòng đảm bảo nhập một số nguyên.")


# ======================================================================================

@client.command()
@commands.has_permissions(manage_roles=True)
async def kick(ctx, member:discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send (f'{member.mention} was kicked ụnu !')

@kick.error
async def kick_error(error, ctx):
    if isinstance(error, MissingPermissions):
        text = "❌ Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await client.send_message(ctx.message.channel, text)


@client.command()
@commands.has_permissions(manage_roles=True)
async def ban (ctx, member:discord.Member = None, *, reason=None):
    if member == None:
        await ctx.send("Bạn có thể vui lòng nhập một người dùng hợp lệ không? ÙwÚ")
        return
    try:
        await member.ban(reason=reason)
        await ctx.send (f'Thuck u ! Đã ban {member.mention} !')
    except Exception as error :
        if isinstance(error):
            await ctx.send("❌ Có vẻ như bạn không có quyền sử dụng lệnh này.")
        else:
            await ctx.send(error)

# @client.command()
# @commands.has_permissions()
# async def unban(ctx,*,member):
#     banned_users = await ctx.guild.bans()
#     member_name , member_discriminator = member.split('#')

#     for ban_entry in banned_users:
#         user = ban_entry.user

#         if (user.name, user.discriminator) == (member_name , member_discriminator):
#             await ctx.guild.unban(user)
#             await ctx.send(f'Unbanned {user.mention}!')
#             return





client.run('OTk2Nzc3NjAwNzc1MDk4NDI4.GX1uTb.kZxpYO8Pzpm8OUpufwFC_aOHTNMeazG_SaHMaA')



