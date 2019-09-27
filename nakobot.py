import discord
TOKEN = 'NTA0Njg4ODA5ODQ2NTA1NDcz.XY4Sgw.xqEsYGcnIJGjGHUtiRdkiBkTZuk'
client = discord.Client()


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == "！なこ":
        await message.channel.send("ウホウホッ！")

client.run(TOKEN)

