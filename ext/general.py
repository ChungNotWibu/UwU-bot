
from ast import arg
from re import A
import discord
from discord.ext import commands
import googletrans
from googletrans import Translator


# ===========================================================

# ==========snipe===========
snipe_message_author = {}
snipe_message_content = {}
# ==========================


class Command(commands.Cog):

    def __init__(self, client):
        self.client = client

    # command general
    # ping
    @commands.command()
    async def ping(self, ctx):
        if round(self.client.latency * 1000) <= 50:
            embed = discord.Embed(
                title="PONG", description=f":ping_pong: Pingpongpingpong! Ping là **{round(self.client.latency *1000)}** ms-milliseconds !", color=0x44ff44)
        elif round(self.client.latency * 1000) <= 100:
            embed = discord.Embed(
                title="PONG", description=f":ping_pong: Pingpongpingpong! Ping là **{round(self.client.latency *1000)}** ms-milliseconds !", color=0xffd000)
        elif round(self.client.latency * 1000) <= 200:
            embed = discord.Embed(
                title="PONG", description=f":ping_pong: Pingpongpingpong! Ping là **{round(self.client.latency *1000)}** ms-milliseconds !", color=0xff6600)
        else:
            embed = discord.Embed(
                title="PONG", description=f":ping_pong: Pingpongpingpong! Ping là **{round(self.client.latency *1000)}** ms-milliseconds !", color=0x990000)
        await ctx.send(embed=embed)

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
                title=f"Tin nhắn cuối cùng bị xóa trong #{channel.name}", description=snipe_message_content[channel.id],color=ctx.author.color)
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
        embed.set_author(name=f"Thông tin người dùng - {user}"),
        embed.set_thumbnail(url=user.avatar_url),
        embed.set_footer(text=f'Yêu cầu bởi - {ctx.author}',icon_url=ctx.author.avatar_url)
        embed.add_field(name='Tên:', value=user.display_name, inline=False)
        embed.add_field(name='Được khởi tạo vào:',value=user.created_at, inline=False)
        embed.add_field(name='Tham gia vào:', value=user.joined_at, inline=False)
        embed.add_field(name=f'Vai trò:({len(rlist)})',value=''.join([b]), inline=False)
        embed.add_field(name='Top vai trò:',value=user.top_role.mention, inline=False)
        await ctx.send(embed=embed)

    # invite
    @commands.command()
    async def invite(self, ctx):
        masked_link_embed = discord.Embed(
            title ='Invite',            
            description = '**[Mời bot vào server của bạn](https://discord.com/api/oauth2/authorize?client_id=996777600775098428&permissions=309237663744&scope=bot)**',
            color = discord.Colour.teal()
        )
        await ctx.message.channel.send(embed=masked_link_embed)

    # say
    @commands.command()
    async def say(self, ctx, *, text):
        await ctx.message.delete()
        await ctx.send(f"{text}")

    # help
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
        color=0xffa8ff,timestamp=ctx.message.created_at
        )
        embed.set_footer(text=f'Yêu cầu bởi {ctx.author}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Help',value='Trợ giúp cho bạn')
        embed.add_field(name='Prefix',value='`uwu`',inline=False)
        embed.add_field(name='General',value='`snipe`, `ping`, `whois`, `serverinfo`, `invite`, `avatar`', inline=False)
        embed.add_field(name='Fun',value='`fakeban`, `roll`, `say`, `usd(upsidedown) [letter]`', inline=False)
        embed.add_field(name='Tictactoe',value='`tictactoe`, `place [number 1-9]`, `end` ', inline=False)   
        embed.add_field(name='Mod',value='`kick`,`ban`,`shutdown[only ADMIN]`',inline=False)
        await ctx.message.channel.send(embed=embed)

    # serverinfo
    @commands.command(no_pm=True)
    async def serverinfo(self, ctx,):
        embed = discord.Embed(timestamp=ctx.message.created_at,colour=0x44ff44)
        guild = ctx.message.guild
        embed.set_footer(text=f'Yêu cầu bởi {ctx.author}', icon_url=ctx.author.avatar_url)
        embed.set_author(name=str(guild), icon_url=guild.icon_url)
        embed.add_field(name="Khởi tạo vào:", value=str(guild.created_at.strftime("%d-%m-%Y at %H:%M")))
        embed.add_field(name='ID:', value=ctx.guild.id, inline=False)
        embed.add_field(name="Số member:", value=str(guild.member_count))
        embed.add_field(name="Số vai trò:", value=str(len(guild.roles)))
        embed.add_field(name="Số kênh:", value=str(len(guild.channels)))
        embed.add_field(name="Số kênh tin nhắn:", value=str(len(guild.text_channels)))
        embed.add_field(name="Số kênh thoại:", value=str(len(guild.voice_channels)))
        embed.add_field(name="Só danh mục:", value=str(len(guild.categories)))
        await ctx.message.channel.send(embed=embed)

    # avatar user
    @commands.command()
    async def avatar(self, ctx, *,  avamember: discord.Member=None):
        if avamember == None:
          avamember = ctx.author
        embed1 = discord.Embed(
            colour=avamember.color,title = f"Ảnh đại diện của{avamember.name}",timestamp=ctx.message.created_at
        )
        embed1.set_image(url=avamember.avatar_url)
        embed1.set_footer(text='Yêu cầu bởi:' + ctx.author.name,icon_url = ctx.author.avatar_url)
        await ctx.send(embed=embed1)
    
    # translate
    # @commands.command()
    # async def translate(ctx, lang, *,args):
    #     t = Translator()
    #     a = t.translate(args, dest=lang)
    #     await ctx.send(a.text)

    # shutdown
    @commands.command()
    async def shutdown(self, ctx):       
        id = str(ctx.author.id)
        if id == '747465114512261185':
            await ctx.send('Bot đang tắt ỤnU!')
            await ctx.bot.logout()       
        else:
            await ctx.send("UwU bạn không có quyền thực hiện hành động này!")

def setup(client):
    client.add_cog(Command(client))
