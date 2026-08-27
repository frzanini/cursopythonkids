# Crescendo como Jesus - jogo de referencia (o "gabarito") e DEMO do curso.
# Estilo Pac-Man, tema de Lucas 2:52.
#
# Este arquivo e o jogo COMPLETO e jogavel, mostrado pronto aos alunos no
# comeco do curso como motivacao. Ele NAO acompanha o ritmo fatiado dos
# modulos - o recorte por aula vive so nos docs/modulo-NN/exemplo.py.
# Design e regras: docs/design-do-jogo.md
#
# A crianca anda pelo labirinto da vida coletando bons habitos e desviando
# das tentacoes. A Oracao da forca para vencer as tentacoes por alguns
# segundos. Encher a vida de virtude (coletar tudo) completa a fase.
# Sao 4 fases: Sabedoria -> Estatura -> Graca com Deus -> Graca com os homens.
#
# v1 desenha tudo com formas e cores (sem imagens nem sons - isso e um item
# separado do backlog).

import math
import random

import pgzrun
import pygame

# --- o labirinto -----------------------------------------------------------
# Cada linha e um texto. Simbolos:
#   '#' parede            '.' bom habito         'o' oracao (power-pellet)
#   ' ' caminho vazio     'P' inicio do jogador  'T' casa das tentacoes
MAPA = [
    "###################",
    "#o...............o#",
    "#.###.#.###.#.###.#",
    "#.................#",
    "#.###.###.###.###.#",
    "#...#...#.#...#...#",
    "###.#.#.#.#.#.#.###",
    "#.....#.....#.....#",
    "#.###.#.###.#.###.#",
    "#.....#.TTT.#.....#",
    "#.###.#.###.#.###.#",
    "#.....#.....#.....#",
    "###.#.#.#.#.#.#.###",
    "#...#...#.#...#...#",
    "#.###.###.###.###.#",
    "#o.......P.......o#",
    "###################",
]

TILE = 30          # tamanho de cada quadradinho, em pixels
MARGEM_TOPO = 46   # faixa de cima para o placar (HUD)

COLUNAS = len(MAPA[0])
LINHAS = len(MAPA)
WIDTH = COLUNAS * TILE
HEIGHT = LINHAS * TILE + MARGEM_TOPO
TITLE = "Crescendo como Jesus"

# --- ajustes de jogo -----------------------------------------------------------
VEL_JOGADOR = 92          # pixels por segundo (base; sobe por fase)
VEL_TENTACAO = 76         # sempre um pouco menor que a do jogador
VIDAS_INICIAIS = 3
ORACAO_DURACAO = 6.0      # segundos de "modo oracao"
N_TENTACOES_BASE = 2      # fase 1 tem 2; cada fase seguinte ganha +1

FASES = ["Sabedoria", "Estatura", "Graca com Deus", "Graca com os homens"]
NOMES_TENT = ["Desobediencia", "Mentira", "Preguica", "Distracao"]
CORES_TENT = [(230, 70, 70), (180, 100, 225), (110, 190, 100), (240, 155, 45)]

# --- cores -------------------------------------------------------------------
COR_FUNDO = (10, 12, 34)
COR_PAREDE = (36, 58, 176)
COR_HABITO = (255, 224, 150)
COR_ORACAO = (130, 225, 255)
COR_JOGADOR = (255, 214, 40)
COR_ASSUSTADA = (80, 100, 235)
COR_ASSUSTADA_FIM = (238, 240, 255)
COR_TEXTO = (236, 236, 242)
COR_HUD = (206, 214, 140)
COR_VERSICULO = (170, 200, 255)

VERSICULO = ('"E crescia Jesus em sabedoria, e em estatura,\n'
             'e em graca, para com Deus e os homens."\n'
             'Lucas 2:52')


# --- funcoes de mapa -------------------------------------------------------
def eh_parede(col, linha):
    """Diz se o quadradinho (col, linha) e parede ou esta fora do mapa."""
    if linha < 0 or linha >= LINHAS:
        return True
    if col < 0 or col >= COLUNAS:
        return True
    return MAPA[linha][col] == "#"


def centro(col, linha):
    """Posicao em pixels do centro do quadradinho (col, linha)."""
    return (col * TILE + TILE // 2,
            linha * TILE + TILE // 2 + MARGEM_TOPO)


def achar(marca):
    """Primeira posicao (col, linha) onde aparece 'marca' no mapa."""
    for linha, texto in enumerate(MAPA):
        col = texto.find(marca)
        if col != -1:
            return (col, linha)
    return (1, 1)


def achar_todos(marca):
    """Todas as posicoes (col, linha) onde aparece 'marca' no mapa."""
    achados = []
    for linha, texto in enumerate(MAPA):
        for col, c in enumerate(texto):
            if c == marca:
                achados.append((col, linha))
    return achados


# --- quem anda pela grade -------------------------------------------------
class AndarilhoDaGrade:
    """Base do jogador e das tentacoes: anda alinhado a grade, um
    quadradinho por vez, e nunca atravessa parede."""

    def __init__(self, col, linha, velocidade):
        self.col = col
        self.linha = linha
        self.x, self.y = centro(col, linha)
        self.dx = 0          # direcao atual em quadradinhos: -1, 0 ou 1
        self.dy = 0
        self.velocidade = velocidade

    def parado(self):
        return self.dx == 0 and self.dy == 0

    def ao_chegar_no_centro(self):
        """Cada subclasse decide aqui para onde ir. Chamado sempre que o
        personagem esta encaixado no centro de um quadradinho."""
        pass

    def atualizar(self, dt):
        if self.parado():
            self.ao_chegar_no_centro()
            if self.parado():
                return

        passo = self.velocidade * dt
        alvo_x, alvo_y = centro(self.col + self.dx, self.linha + self.dy)
        self.x += self.dx * passo
        self.y += self.dy * passo

        chegou = (
            (self.dx == 1 and self.x >= alvo_x)
            or (self.dx == -1 and self.x <= alvo_x)
            or (self.dy == 1 and self.y >= alvo_y)
            or (self.dy == -1 and self.y <= alvo_y)
        )
        if chegou:
            self.col += self.dx
            self.linha += self.dy
            self.x, self.y = alvo_x, alvo_y
            self.ao_chegar_no_centro()


class Jogador(AndarilhoDaGrade):
    """A crianca crescendo em estatura. As setas guardam a proxima direcao,
    aplicada assim que der para virar."""

    def __init__(self, col, linha, velocidade):
        super().__init__(col, linha, velocidade)
        self.prox_dx = 0
        self.prox_dy = 0

    def pedir_direcao(self, dx, dy):
        # Meia-volta e imediata: se ja anda e pediu o contrario, vira na hora.
        if not self.parado() and (dx, dy) == (-self.dx, -self.dy):
            self.col += self.dx
            self.linha += self.dy
            self.dx, self.dy = dx, dy
            self.prox_dx = self.prox_dy = 0
        else:
            self.prox_dx, self.prox_dy = dx, dy

    def ao_chegar_no_centro(self):
        if (self.prox_dx or self.prox_dy) and not eh_parede(
            self.col + self.prox_dx, self.linha + self.prox_dy
        ):
            self.dx, self.dy = self.prox_dx, self.prox_dy
            self.prox_dx = self.prox_dy = 0
        elif eh_parede(self.col + self.dx, self.linha + self.dy):
            self.dx = self.dy = 0


class Tentacao(AndarilhoDaGrade):
    """Tentacao / ma influencia. IA simples: em cada cruzamento escolhe
    direcao - quase sempre aleatoria, as vezes perseguindo o jogador. Nunca
    da meia-volta (a nao ser em beco sem saida). No modo oracao, foge."""

    def __init__(self, col, linha, velocidade, cor, nome, prob_perseguir):
        super().__init__(col, linha, velocidade)
        self.casa = (col, linha)
        self.cor = cor
        self.nome = nome
        self.prob_perseguir = prob_perseguir
        self.assustada = False
        self.preso_timer = 0.0     # segundos "presa em casa" depois de vencida

    def _direcoes_validas(self, permitir_re=False):
        opcoes = []
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            eh_re = not self.parado() and (dx, dy) == (-self.dx, -self.dy)
            if eh_re and not permitir_re:
                continue
            if not eh_parede(self.col + dx, self.linha + dy):
                opcoes.append((dx, dy))
        return opcoes

    def _escolher_por_distancia(self, opcoes, fugir):
        alvo_c, alvo_l = jogador.col, jogador.linha

        def distancia(op):
            return (abs(self.col + op[0] - alvo_c)
                    + abs(self.linha + op[1] - alvo_l))

        return max(opcoes, key=distancia) if fugir else min(opcoes, key=distancia)

    def ao_chegar_no_centro(self):
        opcoes = self._direcoes_validas()
        if not opcoes:                       # beco sem saida: pode voltar
            opcoes = self._direcoes_validas(permitir_re=True)
        if not opcoes:
            self.dx = self.dy = 0
            return

        if self.assustada:
            escolha = self._escolher_por_distancia(opcoes, fugir=True)
        elif random.random() < self.prob_perseguir:
            escolha = self._escolher_por_distancia(opcoes, fugir=False)
        else:
            escolha = random.choice(opcoes)
        self.dx, self.dy = escolha

    def ir_pra_casa(self):
        """Vencida no modo oracao: volta pra casa e fica presa alguns
        segundos antes de voltar a andar."""
        self.col, self.linha = self.casa
        self.x, self.y = centro(*self.casa)
        self.dx = self.dy = 0
        self.assustada = False
        self.preso_timer = 3.0


# --- estado do jogo ---------------------------------------------------------
estado = "inicio"        # inicio | jogando | intervalo | vitoria | derrota
fase_idx = 0
score = 0
vidas = VIDAS_INICIAIS
tempo = 0.0              # relogio geral, so para animacoes
oracao_timer = 0.0
pausa_timer = 0.0        # congela o jogo depois de perder uma vida
intervalo_timer = 0.0    # tela curta entre uma fase e a proxima
mensagem = ""
habitos = set()
oracoes = set()
tentacoes = []
jogador = None


def iniciar_fase(idx):
    """Monta a fase 'idx': repovoa os itens, recoloca o jogador e cria as
    tentacoes (mais uma a cada fase, mais rapidas e mais espertas)."""
    global habitos, oracoes, tentacoes, jogador
    global oracao_timer, pausa_timer, mensagem

    habitos = set(achar_todos("."))
    oracoes = set(achar_todos("o"))

    inicio = achar("P")
    jogador = Jogador(inicio[0], inicio[1], VEL_JOGADOR + idx * 4)

    casas = achar_todos("T")
    quantas = min(N_TENTACOES_BASE + idx, 5)
    tentacoes = []
    for i in range(quantas):
        casa = casas[i % len(casas)]
        tentacoes.append(Tentacao(
            casa[0], casa[1],
            VEL_TENTACAO + idx * 6,
            CORES_TENT[i % len(CORES_TENT)],
            NOMES_TENT[i % len(NOMES_TENT)],
            min(0.30 + idx * 0.12, 0.78),
        ))

    oracao_timer = 0.0
    pausa_timer = 0.0
    mensagem = ""


def reiniciar_posicoes():
    """Depois de perder uma vida: todo mundo volta para o lugar de inicio."""
    inicio = achar("P")
    jogador.col, jogador.linha = inicio
    jogador.x, jogador.y = centro(*inicio)
    jogador.dx = jogador.dy = 0
    jogador.prox_dx = jogador.prox_dy = 0
    for t in tentacoes:
        t.col, t.linha = t.casa
        t.x, t.y = centro(*t.casa)
        t.dx = t.dy = 0
        t.assustada = False
        t.preso_timer = 0.0


def perder_vida():
    global vidas, estado, pausa_timer, mensagem, oracao_timer
    vidas -= 1
    oracao_timer = 0.0
    if vidas <= 0:
        estado = "derrota"
    else:
        reiniciar_posicoes()
        pausa_timer = 1.3
        mensagem = "Uma tentacao te derrubou. Levanta e continua!"


def comecar_jogo():
    global estado, fase_idx, score, vidas
    fase_idx = 0
    score = 0
    vidas = VIDAS_INICIAIS
    iniciar_fase(0)
    estado = "jogando"


iniciar_fase(0)   # deixa a fase 1 montada ja na tela inicial (so de fundo)


# --- laco principal -------------------------------------------------------
def update(dt):
    global tempo, oracao_timer, pausa_timer, intervalo_timer
    global estado, fase_idx, score, vidas, mensagem

    tempo += dt

    if estado == "intervalo":
        intervalo_timer -= dt
        if intervalo_timer <= 0:
            fase_idx += 1
            iniciar_fase(fase_idx)
            estado = "jogando"
        return

    if estado != "jogando":
        return

    if pausa_timer > 0:
        pausa_timer -= dt
        return

    jogador.atualizar(dt)

    # coletar itens do quadradinho em que o jogador esta
    aqui = (jogador.col, jogador.linha)
    if aqui in habitos:
        habitos.discard(aqui)
        score += 10
    if aqui in oracoes:
        oracoes.discard(aqui)
        score += 5
        oracao_timer = ORACAO_DURACAO

    if oracao_timer > 0:
        oracao_timer = max(0.0, oracao_timer - dt)

    # mover as tentacoes
    for t in tentacoes:
        if t.preso_timer > 0:
            t.preso_timer -= dt
            t.assustada = False
            continue
        t.assustada = oracao_timer > 0
        t.atualizar(dt)

    # encostou em alguma tentacao?
    for t in tentacoes:
        if t.preso_timer > 0:
            continue
        perto = (abs(t.x - jogador.x) < TILE * 0.55
                 and abs(t.y - jogador.y) < TILE * 0.55)
        if not perto:
            continue
        if t.assustada:
            t.ir_pra_casa()
            score += 100
        else:
            perder_vida()
            return

    # encheu a vida de virtude -> proxima fase (ou vitoria)
    if not habitos and not oracoes:
        if fase_idx + 1 < len(FASES):
            estado = "intervalo"
            intervalo_timer = 2.6
        else:
            estado = "vitoria"


def on_key_down(key):
    global estado

    if estado == "inicio":
        if key in (keys.RETURN, keys.KP_ENTER, keys.SPACE):
            comecar_jogo()

    elif estado == "jogando":
        if key in (keys.LEFT, keys.A):
            jogador.pedir_direcao(-1, 0)
        elif key in (keys.RIGHT, keys.D):
            jogador.pedir_direcao(1, 0)
        elif key in (keys.UP, keys.W):
            jogador.pedir_direcao(0, -1)
        elif key in (keys.DOWN, keys.S):
            jogador.pedir_direcao(0, 1)

    elif estado in ("vitoria", "derrota"):
        if key in (keys.RETURN, keys.KP_ENTER, keys.SPACE):
            estado = "inicio"


# --- desenho -------------------------------------------------------------
def desenhar_labirinto():
    for linha, texto in enumerate(MAPA):
        for col, marca in enumerate(texto):
            if marca == "#":
                x = col * TILE
                y = linha * TILE + MARGEM_TOPO
                screen.draw.filled_rect(
                    Rect((x + 1, y + 1), (TILE - 2, TILE - 2)), COR_PAREDE)


def desenhar_habitos():
    raio_dot = max(2, int(TILE * 0.11))
    for (c, l) in habitos:
        screen.draw.filled_circle(centro(c, l), raio_dot, COR_HABITO)
    pulso = 2 + math.sin(tempo * 6) * 1.5
    for (c, l) in oracoes:
        screen.draw.filled_circle(centro(c, l), int(TILE * 0.20 + pulso), COR_ORACAO)


def desenhar_jogador():
    r = TILE * 0.42
    screen.draw.filled_circle((jogador.x, jogador.y), int(r), COR_JOGADOR)
    # a "boca" e um triangulo da cor do fundo, apontando para onde anda
    dx, dy = (jogador.dx, jogador.dy) if not jogador.parado() else (1, 0)
    ang = math.atan2(dy, dx)
    abertura = 0.55 + 0.35 * abs(math.sin(tempo * 12))
    ponta = r * 1.7
    p1 = (jogador.x, jogador.y)
    p2 = (jogador.x + math.cos(ang - abertura) * ponta,
          jogador.y + math.sin(ang - abertura) * ponta)
    p3 = (jogador.x + math.cos(ang + abertura) * ponta,
          jogador.y + math.sin(ang + abertura) * ponta)
    pygame.draw.polygon(screen.surface, COR_FUNDO, [p1, p2, p3])


def desenhar_tentacoes():
    r = int(TILE * 0.42)
    for t in tentacoes:
        if t.assustada:
            cor = COR_ASSUSTADA
            if oracao_timer < 2 and int(tempo * 8) % 2 == 0:
                cor = COR_ASSUSTADA_FIM
        else:
            cor = t.cor
        if t.preso_timer > 0:
            cor = tuple(v // 2 for v in cor)
        screen.draw.filled_circle((t.x, t.y), r, cor)
        ox, oy = r * 0.35, -r * 0.1
        branco = max(2, int(r * 0.24))
        pupila = max(1, int(r * 0.11))
        screen.draw.filled_circle((t.x - ox, t.y + oy), branco, (255, 255, 255))
        screen.draw.filled_circle((t.x + ox, t.y + oy), branco, (255, 255, 255))
        screen.draw.filled_circle((t.x - ox, t.y + oy), pupila, (20, 20, 45))
        screen.draw.filled_circle((t.x + ox, t.y + oy), pupila, (20, 20, 45))


def desenhar_hud():
    screen.draw.filled_rect(Rect((0, 0), (WIDTH, MARGEM_TOPO)), (6, 8, 24))
    screen.draw.text(f"Estatura: {score}", topleft=(10, 8),
                     color=COR_HUD, fontsize=22)
    screen.draw.text(f"Fase {fase_idx + 1}/4  -  {FASES[fase_idx]}",
                     midtop=(WIDTH // 2, 6), color=COR_TEXTO, fontsize=20)
    screen.draw.text(f"Vidas: {vidas}", topright=(WIDTH - 10, 8),
                     color=COR_HUD, fontsize=22)
    if oracao_timer > 0:
        frac = oracao_timer / ORACAO_DURACAO
        screen.draw.filled_rect(
            Rect((0, MARGEM_TOPO - 5), (int(WIDTH * frac), 5)), COR_ORACAO)
        screen.draw.text("Oracao! As tentacoes fogem.",
                         midtop=(WIDTH // 2, 26), color=COR_ORACAO, fontsize=16)


def faixa_central(texto):
    screen.draw.filled_rect(Rect((0, HEIGHT // 2 - 48), (WIDTH, 96)), (0, 0, 0))
    screen.draw.text(texto, center=(WIDTH // 2, HEIGHT // 2),
                     color=COR_TEXTO, fontsize=26, align="center")


def tela_inicio():
    screen.fill(COR_FUNDO)
    screen.draw.text("Crescendo como Jesus", midtop=(WIDTH // 2, 38),
                     color=COR_JOGADOR, fontsize=40)
    screen.draw.text(VERSICULO, midtop=(WIDTH // 2, 96),
                     color=COR_VERSICULO, fontsize=20, align="center")
    briefing = (
        "Ande pelo labirinto da vida com as setas.\n"
        "Colete os bons habitos e cresca em estatura:\n"
        "oracao, Biblia, culto, obedecer, ajudar.\n\n"
        "Fuja das tentacoes. Ao pegar uma Oracao,\n"
        "por alguns segundos voce vence as tentacoes!"
    )
    screen.draw.text(briefing, midtop=(WIDTH // 2, 196),
                     color=COR_TEXTO, fontsize=19, align="center")
    if int(tempo * 2) % 2 == 0:
        screen.draw.text("ENTER para comecar",
                         midbottom=(WIDTH // 2, HEIGHT - 28),
                         color=COR_HUD, fontsize=24)


def tela_fim(venceu):
    screen.fill(COR_FUNDO)
    if venceu:
        screen.draw.text("Voce cresceu como Jesus!", midtop=(WIDTH // 2, 84),
                         color=COR_JOGADOR, fontsize=32, align="center")
        screen.draw.text(f"{VERSICULO}\n\nEstatura final: {score}",
                         midtop=(WIDTH // 2, 168), color=COR_TEXTO,
                         fontsize=20, align="center")
    else:
        # Na derrota do jogo, o destaque e para JESUS: e Ele quem venceu.
        screen.draw.text("JESUS", midtop=(WIDTH // 2, 56),
                         color=COR_JOGADOR, fontsize=66, align="center",
                         shadow=(2, 2), scolor=(0, 0, 0))
        screen.draw.text("ja venceu na cruz.\n"
                         "O mal nunca tem a ultima palavra.",
                         midtop=(WIDTH // 2, 132), color=COR_TEXTO,
                         fontsize=22, align="center")
        corpo = (
            "Persevera nas disciplinas espirituais:\n"
            "oracao, leitura da Biblia, culto,\n"
            "obediencia e servir ao proximo.\n\n"
            '"Em todas estas coisas somos mais que\n'
            'vencedores, por meio daquele que nos amou."\n'
            "Romanos 8:37\n\n"
            f"Estatura alcancada: {score}"
        )
        screen.draw.text(corpo, midtop=(WIDTH // 2, 206), color=COR_TEXTO,
                         fontsize=19, align="center")
    if int(tempo * 2) % 2 == 0:
        screen.draw.text("ENTER para jogar de novo",
                         midbottom=(WIDTH // 2, HEIGHT - 38),
                         color=COR_HUD, fontsize=22)


def draw():
    if estado == "inicio":
        tela_inicio()
        return
    if estado == "vitoria":
        tela_fim(True)
        return
    if estado == "derrota":
        tela_fim(False)
        return

    screen.fill(COR_FUNDO)
    desenhar_labirinto()
    desenhar_habitos()
    desenhar_jogador()
    desenhar_tentacoes()
    desenhar_hud()

    if estado == "intervalo":
        faixa_central(f"Fase concluida!\nProxima: {FASES[fase_idx + 1]}")
    elif pausa_timer > 0 and mensagem:
        faixa_central(mensagem)


pgzrun.go()
