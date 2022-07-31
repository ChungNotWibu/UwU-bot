
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

    # command general
    # ping
    @commands.command()
    async def ping(self, ctx):
        if round(self.client.latency * 1000) <= 50:
            embed = discord.Embed(
                title="PONG", description=f":ping_pong: Pingpongpingpong! The ping is **{round(self.client.latency *1000)}** ms-milliseconds !", color=0x44ff44)
        elif round(self.client.latency * 1000) <= 100:
            embed = discord.Embed(
                title="PONG", description=f":ping_pong: Pingpongpingpong! The ping is **{round(self.client.latency *1000)}** ms-milliseconds !", color=0xffd000)
        elif round(self.client.latency * 1000) <= 200:
            embed = discord.Embed(
                title="PONG", description=f":ping_pong: Pingpongpingpong! The ping is **{round(self.client.latency *1000)}** ms-milliseconds !", color=0xff6600)
        else:
            embed = discord.Embed(
                title="PONG", description=f":ping_pong: Pingpongpingpong! The ping is **{round(self.client.latency *1000)}** ms-milliseconds !", color=0x990000)
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
        embed.set_footer(text=f'Requested by - {ctx.author}',icon_url=ctx.author.avatar_url)
        embed.add_field(name='ID:', value=user.id, inline=False)
        embed.add_field(name='Name:', value=user.display_name, inline=False)
        embed.add_field(name='Created at:',value=user.created_at, inline=False)
        embed.add_field(name='Joined at:', value=user.joined_at, inline=False)
        embed.add_field(name='Bot?', value=user.bot, inline=False)
        embed.add_field(name=f'Roles:({len(rlist)})',value=''.join([b]), inline=False)
        embed.add_field(name='Top Role:',value=user.top_role.mention, inline=False)
        await ctx.send(embed=embed)

    # invite
    @commands.command()
    async def invite(self, ctx):
        masked_link_embed = discord.Embed(
            title ='Invite',            
            description = '**[Invite Bot into your server](https://discord.com/api/oauth2/authorize?client_id=996777600775098428&permissions=309237663744&scope=bot)**',
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
        embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Help',value='Help for you')
        embed.add_field(name='Prefix',value='`uwu`',inline=False)
        embed.add_field(name='General',value='`snipe`, `ping`, `whois`, `serverinfo`, `invite`, `avatar`', inline=False)
        embed.add_field(name='Fun',value='`ban`, `roll`, `say`, `usd(upsidedown) [letter]`', inline=False)
        embed.add_field(name='Tictactoe',value='`tictactoe`, `place [number 1-9]`, `end` ', inline=False)   
        await ctx.message.channel.send(embed=embed)

    # serverinfo
    @commands.command(no_pm=True)
    async def serverinfo(self, ctx):
        """General info about the server."""
        embed = discord.Embed()
        guild = ctx.message.guild
        embed.set_author(name=str(guild), icon_url=guild.icon_url)
        embed.add_field(name="Created at:", value=str(guild.created_at.strftime("%d-%m-%Y at %H:%M")))
        embed.add_field(name="Member Count:", value=str(guild.member_count))
        embed.add_field(name="Role Count:", value=str(len(guild.roles)))
        embed.add_field(name="Channel Count:", value=str(len(guild.channels)))
        embed.add_field(name="TextChannel Count:", value=str(len(guild.text_channels)))
        embed.add_field(name="VoiceChannel Count:", value=str(len(guild.voice_channels)))
        embed.add_field(name="Catergory Count:", value=str(len(guild.categories)))
        await ctx.message.channel.send(embed=embed)

    # avatar user
    @commands.command()
    async def avatar(self, ctx, *,  avamember: discord.Member=None):
        if avamember == None:
          avamember = ctx.author
        embed1 = discord.Embed(
            colour=avamember.color,title = f"{avamember.name}'s avatar",timestamp=ctx.message.created_at
        )
        embed1.set_image(url=avamember.avatar_url)
        embed1.set_footer(text='Requested by:' + ctx.author.name,icon_url = ctx.author.avatar_url)

        await ctx.send(embed=embed1)

def setup(client):
    client.add_cog(Command(client))
