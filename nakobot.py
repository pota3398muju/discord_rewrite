import discord
import random
TOKEN = 'NTA0Njg4ODA5ODQ2NTA1NDcz.XY4pmg.-EFncjcsXRH1CGnTflTmN3x1UoY'
client = discord.Client()


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == "！なこ":
        kaiwa =["ウホウホッ！","おはなっこおおおお","なにいってんだこいつ","寝てた！！！","なこを崇めよ"]
        choose = random.choice(kaiwa)
        await message.channel.send(choose)

client.run(TOKEN)
