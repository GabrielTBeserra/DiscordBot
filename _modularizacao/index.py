# Python 3.6+ only
from Data.Token import TokenDiscord
import discord
import os

from pathlib import Path
from os import listdir
from discord.ext import commands

#Intents para permitir determinadas ações (Precisa ser hablitada no painel de desenvolvedor do discord)
intents = discord.Intents.default()
intents.members = True
intents.reactions = True
intents.messages = True

# Link que aparece como se estivesse jogando algo
game = discord.Game("ALGUM_LINK")

# Define o profixo do BOT e tambem a informações carregada nele quando esta online (Rich presence)
bot = commands.Bot(command_prefix="<3",
                   case_insensitive=True, intents=intents)
bot.change_presence(status=discord.Status.online, activity=game)


@bot.event
async def on_ready():
    print('Bot logado usando a tag: {0.user}'.format(bot))

# Responsavel por carregar os modulos de acordo com as pastas
if __name__ == "__main__":
    for fou in listdir('./modulos/'):
        for cmd in listdir(f'./modulos/{fou}'):
            if cmd.endswith('.py'):
                try:
                    bot.load_extension(f'modulos.{fou}.{cmd.split(".")[0]}')
                    print(f"Modulo {cmd.split('.')[0]} carregado! ✅")
                except Exception as exce:
                    print(
                        f"\nFalha no carregamento do modulo {type(exce).__name__}!\n{exce} ❌")


bot.run(tokenDiscord.uploadToken()['token'])