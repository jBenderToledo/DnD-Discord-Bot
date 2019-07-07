import random
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
client = discord.Client()

@bot.command()
async def ping(ctx):
    await ctx.send('PONG!')

@bot.command(name = 'exit')
async def shutdown(ctx):
    exit()

@bot.command(name = 'rps')
async def rock_paper_scissors(ctx, arg):
    results = ['ROCK!', 'PAPER!' 'SCISSORS!']
    winner_text = ["A tie!", "I lose...", "I win!", "what?"]
    answer_map = {'rock':0, 'paper':1, 'scissors':2}
    bot_choice = random.randint(0, 3)
    arg = arg.lower()

    if arg != 'rock' and arg != 'paper' and arg != 'scissors':
        await ctx.send(winner_text[3])
        return

    player_choice = answer_map[arg]
    final_result = (player_choice - bot_choice) % 3

    await ctx.send(winner_text[final_result])
    pass

###

@client.event
async def on_ready(self):
    await ctx.send("Gendo online!")
    print(self.User, "has connected!")
    
    pass



###

bot.run('NDE5ODY3ODg5ODYwODcwMTU1.XSEIKA.6ELiv3wmu1BoB8ZURU8M4zWrlNk') # original token do not steel 
