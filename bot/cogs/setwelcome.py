import discord
from discord.ext import commands
from discord import app_commands
import os

class ChannelList(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @app_commands.command(name= 'sendwelcome', description = 'sends the welcome message')
    @app_commands.checks.has_permissions(manage_channels=True)
    async def setwelcome(self, interaction: discord.Interaction) -> None:
        await interaction.channel.send(file=discord.File("purduehackers.png"))
        await interaction.channel.send("_ _")
        await interaction.channel.send("Hey, welcome to the  **Official Purdue Hackers** discord server! The best way for hackers to work together, meet other hackers, and have fun! :yellow_heart:")
        await interaction.channel.send("We are a community of students who collaborate, learn and build kick-ass technical projects.")
        await interaction.channel.send("_ _")
        embed = discord.Embed(
            title = "So what do we do here?",
            description= "As a member of **Purdue Hackers**, you can attend **Purdue Hackers** events such as workshops and __Hack Night__, meet other hackers, learn new skills, and share all your projects with the community. :partying_face: ",
            color = 0x2f3136
        )
        embed2 = discord.Embed(
            title = "What are workshops?",
            description = "Workshops are a great way to learn new skills and meet other hackers. We host workshops on a variety of topics, from beginner-friendly to advanced. :nerd: You can find the schedule for upcoming workshops as well as past workshops on our [website](https://www.purduehackers.com/). :calendar:",
            color = 0x2f3136
        )
        embed3 = discord.Embed(
            title = "What is Hack Night?",
            description = "Hack Night is a weekly event where you can work on your projects with other hackers. :new_moon_with_face: We have people available to help you with your projects and answer any questions you may have. :cloud_lightning: Hack Nights happen every Friday, and there should be an announcement with details about the event! :zap: There is also a super secret bot that only appears during Hack Night which allows you to share your projects with everyone! :robot:",
            color = 0x2f3136
        )
        embed4 = discord.Embed(
            title = "Where can I share my progress and finished projects?",
            description = "You can share your in progress projects in the :sailboat: sail channel, and your finished projects in the :ferry: ship channel!",
            color = 0x2f3136
        )
        embed5 = discord.Embed(
            title = "How do I get started?",
            description = "To get started, you first need to read the rules, which can be found below. :scroll: Remember to check out the announcements channel for important updates and events! :loudspeaker:",
            color = 0x2f3136
        )
        embed6 = discord.Embed(
            title = "Rules",
            description="The rules serve to create a safe and welcoming environment for everyone. Please read them carefully. :eyes:",
            color = 0x2f3136
        )
        embed6.add_field(name="1. Be civil and respectful.", value="Absolutely no harassment, witch hunting, sexism, racis, or hat speech will be tolerated. :no_entry_sign:", inline=False)
        embed6.add_field(name="2. Dont spam", value="This includes excessive pings, excessive emojis, and excessive messages.", inline=False)
        embed6.add_field(name="3. No NSFW content", value="This includes any content that is sexually explicit, violent, or otherwise inappropriate.", inline=False)
        embed6.add_field(name="4. No advertising", value="This includes advertising other servers, products, or services.", inline=False)
        embed6.add_field(name="5. Use common sense", value="The organizers have the final say on any interpretation of misconduct.", inline=False)
        embed6.add_field(name="6. Have fun!", value="This is a community for hackers to meet and collaborate. :partying_face:", inline=False)
        view = Menu()
        await interaction.channel.send(embed=embed)
        await interaction.channel.send(embed=embed2)
        await interaction.channel.send(embed=embed3)
        await interaction.channel.send(embed=embed4)
        await interaction.channel.send(embed=embed5)
        await interaction.channel.send(embed=embed6, view=view)
    
    @setwelcome.error
    async def setwelcome_error(self, interaction: discord.Interaction, error: Exception) -> None:
        if isinstance(error, commands.MissingPermissions):
            await interaction.response.send_message("You don't have permission to use this command.")
        else:
            raise error

class Menu(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
    
    @discord.ui.button(label="Accept Rules", style=discord.ButtonStyle.blurple)
    async def rules(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name="Purdue Hackers"))
        await interaction.response.send_message("You have been given the Purdue Hackers role! Have fun! :yellow_heart:", ephemeral=True)

    @discord.ui.button(label="Shh", style=discord.ButtonStyle.danger)
    async def shh(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(Shh())


class Shh(discord.ui.Modal, title="???"):
    sec1 = discord.ui.TextInput(
        style=discord.TextStyle.short,
        placeholder="???",
        label="Hack Night",
        required=True
    )
    sec2 = discord.ui.TextInput(
        style=discord.TextStyle.short,
        placeholder="???",
        label="Website",
    )
    sec3 = discord.ui.TextInput(
        style=discord.TextStyle.short,
        placeholder="???",
        label="Sail",
    )
    sec4 = discord.ui.TextInput(
        style=discord.TextStyle.short,
        placeholder="???",
        label="Workshop",
    )
    async def on_submit(self, interaction: discord.Interaction) -> None:
        if (self.sec1.value == os.getenv("HACKNIGHT")) and (self.sec2.value == os.getenv("WEBSITE")) and (self.sec3.value == os.getenv("SAIL")) and (self.sec4.value == os.getenv("WORKSHOP")):
            #nice try looking at source code :)
            await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name="Dedicated Hacker"))
            await interaction.response.send_message("You have been given the Dedicated Hacker role! :yellow_heart: Hope you had fun on this little hunt!", ephemeral=True)
            await interaction.guild.get_channel(1037508176901320756).send(f"{interaction.user.mention} has found the secret role! :tada:")


async def setup(bot: commands.Bot):
    await bot.add_cog(ChannelList(bot))