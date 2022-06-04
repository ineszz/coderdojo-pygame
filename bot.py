import os
from discord.ext import commands

TOKEN = os.get
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

@bot.event
async def on_message(message):
    # Make sure the Bot doesn't respond to it's own messages
    if message.author == bot.user: 
        return
    
    if message.content == 'hello' or message.content == 'hi':
        await message.channel.send(f'Hi {message.author.mention}')
    if message.content == 'bye':
        await message.channel.send(f'Goodbye {message.author.mention}')
    # 
    if message.content.lower() == 'poza':
        await message.channel.send(f'https://media.giphy.com/media/TR0FU9ushLPUX9E6zQ/giphy.gif')


    await bot.process_commands(message)
token = os.environ.get("DISCORD_BOT_SECRET")
bot.run(TOKEN)
