# Crescendo como Jesus - jogo de referencia (o "gabarito")
# Estilo Pac-Man, tema de Lucas 2:52.
#
# Fatia 2 (issue #2): o labirinto aparece na tela e o jogador anda nas 4
# direcoes, alinhado a grade, sem atravessar parede nem sair da tela.
# Ainda nao tem itens nem tentacoes - isso vem nas proximas fatias.

import pgzrun

# --- o labirinto -------------------------------------------------------------
# Cada linha e um texto. '#' e parede, ' ' e caminho livre, 'P' e onde o
# jogador comeca. Mais tarde '.' vira bom habito e 'o' vira oracao.
MAPA = [
    "###############",
    "#.....#.#.....#",
    "#.###.#.#.###.#",
    "#.#.........#.#",
    "#.#.###.###.#.#",
    "#...#..P..#...#",
    "#.#.#.###.#.#.#",
    "#.#.........#.#",
    "#.###.#.#.###.#",
    "#.....#.#.....#",
    "###############",
]

TILE = 32          # tamanho de cada quadradinho, em pixels
RODAPE = 40        # espaco embaixo para uma legenda
VELOCIDADE = 90    # pixels por segundo que o jogador anda

COLUNAS = len(MAPA[0])
LINHAS = len(MAPA)
WIDTH = COLUNAS * TILE
HEIGHT = LINHAS * TILE + RODAPE
TITLE = "Crescendo como Jesus"

COR_FUNDO = (12, 14, 40)
COR_PAREDE = (40, 70, 190)
COR_JOGADOR = (255, 214, 40)
COR_TEXTO = (230, 230, 230)


def eh_parede(col, linha):
    """Diz se o quadradinho (col, linha) e parede ou esta fora do mapa."""
    if linha < 0 or linha >= LINHAS:
        return True
    if col < 0 or col >= COLUNAS:
        return True
    return MAPA[linha][col] == "#"


def centro(col, linha):
    """Posicao em pixels do centro do quadradinho (col, linha)."""
    return col * TILE + TILE // 2, linha * TILE + TILE // 2


def achar_inicio():
    """Procura o 'P' no mapa e devolve (col, linha)."""
    for linha, texto in enumerate(MAPA):
        for col, marca in enumerate(texto):
            if marca == "P":
                return col, linha
    return 1, 1


class Jogador:
    def __init__(self, col, linha):
        self.col = col
        self.linha = linha
        self.x, self.y = centro(col, linha)
        self.dx = 0          # direcao atual (em quadradinhos): -1, 0 ou 1
        self.dy = 0
        self.prox_dx = 0     # direcao que o jogador pediu e esta "guardada"
        self.prox_dy = 0

    def parado(self):
        return self.dx == 0 and self.dy == 0

    def pedir_direcao(self, dx, dy):
        # Reversao imediata: se ja esta andando e pediu o contrario, vira na hora
        # passando a "sair" do quadradinho para onde estava indo.
        if not self.parado() and (dx, dy) == (-self.dx, -self.dy):
            self.col += self.dx
            self.linha += self.dy
            self.dx, self.dy = dx, dy
            self.prox_dx = self.prox_dy = 0
        else:
            self.prox_dx, self.prox_dy = dx, dy

    def _decidir_no_centro(self):
        """Ja esta encaixado no centro de um quadradinho: escolhe a direcao."""
        if (self.prox_dx or self.prox_dy) and not eh_parede(
            self.col + self.prox_dx, self.linha + self.prox_dy
        ):
            self.dx, self.dy = self.prox_dx, self.prox_dy
            self.prox_dx = self.prox_dy = 0
        elif eh_parede(self.col + self.dx, self.linha + self.dy):
            self.dx = self.dy = 0

    def atualizar(self, dt):
        passo = VELOCIDADE * dt

        if self.parado():
            # Encaixado no centro; so comeca a andar se puder ir para a
            # direcao guardada.
            self._decidir_no_centro()
            return

        # Esta andando: avanca em direcao ao centro do proximo quadradinho.
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
            self._decidir_no_centro()

    def desenhar(self):
        screen.draw.filled_circle((self.x, self.y), TILE * 0.4, COR_JOGADOR)


jogador = Jogador(*achar_inicio())


def update(dt):
    jogador.atualizar(dt)


def on_key_down(key):
    if key == keys.LEFT:
        jogador.pedir_direcao(-1, 0)
    elif key == keys.RIGHT:
        jogador.pedir_direcao(1, 0)
    elif key == keys.UP:
        jogador.pedir_direcao(0, -1)
    elif key == keys.DOWN:
        jogador.pedir_direcao(0, 1)


def draw():
    screen.fill(COR_FUNDO)
    for linha, texto in enumerate(MAPA):
        for col, marca in enumerate(texto):
            if marca == "#":
                quadrado = Rect((col * TILE, linha * TILE), (TILE, TILE))
                screen.draw.filled_rect(quadrado, COR_PAREDE)
    jogador.desenhar()
    screen.draw.text(
        "Fatia 2: labirinto e movimento - use as setas",
        midbottom=(WIDTH // 2, HEIGHT - RODAPE // 2),
        color=COR_TEXTO,
        fontsize=22,
    )


pgzrun.go()
