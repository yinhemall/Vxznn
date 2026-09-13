import os
import discord
import asyncio
from discord.ext import commands
from datetime import timedelta
from discord import app_commands

token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=["!", "."], intents=intents)

@bot.event
async def on_ready():
    synced = await bot.tree.sync()
    print("✅")
    print(f"以同步 {len(synced)}個指令")

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

@bot.tree.command(name="ping")
async def ping(interaction: discord.Interaction):
        latency_ms = round(bot.latency * 1000)
        embed = discord.Embed(color=discord.Color.dark_gray())
        embed.description = f"# 🤖Bot Ping\n\n***ping:{latency_ms}ms***"
        embed.set_footer(text="-# 🛠️Made By Noxar")
        await interaction.response.send_message(embed=embed)

@bot.command()
async def kick(ctx, member):
     await member.kick()
     embed = discord.Embed(color=discord.Color.green())
     embed.description = f'# ✅THE USER HAS BEEN KICKED\n\n**{member.mention}has been kicked**'
     await ctx.send(embed=embed)

@kick.error
async def kick_error(ctx, error):
     if isinstance(error, discord.ext.commands.errors.MissingPermissions):
          embed = discord.Embed(color=discord.Color.red)
          embed.description = "# ❌Missing Permissions\n\n**You don't have the required permissions to use this command.**"
          await ctx.send(embed=embed)

     elif isinstance(error, discord.ext.commands.errors.BotMissingPermissions):
        embed = discord.Embed(color=discord.Color.red)
        embed.description = "❌BOT MISSING PERMISSIONS\n\n**Bot don't have the required permissions to use this command.**"
        await ctx.send(embed=embed)

     elif isinstance(error, commands.CommandInvokeError):
        embed = discord.Embed(color=discord.Color.red())
        embed.description = "# ❌FORBIDDEN\n\n**Bot's role might be lower than the user.**"
        await ctx.send(embed=embed)

     elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(color=discord.Color.red())
        embed.description = "# ❌MISSING REQUIRED ARGUMENT\n\n**Right Usage: .kick <@user>**"
        await ctx.send(embed=embed)

running = False
@bot.tree.command(name="n", description="Nuke inf")
@app_commands.user_install()
@app_commands.allowed_contexts(guilds = True, dms = True)
async def n(interaction: discord.Interaction):
    global running
    running = True
    await interaction.response.defer()

    while running:
               embed = discord.Embed(color=discord.Color.dark_gray())
               embed.description = "# 💀YOU'RE SERVER GOT NUKED\n\n# ☠️GG NIGGA\n\n# ☠️GG NIGGA\n\n# 🥵SUCK MY DICK NIGGA\n\n# ☠️GG NIGGA\n\n# ☠️GG NIGGA\n\n# 🥵SUCK MY DICK NIGGA\n\n# 🥀YOUR SERVER GOT NUKED\n\n# EZ"
               await interaction.followup.send(embed=embed)
               await asyncio.sleep(2)

@bot.tree.command(name="stop")
@app_commands.user_install()
@app_commands.allowed_contexts(guilds = True, dms = True)
async def stop(interaction: discord.Interaction):
    global running
    running = False
    embed = discord.Embed(color=discord.Color.green())
    embed.description = "# ✅STOPPES\n\n**The command has been stopped.**"
    await interaction.response.send_message(embed=embed)

@bot.command()
async def n(ctx):
     global running
     running = True
     while running:
              embed = discord.Embed(color=discord.Color.dark_gray())
              embed.description = "# 💀YOU'RE SERVER GOT NUKED\n\n# ☠️GG NIGGA\n\n# ☠️GG NIGGA\n\n# 🥵SUCK MY DICK NIGGA\n\n# ☠️GG NIGGA\n\n# ☠️GG NIGGA\n\n# 🥵SUCK MY DICK NIGGA\n\n# 🥀YOUR SERVER GOT NUKED\n\n# EZ"
              await ctx.send(embed=embed)
              await asyncio.sleep(2)

@bot.command() 
async def stop(ctx):
     global running
     running = False
     embed = discord.Embed(color=discord.Color.green())
     embed.description = "# ✅STOPPES\n\n**The command has been stopped.**"
     await ctx.send(embed=embed)
bot.run(token)