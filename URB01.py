import os
import discord
import random
import asyncio

from discord.ext.commands import Bot

TOKEN = 'NzAwNDY5OTM3MDI1NTgxMTI2.Xpja6w.Ofi6lm59wjpWWEjQWBMCFnZ1o5E'

bot = Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("URB01 is online and ready for duty!")

@bot.event
async def member_join_dm(member):
    welcome_dm = '''Hello and welcome to The Fram! This is just an attempt to bring together all of the gaming
groups MYB01 is a part of. That's rather selfish sounding now that I think about it . . . Anyhow. Feel free to
mute the channels you're not involved in and enjoy!'''
    await member.dm_channel.send(member, welcome_dm)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
        
    if "siege" in message.content or "rainbow six" in message.content:
        r6_op_quotes = ["Remember, I'll take the doors.", "Stay clear of the blast!", "I see I've got your heart racing.",
                    "You can stop worrying about grenades now!", "Device primed, keep an eye on door.",
                    "Pest out! Godspeed, little fella.", "Remember: We are the hunters, they are the prey.",
                    "Every trail leads to death. So is yours.", "Just remember: only two people in the world can get this job done. I'm one of them.",
                    "Now you see me, now you don't", "Brave, smart, or lucky - you will still die.",
                    "A really big fucking hole coming right up!"]
        ops = random.choice(r6_op_quotes)
        await message.channel.send(ops)
        
    if message.content.endswith('dumb'):
        await message.channel.send(f'no u')
    
    if message.content == "no u":
        await message.channel.send(f"Don't kid yourself")
        
    if message.content.startswith('!purpose'):
        purpose = ["Trolling", "I don't know", "Shitposting, mainly", "Being as unhelpful as possible"]
        response = random.choice(purpose)
        await message.channel.send(response)
        
    if "parachut" in message.content or ("warzone" in message.content and "play" in message.content):
        await message.channel.send(f'Remember: Press A to deploy parachute')
        
    if message.content.lower() == "what is the answer to the ultimate question of life, the universe, and everything?":
        await message.channel.send(f'42')
    
    if message.content.startswith('shrug'):
        await message.channel.send(f'¯\_(ツ)_/¯')
    
    await bot.process_commands(message)
        
@bot.command(pass_content=True)
async def hello(ctx):
    await ctx.send(f'Hello!')
    
@bot.command(pass_content=True)
async def test(ctx):
    await ctx.send(f'Working!')
    
@bot.command(pass_content=True)
async def ping(ctx):
    await ctx.send(f"Pong")

bot.run(TOKEN)