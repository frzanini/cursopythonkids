# Crescendo como Jesus — curso de Python para crianças

Curso de programação com **Python + Pygame Zero** para crianças de **9 a 11 anos**, sem
experiência prévia. Ao longo de 12 módulos (mais um Módulo 0 de preparação), os alunos constroem
— passo a passo — um jogo com temática cristã inspirado em Lucas 2:52:

> "E crescia Jesus em sabedoria, e em estatura, e em graça, para com Deus e os homens." (Lucas 2:52)

O jogo usa a mecânica da cobrinha: o personagem cresce em **estatura espiritual** ao coletar
bons hábitos (🙏 oração, 📖 leitura da Bíblia, ⛪ culto, ❤️ obedecer aos pais, 🤝 ajudar o
próximo) e perde uma vida ao tocar itens que atrapalham (😡 desobediência, 🤥 mentira,
distrações).

Este repositório é **conteúdo didático**, não um produto de software.

## Estrutura

| Caminho | O que é |
|---|---|
| `docs/crescendo-como-jesus-conteudo-programatico.md` | Programa completo do curso (objetivos, metodologia, tabela dos 12 módulos) |
| `docs/modulo-NN-slug/` | Um módulo: `material-professor.md`, `material-aluno.md`, `apresentacao.html`, `exemplo.py` |
| `docs/preparacao-ambiente/` | Guia de instalação do VS Code e do ambiente |
| `docs/backlog/status.md` | Estado do trabalho: o que foi entregue, decidido e o que falta |
| `CLAUDE.md` | Índice de fatos duráveis do projeto (para quem for editar o conteúdo) |

**Status atual:** Módulos 0, 1 e 2 escritos no formato novo (falta `apresentacao.html` dos três).
Módulos 3–12 ainda não escritos. Ver `docs/backlog/status.md`.

## Ambiente de desenvolvimento

Projeto determinístico: **Python 3.12** (versão fixa — tem wheel pré-compilada de `pygame`),
venv próprio e `requirements.txt` com versões exatas.

```sh
py -3.12 -m venv ambiente-virtual/.venv
ambiente-virtual\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

No VS Code: `Ctrl+Shift+P` → *Python: Select Interpreter* → `ambiente-virtual/.venv`.

Validar a sintaxe de um exemplo:

```sh
ambiente-virtual\.venv\Scripts\python.exe -m py_compile docs/<modulo>/exemplo.py
```

Rodar o jogo: no VS Code, com o venv selecionado, botão **Run Python File**.

## Ferramentas do curso

VS Code é a única IDE. Thonny, Pydroid 3 (Android) e Google Colab foram avaliados e descartados
— ver `docs/backlog/status.md` para o histórico.
