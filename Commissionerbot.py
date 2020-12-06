# CommissionerBot 0.1.0

# This bot will auto assign roles when a user reacts to a message with an emoji
# Console output will display the role and the username it is assigned to

import os
import discord
from dotenv import load_dotenv

load_dotenv()
client = discord.Client()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
MESSAGE = int(os.getenv("MESSAGE_ID"))
CHANNEL = int(os.getenv("CHANNEL_ID"))


# Check to make sure bot has connected to the server
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            print(
                f"{client.user} has connected to Discord!\n\n"
                f"{client.user} is connected to the following guild(s):\n"
                f"{guild.name} (id: {guild.id})\n"
            )
            break


# Add role by selecting emoji
@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == MESSAGE:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        if payload.emoji.name == 'fry':
            role = discord.utils.get(guild.roles, name='Memes')
            print(f"{role} selected")
        elif payload.emoji.name == 'beaker':
            role = discord.utils.get(guild.roles, name='Scientist')
            print(f"{role} selected")
        elif payload.emoji.name == 'philosophy':
            role = discord.utils.get(guild.roles, name='Philosopher')
            print(f'{role} selected')
        elif payload.emoji.name == 'mind':
            role = discord.utils.get(guild.roles, name='Character Building')
            print(f'{role} selected')
        elif payload.emoji.name == 'd20':
            role = discord.utils.get(guild.roles, name='Table Top')
            print(f'{role} selected')
        elif payload.emoji.name == 'pawn':
            role = discord.utils.get(guild.roles, name='Chess Master')
            print(f'{role} selected')
        elif payload.emoji.name == 'dice':
            role = discord.utils.get(guild.roles, name='Board Games')
            print(f'{role} selected')
        elif payload.emoji.name == 'minecraft':
            role = discord.utils.get(guild.roles, name='Minecraft')
            print(f'{role} selected')
        elif payload.emoji.name == 'controller':
            role = discord.utils.get(guild.roles, name='Console Gamer')
            print(f'{role} selected')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = payload.member
            await member.add_roles(role)
            print(f"{role} assigned to {member}\n")
        else:
            print("No role assigned.")


client.run(TOKEN)
