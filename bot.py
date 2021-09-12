import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.reactions = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_raw_reaction_add(payload):
    if payload.member.bot:
        pass
    else:
        message_id = payload.message_id
        if message_id == 886468971317043231:
            member = payload.member
            guild = member.guild

            print(f'This is the ADDED emoji name: {payload.emoji.name}')

            if payload.emoji.name == '💜':
                role = discord.utils.get(guild.roles, name='they•them')
            else:
                role = None

            if role is not None and member is not None:
                await member.add_roles(role)
                print(f'Gave \'{member.name}\' the role \'{role}\'')

@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 886468971317043231:
        guild = await(client.fetch_guild(payload.guild_id))
        member = await(guild.fetch_member(payload.user_id))

        print(f'This is the ADDED emoji name: {payload.emoji.name}')

        if payload.emoji.name == '💜':
            role = discord.utils.get(guild.roles, name='they•them')
        else:
            role = None

        if role is not None and member is not None:
            await member.remove_roles(role)
            print(f'Removed \'{member.name}\' the role \'{role}\'')

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

client.run(TOKEN)