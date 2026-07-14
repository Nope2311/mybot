import discord
import config
from datetime import datetime 
from discord.ext import commands
from discord import app_commands

class ModCommands(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot
    
    @app_commands.default_permissions(administrator=True)
    @app_commands.command()
    async def backup(self,inter : discord.Interaction):
        config.backup_active = True
        await inter.response.send_message("Đã backup, check <#1454336025076699301> để xem!")

    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    @commands.command()
    async def lock(self, mess : discord.Message):
        guild = self.bot.get_guild(1454336025076699301)
        role_member = guild.get_role(1464795756010541118)
        channel = mess.channel.overwrites_for(role_member)
        channel.send_messages = False
        channel.send_messages_in_threads = False
        channel.add_reactions = False
        channel.use_application_commands = False
        channel.create_private_threads = False
        channel.create_private_threads = False

        await mess.channel.set_permissions(role_member,overwrite=channel)
        await mess.channel.send("☑️ ĐÃ LOCK KÊNH!")

    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    @commands.command()
    async def unlock(self, mess : discord.Message):
        guild = self.bot.get_guild(1454336025076699301)
        role_member = guild.get_role(1464795756010541118)
        channel = mess.channel.overwrites_for(role_member)
        channel.send_messages = True
        channel.send_messages_in_threads = True
        channel.add_reactions = True
        channel.use_application_commands = True
        channel.create_private_threads = True
        channel.create_private_threads = True

        await mess.channel.set_permissions(role_member,overwrite=channel)
        await mess.channel.send("☑️ ĐÃ UNLOCK KÊNH!")
  
    @backup.error
    async def on_error(self,inter : discord.Interaction, error):
        if isinstance(error,app_commands.MissingPermissions):
            await inter.response.send_message("Bạn không có quyền!")
        if isinstance(error,app_commands.BotMissingPermissions):
            await inter.response.send_message("Bot không có quyền!")
    
async def setup(bot : commands.Bot):
    await bot.add_cog(ModCommands(bot))
        
