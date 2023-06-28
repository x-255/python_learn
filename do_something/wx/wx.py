from wxpy import *

bot = Bot(cache_path=True)

bb = bot.friends().search('阿娜达')[0]
print(bb)

