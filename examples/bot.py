import pteropy
import discord
import json
from discord.ext import commands
from discord import option

bot=discord.Bot()
class power(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="開始",
        style=discord.ButtonStyle.green,
        custom_id="awa:start",
    )
    async def start(self, button: discord.ui.Button, interaction: discord.Interaction):
        pass

    @discord.ui.button(
        label="重啟", style=discord.ButtonStyle.gray, custom_id="awa:restart"
    )
    async def restart(self, button: discord.ui.Button, interaction: discord.Interaction):
        pass

    @discord.ui.button(
        label="停止", style=discord.ButtonStyle.red, custom_id="awa:stop"
    )
    async def stop(self, button: discord.ui.Button, interaction: discord.Interaction):
        pass

    @discord.ui.button(
        label="強制停止", style=discord.ButtonStyle.red, custom_id="awa:kill"
    )
    async def kill(self, button: discord.ui.Button, interaction: discord.Interaction):
        pass
