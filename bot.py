import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

ALLOWED_CHANNEL_ID = 1455613451903832275
SECOND_CHANNEL_ID = 1483403044870688818

ALLOWED_USER_ID = 1330573713346920533

AUTO_REPLY = """‎ 
‎ ‎        ‎ ‎ ‎ ‎ ‎ 𓈒⠀𓂃⠀⠀˖⠀<:pink_cross:1483503420349612215>   ⠀˖⠀⠀𓂃⠀𓈒
‎  ‎ ‎ ‎ ‎          ‎        ‎‎ **__invitation sent__**

    <:000_1:1456193174002466924>please     check      your      email
‎ ‎ ‎ ‎ <:000_1:1456193174002466924>type   **/vouch**  to  send   a vouch
‎ ‎ ‎ ‎‎ <:000_1:1456193174002466924>vouch     within     **12hours**    only[.](https://cdn.discordapp.com/attachments/1480096108410568785/1492513162254090280/IMG_0263.png?ex=69db9ab3&is=69da4933&hm=9c727f4a944d3b7869eff674fa0545ad8dc6fa992c1ec8f71280bc89a7ff4b0a&)
     <:bend1:1485543789488508980>or     warranty     will     be    void.
    <:000_1:1456193174002466924>tysm  for  trusting,  come  again!
_ _"""

AUTO_REPLY_2 = """‎ 
‎ ‎        ‎ ‎ ‎ ‎ ‎ 𓈒⠀𓂃⠀⠀˖⠀<:pink_cross:1483503420349612215>   ⠀˖⠀⠀𓂃⠀𓈒
‎  ‎ ‎ ‎ ‎          ‎        ‎‎ **__data loaded__**
‎ ‎ ‎ ‎
    <:000_1:1456193174002466924>type   **/vouch**  to  send   a vouch
    <:000_1:1456193174002466924>tysm  for  trusting,  come  again[!](https://cdn.discordapp.com/attachments/1480096108410568785/1492513162254090280/IMG_0263.png?ex=69db9ab3&is=69da4933&hm=9c727f4a944d3b7869eff674fa0545ad8dc6fa992c1ec8f71280bc89a7ff4b0a&)
_ _"""

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.guild is None:
        return

    # first channel: ,s
    if message.channel.id == ALLOWED_CHANNEL_ID and message.content.strip() == ",s":
        if message.author.id == ALLOWED_USER_ID:
            await message.reply(AUTO_REPLY, mention_author=False)
        return

    # second channel: ,l
    if message.channel.id == SECOND_CHANNEL_ID and message.content.strip() == ",l":
        if message.author.id == ALLOWED_USER_ID:
            await message.reply(AUTO_REPLY_2, mention_author=False)
        return

    await bot.process_commands(message)

token = os.getenv("TOKEN")
if not token:
    raise ValueError("Walang TOKEN environment variable.")

bot.run(token)
