# NetherBot
Um repositório para a explicação simples do funcionamento de um Bot de Discord em Python.

# Introdução
 No final do ano de 2022, o Discord publicou a funcionalidade dos slash commands, comandos por / que facilitavam o acesso do usuário. Neste repositório, irei explicar como escrever um código simples utilizando dessa tecnologia e misturando o entretenimento com o jogo Minecraft.
 
# Conseguindo um Token
A primeira coisa que você deve fazer ao cadastrar um bot, é ir atrás de um token. Você consegue um cadastrando um bot no site: https://discord.com/developers/applications. Tenha muito cuidado, pois cada Token é único e o seu vazamento pode dar acesso a usuários maliciosos.

# Decompilando o Código
O código tem algumas funções simples pré-escritas como: O que fazer ao iniciar, qual prefixo utilizar e qual permissão o bot terá. Para fins de estudo, utilizei o comando "discord.Intents.all()", dando acesso total ao bot. 
A linha @client.tree.command(name='nome_do_comando') é a que demarca todos os comandos em slash, caso queria utilizar do método antigo, você pode usar: @client.command(aliases=['prefixos'])
Para melhor entedimento, escrevi um código baseado no jogo Minecraft. No jogo existem duas dimensões, o Overworld e o Nether. Cada passo dado no Overworld equivalem a 8 passos dados no Nether, o meu bot irá calcular as coordenadas com base nisso. 
Para isso, eu escrevi uma definição. Em outro lugar do código você pode encontrar o def nethera(x: float, z: float), que é responsável por gerar os valores pedidos pelo bot. Ele dividirá X e Z por 8 e então irá enviar para o comando solicitado. Porém, vale lembrar que as variáveis X e Z não estão definidas, então, caso iniciado, o código não irá funcionar.
Como faço para definir as variáveis?
Você quer um input. Porém, inputs não funcionam com bots, afinal o console irá perguntar para o próprio bot qual o input dele, excluindo o usuário. Então para isso, utilizamos o seguinte código abaixo do client.tree: "async def nether(interaction: discord.Interaction, x: float, z: float)". Ele irá demarcar que precisaremos do valor de X (em float) e de Z para que o código seja compilado corretamente, além de solicitar uma interação do próprio programa. Para conseguirmos as coordenadas corretas, ou seja, os valores de X e Z, utilizamos: ```"x = nethera(x, z)"``` que irá requisitar os valores X e Z da Nethera, que foi previamente definida. E então, para que o bot nos responda, utilizamos o seguinte código: "await interaction.response.send_message(f'Se você entrar em um portal no Overworld, você irá parar no Nether com essas coordenadas: {x}')" A variável X serão as coordenadas divididas por 8, como requisitado para o bot.

O mesmo também foi feito no oposto, onde fiz um código que multiplica esses valores por 8, corrigindo as coordenadas do Overworld. O código é o mesmo, mas claro, com outra def. 
```
@client.tree.command(name='overworld')
async def overworld(interaction: discord.Interaction, x: float, z: float):
    pos = overworld1(x, z)
    await interaction.response.send_message(f'Se você entrar em um portal do Nether nessas '
                                            f'coordenadas, sairá em: {pos}')
```                                            
#Final
Agora que todo o código está escrito corretamente, precisamos do acesso ao bot. Para isso, utilizamos o Token que pegamos no início do repositório. Você precisa escrever na última linha, o seguinte código: "client.run('TOKEN')" Substituindo a palavra TOKEN pelo seu token.

Obrigado pela atenção.
