import discord
from discord.ext import commands
import settings

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def yavuzhan(ctx):
    await ctx.send(f'Merhaba! Ben Yavuzhan Phyton Pro Öğrencisiyim.')

@bot.command()
async def yardim(ctx):
    await ctx.send(f'$hello\n$he\n$yavuzhan\n$yardim')

bot.run(settings.TOKEN) #Bot token burada olmalıdır.
