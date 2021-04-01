import discord
from discord.ext import commands

class Ola(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Essa descrições aparecem no comando de HELP padrão da API
    @commands.command(brief='Uma breve Descrição do comando' , description='Descrição completa')
    async def ola(self , ctx , *args):
        await ctx.send(f'<@{ctx.author.id}> Ola!')

def setup(bot):
    bot.add_cog(Ola(bot))
