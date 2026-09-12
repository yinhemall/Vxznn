import discord
import os
bot = discord.Bot()
@bot.slash_command(name="hello")
async def hello(ctx):
    await ctx.respond("Hi,im gay")
    token = os.getenv("DISCORD_TOKEN")
    @bot.event
    async def on_ready():
        print("✅")
    bot.run(token)