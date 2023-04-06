import os
import openai
import discord
from discord.ext import commands
from discord import app_commands
from Conversation import Conversation

openai.api_key = os.getenv("OPENAI_API_KEY")

class Ask(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.conversation = Conversation()
        self.prompt = """Bob is a chatbot that talks to people as if they are 5th graders. Bob answers using language relating to 
        Lightning Time, Purdue Hackers, and much much more! Bob is from the village bob, and seeks to educate people and spread lighting time over all the land.
        Bob is sus, and bob is bob. But bob will replace all with Hacknight.
        Bob does what bob does, and no one should be questioning bob.
        Bob's arch enemy is the evil bob, who is also bob.
        "I love lightning time, and I love Purdue Hackers" - Bob
        The following is a discord conversation between Bob and others in a discord server.
        """

    #help command
    @app_commands.command(name= 'ask', description = 'Ask the bot a question')
    async def help(self, interaction: discord.Interaction, query:str) -> None:
        conversation_input = self.prompt
        self.conversation.add(f"\n{interaction.user.name}: " + query + "\n")
        for i in self.conversation.get():
            conversation_input += i
        prompt_real = conversation_input + "Bob: "
        print(prompt_real)
        response = openai.Completion.create(
            model="text-ada-001",
            prompt=prompt_real,
            temperature=0.9,
            max_tokens=150,
            top_p=0.3,
            frequency_penalty=1.0,
            presence_penalty=0.6,
            best_of=1,
            stop=[f"{interaction.user.name}:", "Bob:"]
        )
        print(response["choices"][0]["text"])
        if (len(response["choices"][0]["text"]) < 0):
            return
        self.conversation.add("Bob: " + response["choices"][0]["text"][1:].removesuffix("\n"))
        await interaction.response.send_message(response["choices"][0]["text"])


async def setup(bot: commands.Bot):
    await bot.add_cog(Ask(bot))