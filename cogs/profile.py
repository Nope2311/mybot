import discord
import json
import config
from datetime import datetime, timezone


from discord.ext import commands
from discord import app_commands


data = config.load_json()


class Profile(commands.Cog):
    def __init__ (self, bot : commands.Bot):
        self.bot = bot
    
    @app_commands.command()
    async def profile(self,inter : discord.Interaction, member : discord.Member | None = None):
        if member is None:
            member = inter.user 

        user_id = str(member.id)
        current = datetime.now().timestamp()

        def format_time(seconds):
            if seconds >= 3600:
                return f"{seconds // 3600} giờ"
            elif seconds >= 60:
                return f"{seconds // 60} phút"
            return f"{seconds}s"
        
        data = config.load_json()

        config.add_user(data=data,user_id=user_id)
        
        config.save_json(data)

        

        streak = data[user_id]["Streak"]
        klt_coins = data[user_id]["KLT"]
        boDem = format_time(round(current - data[user_id]["last_time_streak"]))

        boDem_current = str(boDem) if (data[user_id]["last_time_streak"] != 0) or (data[user_id]["last_time_mess"] != 0) else "Chưa cập nhật"

        emoji_streak = config.streak_emoji_change(streak)

        emoji_check_message =  config.VERIFY if (data[user_id]["message_today"] >= config.MAX_MESSAGE) else config.CROSS
        mess_check_plus = str(data[user_id]["message_today"]) if (data[user_id]["message_today"] <= 100) else "100+"

        pf_embed = discord.Embed(title=f"🎃「 Hồ Sơ Côɴɢ Dâɴ 」",
                                  description="Những dấu ấn bạn đã tạo nên trong cuộc hành trình tại máy chủ.",
                                    color=0xFF0000)
        pf_embed.set_author(name=member.display_name, icon_url=member.display_avatar.url)
        pf_embed.add_field(name=f"{emoji_streak} Streaks :",
                           value=f"`{streak}`",inline=True)
        pf_embed.add_field(name=f"{config.COINS} Coins : ",
                           value=f"`{klt_coins} KLT`",inline=True)
        pf_embed.add_field(name=f"{emoji_check_message} Tin nhắn đã gửi : ",
                           value=f"`{mess_check_plus} / {config.MAX_MESSAGE} `",inline=True)
        pf_embed.add_field(name=f"⌚ Bộ đếm chuỗi trong ngày : ",
                    value=f"`{boDem_current}`",inline=True)
        
        pf_embed.timestamp = datetime.now(timezone.utc)

        await inter.response.send_message(embed=pf_embed,ephemeral=False)

async def setup(bot : commands.Bot):
    await bot.add_cog(Profile(bot))


