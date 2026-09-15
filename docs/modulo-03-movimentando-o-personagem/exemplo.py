# Módulo 3 - Movimentando o personagem
# No VS Code, com o venv do projeto selecionado como interpretador, basta
# clicar em "Run Python File" (por causa do "import pgzrun" no topo e do
# "pgzrun.go()" no final do arquivo), ou rodar pelo terminal:
# uv run jogo.py

import pgzrun

WIDTH = 800
HEIGHT = 600

TITLE = "Crescendo como Jesus"

COR_DE_FUNDO = "skyblue"
COR_DO_TEXTO = "white"
NOME_DO_PECADOR = "Escreva seu nome aqui"

# Posição, tamanho e cor do personagem (um círculo, por enquanto)
personagem_x = WIDTH // 2
personagem_y = HEIGHT // 2
personagem_raio = 40
personagem_cor = "gold"

# Quantos pixels o personagem anda a cada passo
VELOCIDADE = 5


def draw():
    screen.fill(COR_DE_FUNDO)

    screen.draw.text(
        "Pecador: " + NOME_DO_PECADOR,
        topleft=(10, HEIGHT - 30),
        fontsize=16,
        color=COR_DO_TEXTO,
    )

    screen.draw.text(
        "Use as setas para andar. Espaco volta ao meio.",
        center=(WIDTH // 2, 30),
        fontsize=24,
        color=COR_DO_TEXTO,
    )

    screen.draw.filled_circle(
        (personagem_x, personagem_y), personagem_raio, personagem_cor
    )


def update():
    global personagem_x, personagem_y

    if keyboard.right:
        personagem_x = personagem_x + VELOCIDADE
    if keyboard.left:
        personagem_x = personagem_x - VELOCIDADE
    if keyboard.down:
        personagem_y = personagem_y + VELOCIDADE
    if keyboard.up:
        personagem_y = personagem_y - VELOCIDADE


def on_key_down(key):
    global personagem_x, personagem_y

    if key == keys.SPACE:
        personagem_x = WIDTH // 2
        personagem_y = HEIGHT // 2


pgzrun.go()
