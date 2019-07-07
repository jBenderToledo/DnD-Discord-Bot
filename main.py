import random
import discord # Using Python 3.5
import sys
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

###

@bot.event
async def on_ready(self):
    await ctx.send("Gendo online!")
    print(self.User, "has connected!")
    
    pass

###

@bot.command()
async def ping(ctx):
    await ctx.send('PONG!')
    pass

@bot.command(name = 'exit')
async def shutdown(ctx):
    await ctx.send("Shutting down.")
    await logout()
    pass

@bot.command(name = 'rps')
async def rock_paper_scissors(ctx, arg):
    arg = arg.lower()
    
    results = ['Rock!', 'Paper!', 'Scissors!']
    winner_text = ["A tie.", "I win!", "I lose...", "what?"]
    answer_map = {'rock':0, 'paper':1, 'scissors':2}
    
    bot_choice = random.randint(0, 2)

    if arg != 'rock' and arg != 'paper' and arg != 'scissors':
        await ctx.send(winner_text[3])
        return

    player_choice = answer_map[arg]
    bot_choice = results[bot_choice]
    final_result = (bot_choice - player_choice) % 3

    await ctx.send(bot_choice + " " + winner_text[final_result])
    pass

###

if len(sys.argv) >= 2:
    bot.run(sys.argv[1]) # Take the second operand as the token
else:
    print("You need at least two operands to run this bot.")
    print("The structure is as follows:\n")
    print("python3", sys.argv[0], "<token>\n")
    print("This bot will NOT work otherwise!")

