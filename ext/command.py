
import discord
from discord.ext import commands
from discord.utils import get
import random
# ===========================================================

# ==========snipe===========
snipe_message_author = {}
snipe_message_content = {}
# ==========================


class Command(commands.Cog):

    def __init__(self, client):
        self.client = client

    # event
    # status&bot_ready
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.idle, activity=discord.Game('uwu help'))
        print('Bot ready!!!')

    # Answer
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
        if message.content == 'oni-chan baka':
            await message.channel.send('anh hai là đồ óc chó óc chó')
        if message.content == 'damn':
            await message.channel.send('em ơi lâu đài tình ái đó')
        if message.content == 'yasuo':
            await message.channel.send('hasagi mà ko vào ko phải hảo hán')
        if message.content == 'sus':
            await message.channel.send('amogus ඞ')

#  ===================================================================================================

    # member count
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

    # command
    # ping

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms ')

    # snipe

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        snipe_message_author[message.channel.id] = message.author
        snipe_message_content[message.channel.id] = message.content

    @commands.command()
    async def snipe(self, ctx):
        channel = ctx.channel
        try:
            snipeEmbed = discord.Embed(
                title=f"Tin nhắn cuối cùng bị xóa trong #{channel.name}", description=snipe_message_content[channel.id])
            snipeEmbed.set_footer(
                text=f'Xóa bởi {snipe_message_author[channel.id]}')
            await ctx.send(embed=snipeEmbed)
        except:
            await ctx.send(f'Không có tin nhắn đã xóa trong #{channel.name}')

    # whois
    @commands.command(name="whois")
    async def whois(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        rlist = []
        for role in user.roles:
            if role.name != "@everyone":
                rlist.append(role.mention)
        b = ", ".join(rlist)

        embed = discord.Embed(
            colour=user.color, timestamp=ctx.message.created_at)
        embed.set_author(name=f"User Info - {user}"),
        embed.set_thumbnail(url=user.avatar_url),
        embed.set_footer(text=f'Requested by - {ctx.author}',
                         icon_url=ctx.author.avatar_url)
        embed.add_field(name='ID:', value=user.id, inline=False)
        embed.add_field(name='Name:', value=user.display_name, inline=False)
        embed.add_field(name='Created at:',
                        value=user.created_at, inline=False)
        embed.add_field(name='Joined at:', value=user.joined_at, inline=False)
        embed.add_field(name='Bot?', value=user.bot, inline=False)
        embed.add_field(name=f'Roles:({len(rlist)})',
                        value=''.join([b]), inline=False)
        embed.add_field(name='Top Role:',
                        value=user.top_role.mention, inline=False)
        await ctx.send(embed=embed)


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


@commands.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0
        player1 = p1
        player2 = p2

        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn (๑˃̵ᴗ˂̵)ﻭ.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn (๑˃̵ᴗ˂̵)ﻭ.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one uwu.")


@commands.command()
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
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

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


def setup(client):
    client.add_cog(Command(client))
