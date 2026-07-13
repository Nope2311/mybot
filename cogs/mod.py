import discord
from discord.ext import commands
from discord import app_commands

class ModCommands(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    
        