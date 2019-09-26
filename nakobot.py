# インストールした discord.py を読み込む
import discord
import random

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NTA0Njg4ODA5ODQ2NTA1NDcz.XYzHgQ.2pqbM7tfQnUk9Ydzg-cunbx03LY'

# 接続に必要なオブジェクトを生成
client = discord.Client()



# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '！なこ':
	random.uniform(0,3)
	if random.uniform == 0
        await message.channel.send('ウホウホ')
if random.uniform == 1
        await message.channel.send('おはなっこ！！！！！！')
if random.uniform == 2
        await message.channel.send('ふーん')
if random.uniform == 3
        await message.channel.send('腹筋われた！！！！！！！')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
