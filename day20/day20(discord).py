import json
import discord
from discord.ext import commands
import dotenv
import os
import random
import asyncio
dotenv.load_dotenv()

token = os.getenv("BOT_API")
intents = discord.Intents.default()
intents.message_content = True

def load():
    try:
        with open("data/data.json", "r") as f:
            return json.load(f)
    except:
        return {}
def save(data):
    with open("data/data.json", "w") as f:
        json.dump(data, f)



bot = commands.Bot(command_prefix="!", intents=intents)
starting_data = {

}
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Requested command failed: wait {round(error.retry_after, 1)}s")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel is not None:
        await channel.send(f"Welcome {member.name}!")
    base_stats = {
        "coins": 100,
        "xp": 0,
        "level": 1,
        "stats": {
            "wins": 0,
            "losses": 0
        }
    }
    data = load()
    data[str(member.id)] = base_stats
    save(data)
    try:
        await member.send("👋 Welcome to the server!")
        await asyncio.sleep(2)
        await member.send("💰 You start with coins. Use !balance to check them and use !mine to get more.")
        await asyncio.sleep(2)
        await member.send("🎲 Try !roll (max_num) (amount of dice) to roll dice.")
        await asyncio.sleep(2)
        await member.send("🎮 You can do Rock, Paper, Scissors using !rps (r, p, or s). If you win, you get double your money. If you lose, you lose 5% of your money. If you draw, You get 20 coins.")
        await member.send("⚔️ Have fun!")
    except:
        pass


@bot.command()
@commands.cooldown(1, 3, commands.BucketType.guild)
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def roll(ctx, number: int = 6, times: int = 1):
    for i in range(times):
        result = random.randint(1, number)
        await ctx.author.send("You rolled a " + str(result) + ".")
        if i != times - 1:
            await asyncio.sleep(1)

@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def mine(ctx):
    data = load()
    data[str(ctx.author.id)]["coins"] += 20
    save(data)
    try:
        await ctx.author.send("Gained +20 Coins!")
    except:
        await ctx.send("I couldn't DM you 😢")


@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def reset_data(ctx):
    data = load()
    base_stats = {
        "coins": 100,
        "xp": 0,
        "level": 1,
        "stats": {
            "wins": 0,
            "losses": 0
        }
    }
    data[str(ctx.author.id)] = base_stats
    save(data)

@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def balance(ctx):
    data = load()
    try:
        await ctx.author.send(f"Your balance is {data[str(ctx.author.id)]['coins']}!")
    except:
        await ctx.send("I couldn't DM you 😢")

@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def rps(ctx, choice = "r"):
    bot_choice = random.choice(["r", "p", "s"])
    data = load()
    if choice == bot_choice:
        await ctx.send(f"{ctx.author} went against the bot in Rock Paper Scissors and drew! ({choice} vs {bot_choice})")
    elif (choice == "r" and bot_choice == "p") or (choice == "p" and bot_choice == "s") or (choice == "s" and bot_choice == "r"):
        await ctx.send(f"{ctx.author} went against the bot in Rock Paper Scissors and lost! ({choice} vs {bot_choice})")
        data[str(ctx.author.id)]["stats"]["losses"] += 1
        save(data)
    elif (choice == "r" and bot_choice == "s") or (choice == "p" and bot_choice == "r") or (choice == "s" and bot_choice == "p"):
        await ctx.send(f"{ctx.author} went against the bot in Rock Paper Scissors and won! ({choice} vs {bot_choice})")
        data[str(ctx.author.id)]["stats"]["wins"] += 1
        save(data)

@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def wins(ctx):
    data = load()
    try:
        await ctx.author.send(f"You've won {data[str(ctx.author.id)]["stats"]["wins"]} times!")
    except:
        await ctx.send("I couldn't DM you 😢")

@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def losses(ctx):
    data = load()
    try:
        await ctx.author.send(f"You've lost {data[str(ctx.author.id)]["stats"]["losses"]} times!")
    except:
        await ctx.send("I couldn't DM you 😢")

@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def pay(ctx, user_id = 1451944204329812164, amount = 1):
    data = load()
    if data[str(ctx.author.id)]["coins"] >= amount:
        data[str(ctx.author.id)]["coins"] -= amount
        try:
            data[str(user_id)]["coins"] += amount
            await ctx.send(f"{ctx.author} paid the user with the id: {user_id}, {amount} coins.")
        except:
            await ctx.author.send(f"The person who this user id belongs to has not played this game before. Get them to join first.")
    else:
        await ctx.author.send("You don't have enough coins to pay!")

@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def get_id(ctx):
    await ctx.author.send(f"Your user id is: {ctx.author.id}. Use it when getting others to donate to you.")

bot.run(token)