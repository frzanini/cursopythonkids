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
  final), usando o venv `ambiente-virtual/.venv/` do projeto como interpretador. Não escreva código que dependa
  de Thonny, Pydroid/Android ou Google Colab — todos descartados como ferramentas do curso.
- Mantenha comentários e textos de tela em português, tom simples e direto para criança de 9-11
  anos.
- Ao introduzir um item novo do jogo (hábito bom/ruim), mantenha coerência com a lista já
  estabelecida em `docs/crescendo-como-jesus-conteudo-programatico.md` (🙏📖⛪❤️🤝 vs 😡🤥
  distrações) — não invente categoria nova sem atualizar esse documento também.
- Cada módulo tem 4 arquivos: `material-professor.md` (roteiro completo), `material-aluno.md`
  (versão enxuta que o aluno segue), `apresentacao.html` (slides autocontidos) e `exemplo.py`.
  `material-aluno.md` e `apresentacao.html` nunca devem conter as notas de condução que só
  interessam ao professor (tempo por bloco, dicas de como explicar) — isso fica só no
  `material-professor.md`. **Exceção: Módulo 0** (`modulo-00-sistema-operacional-e-pastas/`) não
  tem `exemplo.py` — é preparação (SO, pastas), não ensina Python ainda.
