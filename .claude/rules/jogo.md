---
description: Regras ao editar o jogo de referência/demo em jogo/
paths:
  - "jogo/**"
---

- `jogo/jogo.py` é a **demo pronta** do curso (mostrada aos alunos no Módulo 1 para motivá-los) e
  o **gabarito** que os módulos reconstroem. Fonte da verdade do design: `docs/design-do-jogo.md`.
- É um entregável **completo e independente**: desenvolva-o até o jogo final do design (itens,
  tentações, oração, vidas, 4 fases, telas), sem limitar a conceitos de nenhum módulo. A
  invariante "nunca vazar conceito futuro" (`CLAUDE.md`) vale para os `docs/modulo-*/exemplo.py`,
  **não** para `jogo/jogo.py`.
- Nunca reduza/fatie `jogo/jogo.py` para o estado de uma aula — o recorte por módulo vive só nos
  `exemplo.py`.
- Comentários e textos de tela em português, tom para criança de 9–11 anos.
- Validar com o venv do jogo: `jogo\.venv\Scripts\python.exe -m py_compile jogo\jogo.py`
  (este ambiente de agente não tem display — dá pra checar sintaxe/import, não abrir a janela).
