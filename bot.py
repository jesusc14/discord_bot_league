import discord
import os
import requests

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print("I'am ready")


@client.event
async def on_message(message):
    print(message.content)
    if message.author == client.user:
        return

    if message.content.startswith("sa"):
        await message.channel.send("as")
        return

    if message.content.startswith("!bored"):
        response = requests.get("http://www.boredapi.com/api/activity/")
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Retrieve the activity from the response
            activity = response.json()

            # Create a formatted message with the activity information
            activity_message = f"Here's something you can do!\n"
            activity_message += f"Activity: {activity['activity']}\n"
            activity_message += f"Type: {activity['type']}\n"
            activity_message += f"Participants: {activity['participants']}\n"
            activity_message += f"Price: {activity['price']}\n"
            activity_message += f"Accessibility: {activity['accessibility']}"

            # Send the message
            await message.channel.send(activity_message)
        else:
            # If the request was not successful, print the status code
            print(f"Error: {response.status_code}")


client.run("MTExOTY5MzY0MDY1OTM3ODI5Nw.Gk8f7M.t-tWVmPAXGKPxEis7joTW1vyq_ADntOIXqLWAk")
