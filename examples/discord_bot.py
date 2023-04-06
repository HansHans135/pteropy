import pteropy
import discord
#請使用pycord
import json
from discord.ext import commands
from discord import option
from pteropy import Pterodactyl_Client

base_url = "https://面板網址"
bot=discord.Bot()

class Power(discord.ui.View):
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

@bot.slash_command(description="綁定api")
@option("key", description="你的api key")
async def key(ctx,key:str):
    ptero = Pterodactyl_Client(base_url, key)
    try:
        ptero.list_servers()["errors"]
        await ctx.respond("無效的kpi key 請重新嘗試")
        return
    except:
        with open("key.json","r")as f:
            data=json.load(f)
        data[ctx.user.id]=key
        with open("key.json","w+")as f:
            json.dump(data,f)
        await ctx.respond("綁定成功")

@bot.slash_command(description="控制電源")
@option("server", description="你的主機編號")
async def power(ctx,server:str):
    with open("key.json","r")as f:
        data=json.load(f)
    try:
        ptero = Pterodactyl_Client(base_url, data[ctx.user.id])
    except:
        await ctx.respond("你還沒綁定")
        return
    if ptero.get_server(server) == None:
        await ctx.respond("沒有這個伺服器")
        return
    embed=discord.Embed(title="電源選項",description="正在控制"+server)
    await ctx.respond(content=server,embed=embed, view=Power())
bot.run("")
