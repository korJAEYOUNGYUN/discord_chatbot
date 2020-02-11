import os

import discord
from dotenv import load_dotenv

import dialogflow_client


load_dotenv()
token = os.getenv('DISCORD_TOKEN')
google_project_id = os.getenv('GOOGLE_PROJECT_ID')
language_code = 'en-US'

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user or message.author.bot:
        return

    session_id = message.channel.guild.id + message.channel.id
    response_message = dialogflow_client.detect_intent_texts(
        google_project_id, session_id, message.content, language_code)

    await message.channel.send(response_message)


client.run(token)