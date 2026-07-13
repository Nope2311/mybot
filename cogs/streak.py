import config
import json
import time 
from datetime import datetime

import discord
from discord import app_commands
from discord.ext import commands



class Streak(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, ctx : discord.Message):
        current = datetime.now().timestamp()  

        if ctx.author.bot : return
        if ctx.guild is None : return

        data = config.load_json()
        user_id = str(ctx.author.id)

        config.add_user(data=data,user_id=user_id) # add user



        if(current - data[user_id]["last_time_mess"] >= 86400):  # reset tin nhan sau 24 ke tu lan cuoi
            data[user_id]["message_today"] = 0 
            data[user_id]["today_mess_allow"] = True

        if (data[user_id]["Streak"] > 0):
            if (current - data[user_id]["last_time_streak"] >= 86400):
                data[user_id]["Streak"] = 0
                user = await self.bot.fetch_user(int(user_id))
                await user.send(f"Bạn đã mất chuỗi trong Edit & Meme, hãy bắt đầu trò truyện lại hoặc khôi phục lại chuỗi!")
                

        data[user_id]["message_today"] += 1 # cong 1 tin nhan 

        if (data[user_id]["today_mess_allow"]):  # nhan gia tri lan cuoi cua reset tin nhan 
            data[user_id]["Streak"] += 1
            if data[user_id]["Streak"] == 1:
                await ctx.reply(f"**{ctx.author.name}** đã bắt đầu Streak! \nCheck tại `/profile`")
            elif data[user_id]["Streak"] > 1:
                await ctx.reply(f"**{ctx.author.name}** đã duy trì Streak! \nCheck tại `/profile`")

            data[user_id]["last_time_mess"] = current
            data[user_id]["last_time_streak"] = current
            data[user_id]["today_mess_allow"] = False

        config.save_json(data=data)
            



async def setup(bot: commands.Bot):
    await bot.add_cog(Streak(bot))
    


    
        
    