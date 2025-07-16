import os
token = os.getenv("DISCORD_BOT_TOKEN")

import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

token = os.getenv("DISCORD_BOT_TOKEN")
if not token:
    print("❌ TOKEN ไม่ถูกตั้งค่า")
else:
    bot.run(token)
