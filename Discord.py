import discord
from discord.ext import commands
import random 
import os 
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')   

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
            #В переменную кладём файл, который преобразуется в файл библиотеки Discord!
            picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def garbage(ctx):
    await ctx.send("Мусор - главный враг человечества! Многие люди скорее выкидывают его просто на улицу чем в мусорники! Но этому есть решение, если вы будете собирать летом мусор на пляжах и в лесу компаниями то скорее всего вы сможете очистить большое количество мусора!))))")

@bot.command()
async def helpme(ctx):
    await ctx.send('''Вот что ты можешь у меня спросить: Про мусор и его уничтожение - garbage, 
покажет тебе рандомный мем с уткой - duck, 
покажет тебе рандомный мем про программирование - mem, 
если напишешь это и имя человека то покажеться кто зашёл в группу - joined, 
можешь написать любое слово после этого и написать число повтора - repeat, 
напишеться это столько раз сколько напишешь - heh, 
бот тебя поприветствует - hello.''')

bot.run("your code")
