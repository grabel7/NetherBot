import discord
import random
from discord.ext import commands

# Prefixo do bot e permissões
client = commands.Bot(command_prefix='!', help_command=None, intents=discord.Intents.all())


# Ao iniciar:
@client.event
async def on_ready():
    print('Logado como: {0.user}'.format(client))
    try:
        synced = await client.tree.sync()
        print(f'Sincronizado(s) {len(synced)} comando(s)')
    except Exception as e:
        print(f'Erro sincronizando comandos: {e}')
        
# Definição dos códigos
def nethera(x: float, z: float):
    return 'X:', x / 8, 'Z:', z / 8


def overworld1(x: float, z: float):
    return ['X: ', x * 8, 'Z: ', z * 8]

@client.tree.command(name='nether')
async def nether(interaction: discord.Interaction, x: float, z: float):
    x = nethera(x, z)
    await interaction.response.send_message(f'Se você entrar em um portal no Overworld, você irá parar no '
                                            f'Nether com essas coordenadas: {x}')


@client.tree.command(name='overworld')
async def overworld(interaction: discord.Interaction, x: float, z: float):
    pos = overworld1(x, z)
    await interaction.response.send_message(f'Se você entrar em um portal do Nether nessas '
                                            f'coordenadas, sairá em: {pos}')


# Token utilizada para ligar o seu bot, você pode conseguir uma em https://discord.com/developers/applications
client.run('TOKEN')
