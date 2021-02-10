import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient


bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Bot is ready!")


@bot.command()
async def ping1(ctx):
    mongo_url = "mongodb+srv://admin:clubpenguin888@newdb-dxsvu.mongodb.net/new?retryWrites=true&w=majority"
    cluster = MongoClient(mongo_url)
    db = cluster["databasel"]
    collection = db["new"]

    ping_cm = {"command": 1}
    collection.insert_one(ping_cm)

    await ctx.channel.send("Ping has been registered")


with open("token.txt", "r") as f:
    lines = f.readlines()
    token = lines[0].strip()

bot.run(token)
