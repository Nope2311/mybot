import discord
import config
from discord.ext import commands
from discord import app_commands

class ModCommands(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @app_commands.default_permissions(administrator=True)
    @app_commands.command()
    async def backup(inter : discord.Interaction):
        config.backup_active = True
    
async def setup(bot : commands.Bot):
    await bot.add_cog(ModCommands(bot))
        
