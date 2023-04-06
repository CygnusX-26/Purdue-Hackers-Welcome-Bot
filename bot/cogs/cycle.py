import sqlite3
import discord
from discord.ext import commands
from discord import app_commands
import emoji
import random

def is_emoji(s):
    return s in emoji.EMOJI_DATA

class Cycle(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
            
    #help command
    @app_commands.command(name= 'cycle', description = 'Cycles the channel emoji')
    @app_commands.checks.has_permissions(manage_channels=True)
    async def cycle(self, interaction: discord.Interaction) -> None:
        current_emoji = interaction.channel.name[:1]
        possible_emojis = ["⚡", "💛","😶","💪","🐮","🟨","🐻","☢️","🌝","🌛","🌜","🌚","🐉","🐌","🗣️","👁️"]
        new_emoji = random.choice(possible_emojis)
        while(new_emoji == current_emoji):
            new_emoji = random.choice(possible_emojis)
        try:
            if (is_emoji(current_emoji)):
                await interaction.channel.edit(name = new_emoji + interaction.channel.name[1:])
            else:
                await interaction.channel.edit(name = new_emoji + interaction.channel.name)
            await interaction.response.send_message("Channel emoji cycled!")
        except discord.errors.HTTPException:
            await interaction.response.send_message("We are being ratelimited!")


async def setup(bot: commands.Bot):
    await bot.add_cog(Cycle(bot))