import discord
from discord.ext import commands

TOKEN = "NzE2NDI5NDk4OTc0OTk0NTAy.XtLpOg.7alH4NHgvuARYQPIawmWXf9DzK" + "w"

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_message(message):
    
       if message.content.startswith('!talk'):

        ctx = message.channel
        
        message = (message.content)[6:]

        await ctx.send(message)

bot.run(TOKEN)
