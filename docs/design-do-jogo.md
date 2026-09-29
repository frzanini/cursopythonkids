# Design do jogo — "Crescendo como Jesus" (estilo Pac-Man)

> Documento-fonte do jogo de referência e da decomposição em módulos. As issues do GitHub
> derivam daqui. Mantido junto com o código; o `backlog-keeper` espelha o estado das issues em
> `docs/backlog/status.md`.

## Visão

Jogo de labirinto no estilo **Pac-Man**, com a temática de Lucas 2:52. A criança anda pelo
labirinto da vida coletando **bons hábitos** e desviando das **tentações**. A **oração** dá
força para vencer as tentações por alguns segundos.

| Elemento Pac-Man | No nosso jogo |
|---|---|
| Pac-Man (jogador) | A criança crescendo em estatura |
| Pastilhas | Bons hábitos: 🙏 oração · 📖 Bíblia · ⛪ culto · ❤️ obedecer · 🤝 ajudar |
| Fantasmas | Tentações / más influências: 😡 desobediência · 🤥 mentira · 😴 preguiça · 📱 distração |
| Power-pellet | 🙏 **Oração** — por ~6 s as tentações fogem e podem ser vencidas |
| Limpar a tela | Encher a vida de virtude → completa a fase |
| Níveis | 4 fases: **Sabedoria → Estatura → Graça com Deus → Graça com os homens** |

O versículo (Lucas 2:52) aparece na tela inicial e na tela de vitória.

## Jogo de referência / demo (pasta `jogo/`)

Todo o código-fonte do jogo mora em **`jogo/`** na raiz:

```
jogo/
  jogo.py        # o jogo completo, jogável
  images/        # sprites (entram depois; pgzero procura aqui)
  sounds/        # efeitos e música (entram depois)
  README.md      # como rodar
```

Tem **dois papéis**:

1. **Demo motivacional** — é um jogo **completo e jogável**, mostrado pronto aos alunos logo no
   começo do curso (Módulo 1) como "propaganda": eles veem onde vão chegar e se animam a
   construir o seu. Por isso é desenvolvido **até o fim, de uma vez** — não acompanha o ritmo
   fatiado dos módulos.
2. **Gabarito** — é o alvo que o curso reconstrói por partes; cada `docs/modulo-NN/exemplo.py`
   é um recorte parcial deste jogo.

Os módulos nunca "cortam" o `jogo/jogo.py` para o estado de uma aula — o fatiamento vive só nos
`exemplo.py`. A invariante "nunca vazar conceito futuro" (`CLAUDE.md`) vale para os `exemplo.py`,
**não** para `jogo/jogo.py`.

### Regras

- **Labirinto**: 1 mapa fixo, desenhado à mão como lista de strings (`#` parede, `.` bom hábito,
  `o` oração, ` ` vazio, `P` início do jogador, `T` início da tentação). Tile de ~20 px.
- **Jogador**: move alinhado à grade nas 4 direções; a próxima direção fica "guardada" e é
  aplicada quando dá pra virar. Não atravessa parede.
- **Tentações (IA simples)**: em cada cruzamento escolhem direção — na maior parte das vezes
  aleatória, com uma probabilidade `p` de perseguir (andar na direção do jogador). Nunca dão
  meia-volta. Respeitam parede.
- **Colisões**:
  - jogador × bom hábito → some, **+10 de estatura**.
  - jogador × oração → entra em **modo oração** por ~6 s (tentações ficam "assustadas" e fogem).
  - jogador × tentação, **sem** modo oração → perde 1 vida, posições reiniciam.
  - jogador × tentação, **com** modo oração → tentação é vencida, volta pra casa, ganha pontos.
- **Fase completa**: todos os bons hábitos coletados → próxima fase (mesmo mapa; +velocidade,
  +1 tentação, itens repopulados).
- **Vidas**: começa com 3. Zerou → tela de derrota. Completou as 4 fases → tela de vitória.
- **Telas**: inicial (título + versículo + "aperte ENTER") · jogo (HUD: estatura, vidas, nome da
  fase) · vitória · derrota.

### Restrições técnicas

- **Pygame Zero**: `import pgzrun` no topo, `pgzrun.go()` no fim; `WIDTH`/`HEIGHT`, `draw()`,
  `update(dt)`, `on_key_down`.
- Roda com o venv próprio do jogo em `jogo/.venv/` (Python 3.12; ver `jogo/README.md`). Tem que
  passar `py_compile`.
- Comentários e textos de tela em **português**, tom para criança de 9–11 anos.
- v1 desenha tudo com formas (`Rect`, `screen.draw.filled_circle`) e cores — sem assets. Sprites
  e sons entram como item separado do backlog.

## Decomposição em módulos (básico → avançado)

Cada módulo é uma capacidade concreta do jogo. Ordem respeita a invariante **"nunca vazar
conceito futuro"** (ver `CLAUDE.md`). Substitui a tabela atual (baseada em Snake) em
`docs/crescendo-como-jesus-conteudo-programatico.md`.

O **Módulo 4** é o mais pesado em conceito: listas + `for` precisam ser ensinados ali, porque o
mapa do labirinto é uma lista de strings e desenhá-lo exige percorrê-la. Espera-se que a teoria
tome boa parte da aula e que a construção do labirinto se complete no Módulo 5 (de propósito mais
leve, servindo de reforço) — a atividade do Módulo 4 pode continuar no encontro seguinte.

| # | Módulo | Conceitos novos | Parte do jogo |
|---|---|---|---|
| 0 | Conhecendo o computador | SO, arquivos, pastas, caminho | *(preparação — não constrói o jogo)* |
| 1 | Conhecendo a programação | algoritmo, IDE, PyPI/`pgzero`, instalar VS Code + Pygame Zero | Primeira janela (`WIDTH`/`HEIGHT`, cor de fundo, título) |
| 2 | O personagem e a primeira decisão | coordenadas X/Y, booleano, `if`/`else`, um evento de tecla | A criança aparece na tela e reage a uma tecla |
| 3 | Movimentando o personagem | teclado (`keyboard`/`on_key_down`), atualizar posição em `update()` | Anda nas 4 direções (livre, ainda sem parede) |
| 4 | Os muros do labirinto | **listas**, laço `for`, ler o mapa de uma grade (lista de strings), operadores relacionais | Paredes desenhadas a partir do mapa; não atravessa parede nem sai da tela |
| 5 | Os bons hábitos no mapa | reforço de listas/`for`; remover item de uma lista ao coletar | Vários itens espalhados pelo mapa; somem ao coletar |
| 6 | A estatura (pontuação) | contadores, texto/HUD na tela | Placar de estatura sobe ao coletar |
| 7 | As tentações entram | `random`, movimento aleatório nos cruzamentos | Um inimigo que anda sozinho pelo labirinto |
| 8 | Encostar na tentação | **funções** (`def`), sistema de vidas, tela de derrota | Perde vida ao encostar; game over ao zerar |
| 9 | A força da oração | estado com tempo (`dt`/timer), condições compostas | Power-pellet: tentações fogem e são vencidas |
| 10 | Tentação mais esperta | perseguição (mover em direção ao jogador), lista de tentações | Várias tentações, mistura aleatório + perseguir |
| 11 | Fases e vitória | estados do jogo, condição de fim de fase | 4 fases temáticas com dificuldade crescente + vitória |
| 12 | Personalização e apresentação final | revisão geral, criatividade | Trocar cores/itens/labirinto, som, identidade do aluno |

### Como o personagem anda, módulo a módulo (decisão de 2026-09-29)

O `jogo/jogo.py` anda **deslizando** entre quadradinhos (`update(dt)`, direção guardada pelas
setas, classes). Isso usa conceitos que chegam tarde (`dt` e `and`/`or` no Módulo 9) ou que o
curso nunca ensina (classes, `set`). Os `exemplo.py` chegam perto em três etapas:

| Módulos | Movimento do jogador | Por que dá nesse ponto |
|---|---|---|
| 4–6 | **Um quadradinho por aperto** de seta, no `on_key_down`; o `update()` do Módulo 3 sai | Só precisa de lista e `!=`: "tem parede ali?" é olhar uma letra do `MAPA` |
| 7–8 | **Anda sozinho** na direção escolhida, um quadradinho a cada N quadros (contador); a seta só troca a direção guardada e ela é aplicada quando o lado não é parede. O `update()` volta | Contador é do Módulo 6; a tentação do Módulo 7 usa **o mesmo** jeito de andar, com `random` |
| 9+ (opcional) | **Desliza** suave entre os quadradinhos, como a referência | `dt`/tempo chega no Módulo 9 |

Ponto fraco aceito: até o Módulo 7 o movimento pula de `TILE` em `TILE` e segurar a seta não
repete o passo.

## Organização na máquina do aluno

O aluno trabalha numa pasta própria (fora deste repo). Layout que o curso ensina:

```
crescendo-como-jesus/        <- pasta do aluno (a "raiz" dele)
  .venv/                     <- UM ambiente virtual, criado no Módulo 0 (uv, Python 3.12)
  jogo.py                    <- o projeto que cresce a aula toda, na raiz (nasce no Módulo 1)
  images/  sounds/           <- assets do jogo
  aula-01/  aula-02/  ...    <- uma subpasta por aula, para os testes soltos daquela aula
```

- **Um `.venv` só**, na raiz da pasta do aluno, criado e selecionado no VS Code **no Módulo 0**;
  serve o `jogo.py` e todas as subpastas `aula-NN/`. As subpastas de aula **não** têm `.venv`.
- O **jogo** mora na **raiz** da pasta do aluno (espelha o repo, onde o gabarito roda a partir de
  `jogo/`). O Pygame Zero resolve `images/`/`sounds/` relativo ao script, então cada `aula-NN/`
  que precise de assets usa os seus.
- Subpastas nomeadas `aula-01`, `aula-02`, ... (não `modulo-NN`, para não confundir com os
  `docs/modulo-NN/` deste repo).

Toda a preparação de ambiente (instalar `uv`/Python/VS Code, criar a pasta, o `.venv` e instalar
o `pgzero`) é feita no **Módulo 0** — ver issue #15. O guia
`docs/preparacao-ambiente/instalacao_vscode.md` é o companheiro seco desse módulo. O Módulo 1 (e
seguintes) assume a máquina pronta e não repete passo de instalação.

### Impacto no conteúdo já escrito

- **Módulo 0** — reescrito para cobrir a preparação de ambiente completa (issue #15) e a
  estrutura de pastas `crescendo-como-jesus/` + `aula-NN/`.
- **`docs/crescendo-como-jesus-conteudo-programatico.md`** — reescrever a descrição do jogo
  (Snake → Pac-Man), a tabela de módulos (acima) e a lista de itens bons/ruins; registrar que o
  **jogo pronto é demonstrado no Módulo 1** (bloco de demonstração).
- **Módulo 1** — ajustar a seção "O jogo que vamos construir" para o Pac-Man cristão, incluir a
  **demonstração do jogo pronto** (rodar `jogo/jogo.py` na aula) como gancho de motivação, e
  **remover as seções de instalação de ambiente** (uv, Python, venv, Pygame Zero), que passaram
  para o Módulo 0 — ver issue #15.
- **Módulo 2** — ajustar as partes que descrevem o personagem/decisão no contexto do jogo novo.
- **`CLAUDE.md`** — trocar "mecânica da cobrinha" pela de labirinto; apontar o código-fonte do
  jogo para `jogo/jogo.py` (hoje diz `jogo.py` na raiz); conferir invariantes.
- **`.claude/rules/modulos.md`** — atualizar a lista de itens (inclui 😴 preguiça, 📱 distração).
