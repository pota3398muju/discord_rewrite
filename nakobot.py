import discord
TOKEN = 'NTA0Njg4ODA5ODQ2NTA1NDcz.XYzHgQ.2pqbM7tfQnUk9Ydzg-cunbx03LY'
client = discord.Client():

@client.event
async def on_ready():

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '！なこ':
        await message.channel.send('ウホウホ')
	
client.run(TOKEN)
