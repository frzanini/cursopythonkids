---
description: Regras ao criar ou editar conteúdo de módulo (roteiro .md + exemplo.py)
paths:
  - "docs/modulo-*/**"
---

- Antes de escrever/editar um módulo, releia a tabela de módulos em
  `docs/crescendo-como-jesus-conteudo-programatico.md` para saber exatamente quais conceitos já
  foram ensinados até aquele ponto. Não use nem exija nada além disso no `exemplo.py` ou no
  roteiro (ver invariante "nunca vazar conceito futuro" no `CLAUDE.md`).
- `exemplo.py` roda no **VS Code** com Pygame Zero (`import pgzrun` no topo, `pgzrun.go()` no
  final). Para validar (`py_compile`), use o venv do jogo (`jogo/.venv/`); na aula, o aluno roda
  no `.venv/` que ele cria no Módulo 1. Não escreva código que dependa de Thonny, Pydroid/Android
  ou Google Colab — todos descartados como ferramentas do curso.
- Mantenha comentários e textos de tela em português, tom simples e direto para criança de 9-11
  anos.
- **Todo comando ensinado vem com o resultado esperado.** Sempre que o material manda o aluno
  digitar um comando (terminal, `uv`, `git`, etc.), diga logo abaixo o que deve aparecer na tela
  se deu certo (a versão impressa, "a pasta X aparece no explorador", "nenhuma mensagem de
  erro", o prompt mudando para `(.venv)`, etc.) — assim o aluno sabe se pode seguir ou se algo
  falhou.
- Ao introduzir um item novo do jogo (hábito bom/ruim), mantenha coerência com a lista já
  estabelecida em `docs/crescendo-como-jesus-conteudo-programatico.md` (🙏📖⛪❤️🤝 vs 😡🤥
  distrações) — não invente categoria nova sem atualizar esse documento também.
- Cada módulo tem 2 arquivos de conteúdo + código: `material-professor.md` (roteiro completo),
  `material-aluno.md` (versão enxuta que o aluno segue) e `exemplo.py`. `material-aluno.md` nunca
  deve conter as notas de condução que só interessam ao professor (tempo por bloco, dicas de como
  explicar) — isso fica só no `material-professor.md`. O `apresentacao.html` (slides) **não** é
  feito por módulo: é o último entregável do curso, gerado para todos os módulos de uma vez no
  fim do projeto, com o conteúdo das aulas já revisado (issue #12). Não crie `apresentacao.html`
  ao escrever um módulo novo. **Exceção: Módulo 0** (`modulo-00-sistema-operacional-e-pastas/`) não
  tem `exemplo.py` — é preparação de ambiente (SO, pastas, terminal, `uv`/Python 3.12/VS Code,
  criação do `.venv` e da pasta `crescendo-como-jesus/` com `aula-NN/`), não ensina Python ainda.
- Do Módulo 1 em diante, **não** repita passos de instalação de ambiente — a máquina já está
  pronta desde o Módulo 0. Módulos assumem `uv`, Python 3.12, VS Code + extensão Python e o
  `.venv` com `pgzero` já instalados e o interpretador selecionado.
