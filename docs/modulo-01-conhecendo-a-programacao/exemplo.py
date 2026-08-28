# Módulo 1 - Primeira janela do jogo
# A máquina já está pronta desde o Módulo 0 (Python 3.12, VS Code, .venv
# com pgzero, interpretador .venv selecionado). Este arquivo fica na raiz
# de crescendo-como-jesus/.
# Para rodar: botão "Run Python File" no VS Code (funciona por causa do
# "import pgzrun" no topo e do "pgzrun.go()" no final), ou no terminal
# integrado: python jogo.py

import pgzrun

WIDTH = 800
HEIGHT = 600

TITLE = "Crescendo como Jesus"

NOME_DO_CRIADOR = "Escreva seu nome aqui"
VERSICULO = "\"Jesus crescia em sabedoria, estatura e graça...\" (Lucas 2:52)"
COR_DE_FUNDO = "skyblue"
COR_DO_TEXTO = "white"


def draw():
    screen.fill(COR_DE_FUNDO)
    screen.draw.text(
        "Bem-vindo(a) ao " + TITLE + "!",
        center=(WIDTH // 2, HEIGHT // 2 - 60),
        fontsize=40,
        color=COR_DO_TEXTO,
    )
    screen.draw.text(
        VERSICULO,
        center=(WIDTH // 2, HEIGHT // 2 - 10),
        fontsize=20,
        color=COR_DO_TEXTO,
    )
    screen.draw.text(
        "Criado por: " + NOME_DO_CRIADOR,
        center=(WIDTH // 2, HEIGHT // 2 + 40),
        fontsize=24,
        color=COR_DO_TEXTO,
    )


pgzrun.go()
