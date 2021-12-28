from discord.ext import commands
from discord.ext import tasks
from api_requests import get_price_pair


class Leonicornswap(commands.Cog, ctx):
    def __init__(self, bot):
        self.ctx = ctx
        self.printer.start()
        self.colddown = 1

    def cog_unload(self):
        self.printer.cancel()

    @tasks.loop(hours=1)
    async def printer(self):
        pair = get_price_pair()
        message = f"""
        Current prices for LEON and LEOS:
        LEON - {pair[0]}
        LEOS - {pair[1]}
        """
        await self.ctx.send(message)

    @bot.command(name='leonicornswap', help='TO THE MOON')
    async def print_pairs(self) -> str:
        pair = get_price_pair()
        message = f"""
        Current prices for LEON and LEOS:
        LEON - {pair[0]}
        LEOS - {pair[1]}
        TO THE MOON!
        """
        await self.ctx.send(message)
