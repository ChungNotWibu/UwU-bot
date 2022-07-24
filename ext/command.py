
import discord
from discord.ext import commands
# ===========================================================

# ==========snipe===========
snipe_message_author = {}
snipe_message_content = {}
# ==========================



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



    #command
    #ping
    @commands.command()
    async def ping(self, ctx):
        if round(self.client.latency * 1000) <= 50:
            embed=discord.Embed(title="PONG", description=f":ping_pong: Pingpongpingpong! The ping is **{round(self.client.latency *1000)}** ms-milliseconds !", color=0x44ff44)
        elif round(self.client.latency * 1000) <= 100:
            embed=discord.Embed(title="PONG", description=f":ping_pong: Pingpongpingpong! The ping is **{round(self.client.latency *1000)}** ms-milliseconds !", color=0xffd000)
        elif round(self.client.latency * 1000) <= 200:
            embed=discord.Embed(title="PONG", description=f":ping_pong: Pingpongpingpong! The ping is **{round(self.client.latency *1000)}** ms-milliseconds !", color=0xff6600)
        else:
            embed=discord.Embed(title="PONG", description=f":ping_pong: Pingpongpingpong! The ping is **{round(self.client.latency *1000)}** ms-milliseconds !", color=0x990000)
        await ctx.send(embed=embed)


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

    #whois
    @commands.command(name="whois")
    async def whois(self, ctx,user:discord.Member=None):
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




def setup(client):
    client.add_cog(Command(client))       
