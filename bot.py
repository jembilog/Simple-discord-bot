import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Important for reading messages

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("👋 Hello! I'm your simple Discord bot.")

@bot.command()
async def helpme(ctx):
    help_text = "**Available Commands:**\n"
    help_text += "`!hello` - Greet the bot\n"
    help_text += "`!helpme` - Show this help message\n"
    help_text += "`!about` - Learn about the bot"
    await ctx.send(help_text)

@bot.command()
async def about(ctx):
    await ctx.send("🤖 I am a Python-based Discord bot built for fun and learning!")

# Replace with your bot token
bot.run("YOUR_BOT_TOKEN_HERE")
