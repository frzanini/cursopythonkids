# `jogo/` — jogo de referência ("gabarito")

Código-fonte do jogo completo **"Crescendo como Jesus"** (estilo Pac-Man). É o alvo que o curso
reconstrói: cada `docs/modulo-NN-*/exemplo.py` é um recorte parcial deste jogo.

Design e regras: `docs/design-do-jogo.md`.

## Rodar

Com o venv do projeto selecionado (ver `CLAUDE.md`):

```sh
ambiente-virtual\.venv\Scripts\python.exe jogo\jogo.py
```

Precisa de tela — este ambiente de agente não abre a janela; aqui só dá pra checar sintaxe:

```sh
ambiente-virtual\.venv\Scripts\python.exe -m py_compile jogo\jogo.py
```

## Estrutura

| Caminho | O que é |
|---|---|
| `jogo.py` | O jogo completo e jogável |
| `images/` | Sprites (Pygame Zero procura imagens aqui) |
| `sounds/` | Efeitos sonoros e música |
