from discord.ext import commands
from discord.ext import tasks
from leonicornswap.api_requests import get_price_pair


class Leonicornswap(commands.Cog):
    def __init__(self, bot):
        #self.printer.start()
        self.bot = bot
        self.colddown = 1

    def cog_unload(self):
        self.printer.cancel()

    @staticmethod
    def get_prices():
        pair = get_price_pair()
        message = f"""
Current prices for LEON and LEOS:
LEON - {pair[0]}
LEOS - {pair[1]}
TO THE MOON
        """
        return message

    @commands.command(name='leonicornswap', help='TO THE MOON')
    async def call_printer(self, ctx):
        await ctx.send(self.get_prices())
    
    #@commands.command(name='set_leonicornspam', help='Set task to send current LEON and LEOS prices, minimal colddown is 1 hour')
    #async def set_printer(self, ctx, colddown=1):
    #    #minimal colddown is 1 hour
    #    if colddown >= 1:
    #        @tasks.loop(hours=1)
    #        async def printer(self, channel):
    #            await channel.send(self.get_prices())
    #        await ctx.send(f"Leonicornspam was successfully set, colddown is {colddown} hour(s)")
    #    else:
    #        await ctx.send(f"Failed to set Leonicorn, minimal colddown is 1 hour")
