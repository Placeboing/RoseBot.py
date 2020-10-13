from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase

PREFIX = "rpy "
OWNER_IDS = [619595472733995009]


class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()
        super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS)

        def run(self):
            pass

        async def on_connect(self):
            print("RoseBot.py is online.")

        async def on_disconnect(self):
            print("RoseBot.py is offline.")

        async def on_ready(self):
            pass

        async def on_message(self, message):
            pass


bot = Bot()
