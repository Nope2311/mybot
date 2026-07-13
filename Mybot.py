import asyncio
import config
import discord
import os
from flask import Flask
from threading import Thread
from discord.ext import commands
from discord import app_commands

TOKEN = os.getenv("TOKEN")

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

def run_web():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

Thread(target=run_web).start()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.load_extension("cogs.profile")
    await bot.load_extension("cogs.streak")
    await bot.load_extension("cogs.help")

    synced = await bot.tree.sync()
    print(f"so command da dc thuc thi {len(synced)}")

@bot.tree.command()
async def spam(inter : discord.Interaction, amount : int, noidung : str):
    if amount > 36 : 
        await inter.response.send_message("Tối đa 36 tin nhắn!",ephemeral=True) 
        return
    
    await inter.response.defer(thinking=False,ephemeral=True)
    
    for i in range(0,amount):
        await inter.channel.send(noidung)
        
    await inter.edit_original_response(content="Xong!")
    await asyncio.sleep(5)
    await inter.delete_original_response()

@bot.tree.command()
async def embed(inter : discord.Interaction ,msg : str,dogay: int):
    embed = discord.Embed(title= "abc", description= msg, color=0xBBFF00)
    embed.set_thumbnail(url ="https://klipy.com/gifs/elmo-D7c")
    embed.set_image(url ="https://klipy.com/gifs/elmo-D7c")
    embed.set_footer(text="memaybeo",icon_url="https://klipy.com/gifs/elmo-D7c")

    embed.add_field(name="ownergaycac",value=f"do gay : {dogay}%",inline=True)
    embed.add_field(name="ownergaycac",value=f"do cac : {dogay}%",inline=True)

    await inter.response.send_message(embed=embed)

@bot.tree.command()
@app_commands.checks.has_permissions(manage_messages=True)
@app_commands.checks.bot_has_permissions(manage_messages=True)
async def clear(inter : discord.Interaction ,amount : int):
    await inter.response.defer(thinking=True,ephemeral=True)
    await inter.channel.purge(limit= amount)
    await inter.followup.send(content=f"Đã xóa {amount} tin nhắn!",ephemeral=True)
    
@clear.error
async def on_error(inter : discord.Interaction, error):
    if isinstance(error, app_commands.MissingPermissions):
        await inter.response.send_message("Mày làm ddeeck có quyền")
    elif isinstance(error, app_commands.BotMissingPermissions):
        await inter.response.send_message("Bot làm ddeeck có quyền")


    
bot.run(TOKEN)

