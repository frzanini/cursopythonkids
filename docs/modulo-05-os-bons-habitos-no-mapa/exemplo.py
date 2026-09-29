# Módulo 5 - Os bons hábitos no mapa
# No VS Code, com o venv do projeto selecionado como interpretador, basta
# clicar em "Run Python File" (por causa do "import pgzrun" no topo e do
# "pgzrun.go()" no final do arquivo), ou rodar pelo terminal:
# uv run jogo.py

import pgzrun

# O labirinto: uma LISTA de textos. Cada texto é uma linha do mapa.
#   "#" = parede
#   "." = caminho com um bom hábito para coletar
#   " " = caminho vazio
# A primeira e a última linha ficam vazias: é o espaço dos textos.
# A linha do meio é aberta nas pontas: é o túnel.
MAPA = [
    "                    ",
    "####################",
    "#........##........#",
    "#.##.###.##.###.##.#",
    "#..................#",
    "#.##.#.######.#.##.#",
    "#....#...##...#....#",
    "####.###.##.###.####",
    "    .#........#.    ",
    "####.#.######.#.####",
    "#........##........#",
    "#.##.###.##.###.##.#",
    "#........  ........#",
    "####################",
    "                    ",
]

# Tamanho de cada quadradinho do mapa, em pixels
TILE = 40

COLUNAS = len(MAPA[0])  # quantas letras tem uma linha do mapa (20)
LINHAS = len(MAPA)      # quantas linhas tem o mapa (15)

WIDTH = COLUNAS * TILE  # 20 x 40 = 800
HEIGHT = LINHAS * TILE  # 15 x 40 = 600

TITLE = "Crescendo como Jesus"

COR_DE_FUNDO = "skyblue"
COR_DO_TEXTO = "white"
COR_DA_PAREDE = "navy"
COR_DO_HABITO = "darkgreen"
NOME_DO_PECADOR = "Escreva seu nome aqui"

# Onde o personagem começa: coluna e linha do mapa (contando a partir do 0)
INICIO_COLUNA = 9
INICIO_LINHA = 12

# O personagem agora mora num quadradinho do mapa
personagem_coluna = INICIO_COLUNA
personagem_linha = INICIO_LINHA
personagem_raio = TILE // 2 - 4
personagem_cor = "gold"

# Os bons hábitos: uma lista com a posição (coluna, linha) de cada um.
# Ela começa vazia e é enchida olhando o mapa: cada "." vira um hábito.
habitos = []
for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        if MAPA[linha][coluna] == ".":
            habitos.append((coluna, linha))


def draw():
    screen.fill(COR_DE_FUNDO)

    # As paredes: passa por todas as linhas e, em cada linha, por todas as
    # colunas. Onde o mapa tem "#", desenha um quadrado.
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            if MAPA[linha][coluna] == "#":
                parede = Rect((coluna * TILE, linha * TILE), (TILE, TILE))
                screen.draw.filled_rect(parede, COR_DA_PAREDE)

    # Os bons hábitos: uma bolinha no centro de cada quadradinho da lista
    for habito in habitos:
        x = habito[0] * TILE + TILE // 2
        y = habito[1] * TILE + TILE // 2
        screen.draw.filled_circle((x, y), 6, COR_DO_HABITO)

    # A lista ficou vazia? Então todos os hábitos foram coletados!
    if len(habitos) == 0:
        mensagem = "Parabens! Voce encheu sua vida de bons habitos!"
    else:
        mensagem = "Setas: anda. Passe por cima dos bons habitos."

    screen.draw.text(
        mensagem,
        center=(WIDTH // 2, TILE // 2),
        fontsize=24,
        color=COR_DO_TEXTO,
    )

    screen.draw.text(
        "Pecador: " + NOME_DO_PECADOR,
        topleft=(10, HEIGHT - 30),
        fontsize=16,
        color=COR_DO_TEXTO,
    )

    # Do quadradinho (coluna, linha) para os pixels do centro dele
    x = personagem_coluna * TILE + TILE // 2
    y = personagem_linha * TILE + TILE // 2
    screen.draw.filled_circle((x, y), personagem_raio, personagem_cor)


def on_key_down(key):
    global personagem_coluna, personagem_linha

    if key == keys.SPACE:
        personagem_coluna = INICIO_COLUNA
        personagem_linha = INICIO_LINHA

    # 1. Para onde o personagem QUER ir?
    nova_coluna = personagem_coluna
    nova_linha = personagem_linha

    if key == keys.RIGHT:
        nova_coluna = personagem_coluna + 1
    if key == keys.LEFT:
        nova_coluna = personagem_coluna - 1
    if key == keys.DOWN:
        nova_linha = personagem_linha + 1
    if key == keys.UP:
        nova_linha = personagem_linha - 1

    # 2. O túnel: saiu por um lado, entra pelo outro
    if nova_coluna < 0:
        nova_coluna = COLUNAS - 1
    if nova_coluna >= COLUNAS:
        nova_coluna = 0

    # 3. Só anda se lá não for parede
    if MAPA[nova_linha][nova_coluna] != "#":
        personagem_coluna = nova_coluna
        personagem_linha = nova_linha

    # 4. Parou em cima de um bom hábito? Ele sai da lista (e some da tela)
    if (personagem_coluna, personagem_linha) in habitos:
        habitos.remove((personagem_coluna, personagem_linha))


pgzrun.go()
