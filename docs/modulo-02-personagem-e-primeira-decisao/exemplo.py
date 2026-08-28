# Módulo 2 - O personagem e a primeira decisão
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

PERGUNTA = "Você orou hoje?"

# Posição e tamanho do personagem (um círculo, por enquanto)
personagem_x = WIDTH // 2
personagem_y = HEIGHT // 2 - 60
personagem_raio = 40
personagem_cor = "gold"

# Estado da resposta: começa sem nenhuma resposta ainda
respondeu = False
resposta_foi_sim = False

# Área (retângulo) de cada botão: (x, y, largura, altura)
botao_sim = Rect((WIDTH // 2 - 160, HEIGHT // 2 + 120), (120, 50))
botao_nao = Rect((WIDTH // 2 + 40, HEIGHT // 2 + 120), (120, 50))


def draw():
    screen.fill(COR_DE_FUNDO)

    screen.draw.text(
        "Pecador: " + NOME_DO_PECADOR,
        topleft=(10, HEIGHT - 30),
        fontsize=16,
        color=COR_DO_TEXTO,
    )

    screen.draw.text(
        PERGUNTA,
        center=(WIDTH // 2, HEIGHT // 2 - 160),
        fontsize=32,
        color=COR_DO_TEXTO,
    )

    # O personagem: cresce e muda de cor quando a resposta é "Sim"
    screen.draw.filled_circle(
        (personagem_x, personagem_y), personagem_raio, personagem_cor
    )

    screen.draw.filled_rect(botao_sim, "green")
    screen.draw.text("Sim", center=botao_sim.center, fontsize=28, color="white")

    screen.draw.filled_rect(botao_nao, "red")
    screen.draw.text("Não", center=botao_nao.center, fontsize=28, color="white")

    if respondeu:
        if resposta_foi_sim:
            mensagem = "Muito bem! Continue assim!"
        else:
            mensagem = "Que tal fazer isso hoje?"

        screen.draw.text(
            mensagem,
            center=(WIDTH // 2, HEIGHT // 2 + 220),
            fontsize=26,
            color="white",
        )


def on_mouse_down(pos):
    global respondeu, resposta_foi_sim, personagem_raio, personagem_cor

    if botao_sim.collidepoint(pos):
        respondeu = True
        resposta_foi_sim = True
        personagem_raio = 60
        personagem_cor = "yellow"
    elif botao_nao.collidepoint(pos):
        respondeu = True
        resposta_foi_sim = False
        personagem_raio = 30
        personagem_cor = "gray"


pgzrun.go()
