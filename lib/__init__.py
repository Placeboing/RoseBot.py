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

        def run(self, version):
            self.VERSION = version

            with open(".lib/bot/token", "r", encoding="utf-8") as tf:
                self.TOKEN = tf.read()

                print("RoseBot.py is starting...")
                super().run(self.TOKEN, reconnect=True)

        async def on_connect(self):
            print("RoseBot.py connected.")

        async def on_disconnect(self):
            print("RoseBot.py disconnected.")

        async def on_ready(self):
            if not self.ready:
                self.ready = True
                self.guild = self.get_guild(754106959791259678)
                print("RoseBot.py is online.")

            else:
                print("RoseBot.py attempting to reconnect.")

        async def on_message(self, message):
            pass


bot = Bot()
