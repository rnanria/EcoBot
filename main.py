import discord
from bot_logic import *

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send(welcome())
    elif message.content.startswith('$dato'):
        await message.channel.send(dato_curioso())
    elif message.content == "$reto":
        await message.channel.send(xp())
    elif message.content.startswith('$comandos'):
        await message.channel.send(help())
    elif message.content == "$idea":
            await ideas_reciclaje(message)
    else:
        await message.channel.send("No puedo procesar este comando, ¡lo siento!")

async def ideas_reciclaje(message):
    def check(m):
        return m.author == message.author and m.channel == message.channel and m.content.isdigit()

    await message.channel.send("¿Qué material desea reciclar? \n(1) Papel y cartón \n(2) Plástico \n(3) Vidrio \n(4) Metales")

    msg = await client.wait_for('message', check=check)
    opcion = int(msg.content)
    
    if opcion == 1:
        await message.channel.send("𝗣𝗮𝗽𝗲𝗹 𝘆 𝗰𝗮𝗿𝘁ó𝗻\n• Cajas de cartón: úsalas para almacenar cosas, hacer muebles para mascotas o crear cajas de regalo decorativas. \n• Tubos de papel higiénico y toallas de papel: conviértelos en organizadores de escritorio, porta lápices o juguetes para gatos. \n• Periódicos y revistas: úsalos para hacer compostaje, empaquetar regalos o crear papel maché.")
    elif opcion == 2:
        await message.channel.send("𝗣𝗹á𝘀𝘁𝗶𝗰𝗼\n• Botellas de plástico: conviértelas en macetas, organizadores de almacenamiento, comederos para pájaros o instrumentos musicales.\n• Bolsas de plástico: reutilízalas para hacer bolsas de compras reutilizables, forrar botes de basura o crear alfombras.\n• Tapas de plástico: úsalas para hacer collares, mosaicos o juguetes para niños.")
    elif opcion == 3:
        await message.channel.send("𝗩𝗶𝗱𝗿𝗶𝗼𝘀\n• Frascos de vidrio: conviértelos en vasos, jarrones, especieros o velas decorativas.\n• Botellas de vidrio: úsalas para almacenar bebidas caseras, hacer lámparas o crear arte con vidrio.")
    elif opcion == 4:
        await message.channel.send("𝗠𝗲𝘁𝗮𝗹𝗲𝘀\n• Latas de aluminio: conviértelas en adornos navideños, instrumentos musicales o organizadores de escritorio.\n• Latas de conservas: úsalas para almacenar alimentos secos, hacer macetas o crear instrumentos musicales.\n• Tapas de metal: úsalas para hacer collares, mosaicos o juguetes para niños.")
    else:
        await message.channel.send("Opción inválida, inténtalo de nuevo.")


client.run("TOKEN")
