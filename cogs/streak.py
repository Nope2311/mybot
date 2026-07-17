import config
import json
import time 
import random
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
        channel_streak = ctx.guild.get_channel(1526890780420210838)
        
        s3_role = ctx.guild.get_role(config.S3_ROLE)
        s10_role = ctx.guild.get_role(config.S10_ROLE)
        s30_role = ctx.guild.get_role(config.S30_ROLE)
        s100_role = ctx.guild.get_role(config.S100_ROLE)
        s150_role = ctx.guild.get_role(config.S150_ROLE)

        chat = ["Tuyệt!","Nhắn vào hôm sau để tiếp tục nhé!","Ngon!"]
        chat_random = random.choice(chat)

        data = config.load_json()
        user_id = str(ctx.author.id)

        config.add_user(data=data,user_id=user_id) # add user


        if(current - data[user_id]["last_time_mess"] >= 86400):  # reset tin nhan sau 24 ke tu lan cuoi
            data[user_id]["message_today"] = 0 
            data[user_id]["today_mess_allow"] = True

        if (data[user_id]["Streak"] > 0):
            if (current - data[user_id]["last_time_streak"] >= 90000 ):
                data[user_id]["Streak"] = 0
                await ctx.author.remove_roles(s3_role, s10_role, s30_role, s100_role, s150_role)

        data[user_id]["message_today"] += 1 # cong 1 tin nhan 

        if (data[user_id]["today_mess_allow"] or data[user_id]["Streak"] == 0):  # nhan gia tri lan cuoi cua reset tin nhan 
            data[user_id]["Streak"] += 1
            if user_id in config.warning_send_message:
                try:
                    await config.warning_send_message[user_id].delete()
                except: pass
                del config.warning_send_message[user_id]
            if data[user_id]["Streak"] == 1:
                await channel_streak.send(f"[🔥] {ctx.author.mention} đã bắt đầu Streak : `{data[user_id]['Streak']}`.{chat_random}")
            elif data[user_id]["Streak"] > 1:
                await channel_streak.send(f"[🔥] {ctx.author.mention} đã duy trì Streak : `{data[user_id]['Streak']}`.{chat_random}")

            data[user_id]["last_time_mess"] = current
            data[user_id]["last_time_streak"] = current
            data[user_id]["today_mess_allow"] = False

        if data[user_id]["Streak"] >= 150:
            if s150_role not in ctx.author.roles:
                await ctx.author.add_roles(s150_role)
                await channel_streak.send(f"⚡ VỊ THẦN XUẤT HIỆN, **{ctx.author.name}** bay phấp phới, quá khủng khiếp với **150+ Streak Role**!")
        elif data[user_id]["Streak"] >= 100:
            if s100_role not in ctx.author.roles:
                await ctx.author.add_roles(s100_role)
                await channel_streak.send(f"🔥 WOW, **{ctx.author.name}** tiến đến con số 100 ngày và bú **100 Streak Role**!")
        elif data[user_id]["Streak"] >= 30:
            if s30_role not in ctx.author.roles:
                await ctx.author.add_roles(s30_role)
                await channel_streak.send(f"🔥 Tuyệt! **{ctx.author.name}** đã gặt hái **30 Streak Role**!")
        elif data[user_id]["Streak"] >= 10:
            if s10_role not in ctx.author.roles:
                await ctx.author.add_roles(s10_role)
                await channel_streak.send(f"🎉 Tiến xa hơn 1 chút với **10 Streak Role**! Chúc mừng {ctx.author.name}")
        elif data[user_id]["Streak"] >= 3:
            if s3_role not in ctx.author.roles:
                await ctx.author.add_roles(s3_role)
                await channel_streak.send(f"🎉 Chúc mừng **{ctx.author.name}** đã đạt được **3 Streak Role**!")
                embed3 = discord.Embed(color=discord.Color.random())
                embed3.set_image(url="https://cdn.discordapp.com/attachments/1454481372549873767/1527325915338506350/Comp_1.gif")

                await channel_streak.send(embed=embed3)

        config.save_json(data=data)

            



async def setup(bot: commands.Bot):
    await bot.add_cog(Streak(bot))
    


    
        
    
