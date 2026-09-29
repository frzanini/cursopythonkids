# Módulo 4 - Os muros do labirinto
# No VS Code, com o venv do projeto selecionado como interpretador, basta
# clicar em "Run Python File" (por causa do "import pgzrun" no topo e do
# "pgzrun.go()" no final do arquivo), ou rodar pelo terminal:
# uv run jogo.py

import pgzrun

# O labirinto: uma LISTA de textos. Cada texto é uma linha do mapa.
#   "#" = parede
#   "." = caminho (é onde os bons hábitos vão aparecer no Módulo 5)
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
NOME_DO_PECADOR = "Escreva seu nome aqui"

# Onde o personagem começa: coluna e linha do mapa (contando a partir do 0)
INICIO_COLUNA = 9
INICIO_LINHA = 12

# O personagem agora mora num quadradinho do mapa
personagem_coluna = INICIO_COLUNA
personagem_linha = INICIO_LINHA
personagem_raio = TILE // 2 - 4
personagem_cor = "gold"


def draw():
    screen.fill(COR_DE_FUNDO)

    # As paredes: passa por todas as linhas e, em cada linha, por todas as
    # colunas. Onde o mapa tem "#", desenha um quadrado.
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            if MAPA[linha][coluna] == "#":
                parede = Rect((coluna * TILE, linha * TILE), (TILE, TILE))
                screen.draw.filled_rect(parede, COR_DA_PAREDE)

    screen.draw.text(
        "Setas: anda um quadradinho. Espaco: volta ao inicio.",
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


pgzrun.go()
