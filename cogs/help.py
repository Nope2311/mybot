import discord
from discord import app_commands
from discord.ext import commands 


class Help(commands.Cog):
    def __init__(self,bot : commands.Bot):
        self.bot = bot
    
    @app_commands.command()
    async def help(self ,inter : discord.Interaction):
        help_embed = discord.Embed(title="「 TRỢ GIÚP LỆNH 」",
                               description="\n",
                               color=0xFF0000)
        help_embed.add_field(name="**/profile**", value="Xem thông tin hồ sơ về thành viên.",inline=False)
        
        await inter.response.send_message(embed=help_embed,ephemeral=False)

    

async def setup(bot: commands.Bot):
    await bot.add_cog(Help(bot))
    