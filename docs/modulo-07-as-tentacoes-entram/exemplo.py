# Módulo 7 - As tentações entram
# No VS Code, com o venv do projeto selecionado como interpretador, basta
# clicar em "Run Python File" (por causa do "import pgzrun" no topo e do
# "pgzrun.go()" no final do arquivo), ou rodar pelo terminal:
# python jogo.py

import pgzrun
import random

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
COR_DA_REGUA = "gold"
COR_DA_TENTACAO = "crimson"
NOME_DO_PECADOR = "Escreva seu nome aqui"

# Onde o personagem começa: coluna e linha do mapa (contando a partir do 0)
INICIO_COLUNA = 9
INICIO_LINHA = 12

# O personagem agora mora num quadradinho do mapa
personagem_coluna = INICIO_COLUNA
personagem_linha = INICIO_LINHA
personagem_raio = TILE // 2 - 4
personagem_cor = "gold"

# Quanto cada bom hábito faz você crescer
PONTOS_POR_HABITO = 10

# A estatura: um contador. Começa em 0 e cresce a cada bom hábito.
estatura = 0

# O relógio do jogo: a cada ESPERA_PERSONAGEM voltas do update(), o personagem anda
ESPERA_PERSONAGEM = 12
quadros_personagem = 0

# A direção é um par: (1, 0) direita, (-1, 0) esquerda, (0, 1) baixo, (0, -1) cima.
# O personagem anda SOZINHO na direção guardada. As setas só escolhem a
# próxima direção, que vale assim que der para virar.
direcao = (0, 0)           # (0, 0) = parado
proxima_direcao = (0, 0)

# A tentação (desobediência) começa no meio do labirinto, olhando para a esquerda
TENTACAO_INICIO_COLUNA = 9
TENTACAO_INICIO_LINHA = 8
tentacao_coluna = TENTACAO_INICIO_COLUNA
tentacao_linha = TENTACAO_INICIO_LINHA
tentacao_direcao = (-1, 0)

# As quatro direções que a tentação pode tentar
DIRECOES = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# A tentação tem o relógio dela: é um pouco mais lenta que você
ESPERA_TENTACAO = 16
quadros_tentacao = 0

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

    # O placar (HUD): a estatura à esquerda e quantos hábitos faltam à direita.
    # str() transforma o número em texto, para poder juntar com o +.
    screen.draw.text(
        "Estatura: " + str(estatura),
        topleft=(10, 8),
        fontsize=28,
        color=COR_DO_TEXTO,
    )
    screen.draw.text(
        "Faltam: " + str(len(habitos)),
        topright=(WIDTH - 10, 8),
        fontsize=28,
        color=COR_DO_TEXTO,
    )

    # A lista ficou vazia? Então todos os hábitos foram coletados!
    if len(habitos) == 0:
        mensagem = "Parabéns! Você cresceu!"
    else:
        mensagem = "As setas escolhem o caminho!"

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

    # A régua da estatura: um retângulo que fica mais comprido quanto mais
    # você cresce. A estatura máxima é 1160, e 1160 // 3 dá 386 pixels.
    # A moldura (só a borda) mostra até onde a régua pode chegar.
    regua = Rect((WIDTH - 400, HEIGHT - 28), (estatura // 3, 16))
    screen.draw.filled_rect(regua, COR_DA_REGUA)
    moldura = Rect((WIDTH - 400, HEIGHT - 28), (386, 16))
    screen.draw.rect(moldura, COR_DO_TEXTO)

    # Do quadradinho (coluna, linha) para os pixels do centro dele
    x = personagem_coluna * TILE + TILE // 2
    y = personagem_linha * TILE + TILE // 2
    screen.draw.filled_circle((x, y), personagem_raio, personagem_cor)

    # A tentação: um círculo com dois olhos que olham para onde ela vai
    x = tentacao_coluna * TILE + TILE // 2
    y = tentacao_linha * TILE + TILE // 2
    screen.draw.filled_circle((x, y), TILE // 2 - 4, COR_DA_TENTACAO)
    olhar_x = tentacao_direcao[0] * 2
    olhar_y = tentacao_direcao[1] * 2
    screen.draw.filled_circle((x - 6, y - 4), 5, "white")
    screen.draw.filled_circle((x + 6, y - 4), 5, "white")
    screen.draw.filled_circle((x - 6 + olhar_x, y - 4 + olhar_y), 2, "black")
    screen.draw.filled_circle((x + 6 + olhar_x, y - 4 + olhar_y), 2, "black")


def update():
    global quadros_personagem, personagem_coluna, personagem_linha
    global direcao, estatura
    global quadros_tentacao, tentacao_coluna, tentacao_linha, tentacao_direcao

    # ---------------- o personagem ----------------
    quadros_personagem = quadros_personagem + 1
    if quadros_personagem == ESPERA_PERSONAGEM:
        quadros_personagem = 0

        # 1. Dá para virar para a direção que você escolheu? Então vira.
        nova_coluna = personagem_coluna + proxima_direcao[0]
        nova_linha = personagem_linha + proxima_direcao[1]
        if nova_coluna < 0:
            nova_coluna = COLUNAS - 1
        if nova_coluna >= COLUNAS:
            nova_coluna = 0
        if MAPA[nova_linha][nova_coluna] != "#":
            direcao = proxima_direcao

        # 2. Anda um quadradinho na direção atual, se lá não for parede
        nova_coluna = personagem_coluna + direcao[0]
        nova_linha = personagem_linha + direcao[1]
        if nova_coluna < 0:
            nova_coluna = COLUNAS - 1
        if nova_coluna >= COLUNAS:
            nova_coluna = 0
        if MAPA[nova_linha][nova_coluna] != "#":
            personagem_coluna = nova_coluna
            personagem_linha = nova_linha

        # 3. Parou em cima de um bom hábito? Ele sai da lista e você cresce
        if (personagem_coluna, personagem_linha) in habitos:
            habitos.remove((personagem_coluna, personagem_linha))
            estatura = estatura + PONTOS_POR_HABITO

    # ---------------- a tentação ----------------
    quadros_tentacao = quadros_tentacao + 1
    if quadros_tentacao == ESPERA_TENTACAO:
        quadros_tentacao = 0

        # 1. Quais caminhos estão livres? Ela nunca dá meia-volta.
        meia_volta = (-tentacao_direcao[0], -tentacao_direcao[1])
        livres = []
        for opcao in DIRECOES:
            if opcao != meia_volta:
                nova_coluna = tentacao_coluna + opcao[0]
                nova_linha = tentacao_linha + opcao[1]
                if nova_coluna < 0:
                    nova_coluna = COLUNAS - 1
                if nova_coluna >= COLUNAS:
                    nova_coluna = 0
                if MAPA[nova_linha][nova_coluna] != "#":
                    livres.append(opcao)

        # 2. Sorteia um dos caminhos livres. No corredor só tem um;
        #    no cruzamento tem dois ou três, e o random escolhe.
        tentacao_direcao = random.choice(livres)

        # 3. Anda um quadradinho para lá (com túnel)
        tentacao_coluna = tentacao_coluna + tentacao_direcao[0]
        tentacao_linha = tentacao_linha + tentacao_direcao[1]
        if tentacao_coluna < 0:
            tentacao_coluna = COLUNAS - 1
        if tentacao_coluna >= COLUNAS:
            tentacao_coluna = 0


def on_key_down(key):
    global personagem_coluna, personagem_linha, direcao, proxima_direcao

    if key == keys.SPACE:
        personagem_coluna = INICIO_COLUNA
        personagem_linha = INICIO_LINHA
        direcao = (0, 0)
        proxima_direcao = (0, 0)

    # As setas só ESCOLHEM a direção. Quem anda é o update().
    if key == keys.RIGHT:
        proxima_direcao = (1, 0)
    if key == keys.LEFT:
        proxima_direcao = (-1, 0)
    if key == keys.DOWN:
        proxima_direcao = (0, 1)
    if key == keys.UP:
        proxima_direcao = (0, -1)


pgzrun.go()
