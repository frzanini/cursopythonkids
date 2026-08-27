---
description: Cria a pasta e o esqueleto de um novo módulo (roteiro, material do aluno, apresentação, exemplo.py) a partir dos módulos anteriores
argument-hint: "<número> <slug-curto>"
---

# /novo-modulo — scaffold de módulo novo

1. Leia `docs/crescendo-como-jesus-conteudo-programatico.md` — confirme o número do módulo, o
   título e a linha da tabela de módulos, e liste os conceitos **já ensinados até o módulo
   anterior** (isso define o teto do que este módulo pode usar).
2. Leia o `exemplo.py` do módulo anterior — o novo `exemplo.py` parte de lá, não do zero.
3. Crie `docs/modulo-$ARGUMENTS/` com:
   - `material-professor.md` — roteiro completo seguindo o padrão dos módulos existentes
     (Duração/Ferramentas, Conceitos, Parte do jogo, Roteiro em blocos de tempo, Desafios,
     Revisão), adaptando livremente o que não se encaixar.
   - `material-aluno.md` — versão enxuta derivada do roteiro, só o que o aluno acompanha
     (sem tempo por bloco nem notas de condução do professor).
   - `apresentacao.html` — slides autocontidos (sem CDN/internet) resumindo os conceitos e a
     parte do jogo do módulo.
   - `exemplo.py` — evoluindo o exemplo do módulo anterior, usando só conceitos já liberados.
4. Rode `jogo\.venv\Scripts\python.exe -m py_compile docs/modulo-$ARGUMENTS/exemplo.py` e conserte até
   compilar limpo.
5. Atualize a tabela de módulos em `docs/crescendo-como-jesus-conteudo-programatico.md` com o
   link do novo módulo.
