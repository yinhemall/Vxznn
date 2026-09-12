import os
import discord
from discord.ext import commands
from datetime import timedelta

token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=["!", "."], intents=intents)

@bot.event
async def on_ready():
    print("✅")

@bot.command()
async def hello(ctx):
    embed = discord.Embed(color=discord.Color.blue())
    embed.title = "# 🥵『你好啊小騷逼』"
    embed.description = "**今天你晨勃了嗎?**\n\n-# 讓我看看"
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(moderate_members=True)
@commands.bot_has_permissions(moderate_members=True)
async def mute(ctx, member, minutes: int):
    member = ctx.message.mentions[0]
    duration = timedelta(minutes=minutes)

    print("mute已啟用")

    await member.timeout_for(duration)
    embed = discord.Embed(color=discord.Color.green())
    embed.description = f"# The user has been muted\n\n**{member.mention}has been muted for {minutes} minutes**"
    embed.set_footer(text="-# GG NIGGA")
    await ctx.send(embed=embed)

@mute.error
async def mute_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingPermissions):
          embed = discord.Embed(color=discord.Color.yellow())
          embed.description = "# ❌Missing Permissions\n\n**You don't have the required permissions to use this command.**"
          await ctx.send(embed=embed)

    elif isinstance(error, discord.ext.commands.errors.BotMissingPermissions):
          embed = discord.Embed(color=discord.Color.red())
          embed.description = "# ❌Bot Missing Permissions\n\n**Bot don't have the required permissions to use this command.**"
          await ctx.send(embed=embed)

    elif isinstance(error, commands.CommandInvokeError):
      if isinstance(error.original, discord.Forbidden):
         embed = discord.Embed(color=discord.Color.red())
         embed.description = "# ❌Forbidden\n\n**Bot's role might be lower than the user.**"
         await ctx.send(embed=embed)

    elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(color=discord.Color.red())
            embed.description = "# ❌MISSING ARGUMENT\n\n**Right Usage: .mute <@user> minutes**"
            await ctx.send(embed=embed)

@bot.slash_command(name="ping")
async def ping(cxt):
        latency = bot.latency
        latency_ms = round(latency * 1000)
        embed = discord.Embed(color=discord.Color.dark_gray())
        embed.description = f"# 🤖Bot Ping\n\n***ping:{latency_ms}ms***"
        embed.set_footer(text="-# 🛠️Made By Noxar")
        await cxt.respond(embed=embed)
bot.run(token)