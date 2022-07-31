import discord
from discord.ext import commands

# ===========================================================

class Event(commands.Cog):

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
            await message.channel.send('hasagi mà ko trăn trối ko phải hảo hán')
        if message.content == 'sus':
            await message.channel.send('amogus ඞ')



# ===========================================================

def setup(client):
    client.add_cog(Event(client))