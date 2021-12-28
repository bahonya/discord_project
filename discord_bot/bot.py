import os
import random
import asyncio
import discord

from discord.ext import commands
from dotenv import load_dotenv
from leonicornswap.leonicornswap import Leonicornswap

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
bot.add_cog(Leonicornswap(bot))
vote_in_progress = False
users_in_channel = []
votes = {}


@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll_dice(ctx, number_of_dice=1, number_of_sides=6):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='roll', help='Roll random number.')
async def roll(ctx, range_left=0, range_right=101):
    roll_number = str(random.choice(range(range_left, range_right)))
    await ctx.send(roll_number)

@bot.command(name='list_online', help='List online members')
async def list_online(ctx):
    users_dict = {}
    for user in ctx.guild.members:
        if user.status != discord.Status.offline:
            await ctx.send(user.name+"#"+user.discriminator)


            
async def voting_time():
    await asyncio.sleep(60)
    global vote_in_progress
    vote_in_progress = False

    

async def vote(ctx, target):

    global vote_in_progress 
    global users_in_channel
    current_voice_channel = ctx.author.voice.channel
    users_in_channel = current_voice_channel.members
    user = discord.utils.get(bot.get_all_members(), name=target)

    if vote_in_progress:
        await ctx.send('Vote is already in progress')
    else:
        vote_in_progress = True
        done, pending = await asyncio.wait(
            [voting_time()], return_when=asyncio.FIRST_COMPLETED)
        await ctx.send(f'Vote has ended')

@bot.command(name='y', help='Vote for something')
async def vote_for(ctx):
    global users_in_channel
    global vote_in_progress
    if vote_in_progress:
        if ctx.author in users_in_channel:
            if ctx.author not in votes.keys():
                votes[ctx.author] = 1
                await ctx.send('Your vote has been accepted')
            else:
                await ctx.send(f'{ctx.author}, you have already voted')
        else:
            await ctx.send(f'{ctx.author},you can not vote since you were in another channel when vote was called')
    else:
        await ctx.send('Vote is not in progress')

@bot.command(name='n', help='Vote against something')
async def vote_against(ctx):
    global users_in_channel
    global vote_in_progress
    if vote_in_progress == True:
        if ctx.author in users_in_channel:
            if ctx.author not in votes.keys():
                votes[ctx.author] = 0
                await ctx.send('Your vote has been accepted')
            else:
                await ctx.send(f'{ctx.author}, you have already voted')
        else:
            await ctx.send(f'{ctx.author},you can not vote since you were in another channel when vote was called')
    else:
        await ctx.send('Vote is not in progress')

@bot.command(name='votekick', help='Vote for kicking someone')
async def votekick(ctx, target):
    global vote_in_progress
    global users_in_channel
    current_voice_channel = ctx.author.voice.channel
    users_in_channel = current_voice_channel.members
    user = discord.utils.get(bot.get_all_members(), name=target)
    if user in users_in_channel:
        if vote_in_progress==False:
            await ctx.send(f'Vote for kicking {target} from the voice channel has started')
            #kick someone if he got >75% of votes  
            await vote(ctx, target)
            if sum(votes.values())/len(votes.values()) >= 0.75:
                if len(votes)>1:
                    votes.clear()
                    await user.edit(voice_channel=None)
                    await ctx.send(f'{user.name} was kicked')
                else:
                    votes.clear()
                    await ctx.send(f'More than 1 vote required in order to kick')
            else:
                votes.clear()
                users_in_channel.clear()
        else:
            await ctx.send(f'Vote is already in progress')
    else:
        await ctx.send('You can kick someone from the voice channel only if the victim is in the same voice channel with you')

@bot.command(name='voteprogress', help='Vote for kicking someone')
async def votekick(ctx):
    global vote_in_progress
    await ctx.send(vote_in_progress)

@bot.command(name='usersinvoicechannel', help='Vote for kicking someone')
async def list_users_in_channel(ctx):
    current_voice_channel = ctx.author.voice.channel
    users_in_channel = current_voice_channel.members
    await ctx.send(users_in_channel)

@votekick.error
async def user_not_found_error(ctx, error):
    if isinstance(error, commands.errors.CommandInvokeError):
        await ctx.send('I could not find that member...')



bot.run(TOKEN)



