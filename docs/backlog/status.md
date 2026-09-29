# Backlog — Crescendo como Jesus

Mantido pelo agente `backlog-keeper` (`.claude/agents/backlog-keeper.md`). Não é gerado por
git/gh (o repositório não usa controle de versão) — cada linha é registrada manualmente quando
uma entrega/decisão acontece ou uma pendência é identificada.

## Pendente

- **`jogo/jogo.py` — playtest visual pendente.** A 1ª versão completa está escrita (ver Feito
  2026-08-27), mas só foi validada headless (sintaxe + conectividade do mapa + simulação de
  lógica). Falta rodar numa máquina com tela para ajustar velocidades, tamanho da janela,
  legibilidade e "sensação" do movimento. Sprites e sons continuam fora (item à parte).
- **Módulos 6 a 12** ainda não foram escritos — só existem como linha na tabela de
  `docs/crescendo-como-jesus-conteudo-programatico.md` (título + conceitos-chave). **Prioridade
  atual do projeto: revisar e escrever o conteúdo das aulas** (`material-professor.md` +
  `material-aluno.md` + `exemplo.py`).
- **`docs/error/*.png`** (5 imagens) não são referenciadas em nenhum `.md` — decidir se documentam
  algum erro conhecido (e onde entram) ou se podem ser removidas.
- **Divergência entre `docs/design-do-jogo.md` e `docs/crescendo-como-jesus-conteudo-programatico.md`
  sobre o Módulo 2.** O design do jogo diz que o Módulo 2 usa "um evento de tecla", enquanto o
  conteúdo programático diz "eventos de clique". O material reescrito (`docs/modulo-02-personagem-
  e-primeira-decisao/`) seguiu clique (`on_mouse_down`). Falta decidir qual documento está certo e
  alinhar o outro.
- **[FINAL DO PROJETO] Gerar `apresentacao.html` de todos os módulos** — os slides são o **último
  entregável do curso**: definir o template (HTML+CSS puro, autocontido, navegável por teclado) e
  gerar os slides de todos os módulos de uma vez, só depois que o conteúdo de todas as aulas
  estiver escrito e revisado. Não é feito módulo a módulo. Rastreado na issue #12. Removido dos
  materiais por módulo em `CLAUDE.md`, `.claude/rules/modulos.md`,
  `docs/crescendo-como-jesus-conteudo-programatico.md` e `/novo-modulo`.

## Feito

- 2026-09-29 — **Módulos 4 e 5 escritos** (`docs/modulo-04-os-muros-do-labirinto/` e
  `docs/modulo-05-os-bons-habitos-no-mapa/`: `material-professor.md`, `material-aluno.md`,
  `exemplo.py`). Módulo 4: listas, índice, `len`, `for`/`range`, laço dentro de laço, operadores
  relacionais; mapa 20×15 com `TILE = 40` (janela continua 800×600, primeira e última linha vazias
  para os textos), paredes desenhadas do mapa, personagem passa a morar num quadradinho
  (`personagem_coluna`/`personagem_linha`) e anda **um quadradinho por aperto** no `on_key_down` —
  o `update()` do Módulo 3 sai (volta quando as tentações andarem sozinhas); túnel no corredor do
  meio (`<`/`>=`), com o `IndexError` usado de propósito como momento de aprendizado. Módulo 5:
  lista vazia + `append`, pares `(coluna, linha)`, `in`, `remove`, `len == 0`; os `.` do mapa viram
  116 bons hábitos que somem ao coletar, com mensagem de parabéns no fim. Cada módulo começa com um
  experimento em `aula-NN/` no terminal. Sem funções próprias (`def` só no Módulo 8) nem `and`/`or`
  (condições compostas só no Módulo 9). Exemplos validados com `py_compile`, execução headless e
  teste de lógica (parede, túnel, espaço, coleta dos 116).

- 2026-08-28 — **Módulo 2 reescrito no padrão passo-a-passo do Módulo 1**
  (`docs/modulo-02-personagem-e-primeira-decisao/material-aluno.md` e `material-professor.md`).
  Antes só havia o `exemplo.py` pronto, sem passo a passo didático; agora são 6 passos
  incrementais — coordenadas/personagem parado, pergunta na tela, botões Sim/Não com `Rect`,
  detecção de clique com `on_mouse_down(pos)`, guardar a resposta com `global`, mensagem final por
  resposta — cada um com código, explicação do conceito novo e o resultado esperado ao rodar,
  permitindo o aluno fazer a aula sozinho. Conceitos novos documentados: `Rect`, `collidepoint`,
  `filled_circle`, `filled_rect`, `topleft`, `global`, `==` vs `=`, `if`/`elif`/`else`. Continuidade
  com o Módulo 1 corrigida: o `jogo.py` é o mesmo arquivo que evolui o curso inteiro (não um
  projeto novo por aula), então o Módulo 2 passa a reaproveitar explicitamente as variáveis
  `COR_DE_FUNDO` e `COR_DO_TEXTO` criadas no Módulo 1 (antes o `exemplo.py` usava literais soltos
  `"skyblue"`/`"white"`) e preserva o nome do aluno na tela (antes centralizado como boas-vindas,
  agora um texto pequeno no canto inferior esquerdo via `topleft`). Todos os `exemplo.py` tocados
  validados com `py_compile` sem erro.
- 2026-08-28 — **Variável renomeada `NOME_DO_CRIADOR` → `NOME_DO_PECADOR`** em todos os módulos
  existentes (1 e 2): decisão do usuário — "Criador" remete a Deus, e a variável guarda o nome do
  aluno, que segundo o evangelho é pecador. Texto exibido na tela também mudou de
  `"Criado por: "` para `"Pecador: "`. Atualizado em `exemplo.py`, `material-aluno.md` e
  `material-professor.md` dos módulos 1 e 2.
- 2026-08-28 — **Módulo 1 ganhou a seção "De onde vem o `pgzrun`?"** em `material-aluno.md` e
  `material-professor.md` (`docs/modulo-01-conhecendo-a-programacao/`), explicando o conceito de
  biblioteca/pacote e a diferença entre `pgzero` (pacote instalado no `.venv`) e `pgzrun` (a peça/
  módulo importado dele). Inclui diagrama `mermaid` do fluxo Módulo 0 → `.venv` → `import pgzrun`
  → Python procura no `.venv` → acha (`screen`, `draw()`...) ou não acha (`ModuleNotFoundError`).
  Tabelas de "Palavras novas" ganharam "Biblioteca / pacote" e `pgzrun`; mensagens de erro
  esperadas passam a distinguir `screen is not defined` de `ModuleNotFoundError`.
- 2026-08-27 — **`apresentacao.html` adiado para o fim do projeto.** Decisão do usuário: os
  slides deixam de ser um arquivo por módulo e passam a ser o último entregável do curso —
  gerados de uma vez para todos os módulos, com o conteúdo das aulas já revisado. Removidas as
  menções a "4 arquivos por módulo"/slides de `CLAUDE.md`, `.claude/rules/modulos.md`,
  `docs/crescendo-como-jesus-conteudo-programatico.md` e do comando `/novo-modulo`. A issue #12
  virou a tarefa única de "definir template + gerar todos os slides no fim"; nenhuma outra issue
  cita apresentação HTML. Prioridade declarada: revisar/escrever o conteúdo das aulas.
- 2026-08-27 — **Diagrama do ambiente virtual devolvido ao Módulo 0**, agora no contexto
  pasta/projeto: `mermaid` mostrando computador → Python 3.12 (via `uv`) → `.venv/` dentro de
  `crescendo-como-jesus/`, usado por `jogo.py` e por todas as `aula-NN/`. Entrou no
  `material-aluno.md` (seção 5) e no `material-professor.md` (seção 11, ao lado do diagrama
  conceitual "sem venv × com venv").
- 2026-08-27 — **Módulo 0 reescrito: preparação de ambiente completa** (issue #15). Deixa a
  máquina do aluno pronta pra codar — SO/pastas/terminal + instalar `uv`, Python 3.12, VS Code +
  extensão Python, criar a pasta `crescendo-como-jesus/` com `aula-NN/`, o `.venv` e o `pgzero`,
  selecionar o interpretador, e um teste de fumaça. Não ensina nada de Python/jogo. Alinhados:
  `CLAUDE.md`, `docs/crescendo-como-jesus-conteudo-programatico.md` (linhas 0 e 1 da tabela +
  carga horária → ~21h), `docs/design-do-jogo.md`, `docs/preparacao-ambiente/instalacao_vscode.md`
  (guia companheiro), `.claude/rules/modulos.md`. Pendente em #10: tirar as seções de instalação
  (4–7) do Módulo 1, que agora duplicam o Módulo 0.
- 2026-08-27 — **Redefinido o papel de `jogo/`**: além de gabarito, é a **demo pronta** do curso,
  mostrada aos alunos no Módulo 1 como motivação ("propaganda"). Passa a ser desenvolvido como
  entregável completo e independente — não fatiado pelos módulos; a invariante "nunca vazar
  conceito futuro" não se aplica a ele. Atualizado: `CLAUDE.md`, `docs/design-do-jogo.md`,
  `jogo/README.md`, novo `.claude/rules/jogo.md`.
- 2026-08-27 — **1ª versão completa de `jogo/jogo.py` escrita.** Labirinto Pac-Man 19×17 (mapa
  como lista de strings), jogador alinhado à grade (classe-base `AndarilhoDaGrade`), tentações
  com IA simples (aleatório + perseguir, fogem no modo oração, voltam pra casa quando vencidas),
  oração como power-pellet (6 s), estatura, 3 vidas, 4 fases com dificuldade crescente, telas de
  início/intervalo/vitória/derrota com Lucas 2:52. Tudo com formas (sem assets, v1). A tela de
  derrota dá destaque a **JESUS** ("já venceu na cruz") e exorta à perseverança nas disciplinas
  espirituais (Romanos 8:37) — o jogo nunca diz que o pecado venceu. Validado headless
  (`py_compile`, flood-fill do mapa, simulação da lógica das 4 fases). Falta playtest visual.
- 2026-08-22 — Harness do `.claude/` limpo (removido material do projeto PontoWeb30, que estava
  aqui por engano) e reconstruído para este projeto via `harness-architect`.
- 2026-08-22 — Ferramentas do curso definidas: Thonny único (Pydroid e Google Colab descartados).
- 2026-08-22 — Venv próprio criado (`.venv/`, Python 3.12, `pgzero`/`pygame`/`numpy`), gate
  automático de sintaxe (`py_compile`) via hook `PostToolUse` em `exemplo.py`.
- 2026-08-22 — Estrutura de 4 materiais por módulo definida (professor/aluno/apresentação/código)
  e registrada em `CLAUDE.md`, `docs/crescendo-como-jesus-conteudo-programatico.md` e
  `.claude/rules/modulos.md`; `/novo-modulo` atualizado pra gerar os 4 arquivos.
- 2026-08-22 — `CLAUDE.md` revisado; limite de 200 linhas anotado no topo do arquivo.
- 2026-08-22 — Módulos 1 e 2 migrados para o formato novo: `material-professor.md` +
  `material-aluno.md` criados, `.md` único antigo removido, link da tabela em
  `docs/crescendo-como-jesus-conteudo-programatico.md` atualizado. `apresentacao.html` dos dois
  fica pendente por decisão do usuário (gerar só depois do texto revisado).
- 2026-08-22 — **Thonny descartado como ferramenta do curso** — motivo: Python embutido do
  Thonny é recente demais, sem wheel pré-compilada de `pygame` disponível, e a compilação a
  partir do código-fonte quebra (`ModuleNotFoundError: setuptools._distutils.msvccompiler`,
  removido nas versões novas do setuptools). Curso passa a usar **VS Code** com o venv
  determinístico do projeto (Python 3.12 fixo). Atualizado: `CLAUDE.md`,
  `.claude/rules/modulos.md`, `.claude/settings.local.json` (permissão `thonny.org` trocada por
  `code.visualstudio.com`/`pypi.org`), `docs/crescendo-como-jesus-conteudo-programatico.md`
  (Ferramentas + nota de teclado, já que tablet também não é mais usado), comentários dos dois
  `exemplo.py`. Guia `docs/preparacao-ambiente/instalacao_vscode.md` escrito (substitui o
  `instalacao_pydroid.md.obsoleto`, que foi removido).
- 2026-08-22 — Módulo 1 ganhou 3 seções novas no roteiro (professor e aluno): "O jogo que vamos
  construir" (visão geral do projeto final), "O que é uma IDE" e "Pacotes livres e gratuitos"
  (PyPI, `pgzero`). Roteiro de tempo redistribuído para caber as seções novas em 1h30.
- 2026-08-22 — **Módulo 0 criado** (`docs/modulo-00-sistema-operacional-e-pastas/`):
  sistema operacional (Windows/Linux), arquivos, pastas, caminho — preparação antes do Módulo 1,
  fora da sequência de 12 que constroem o jogo (decisão do usuário: virou Módulo 0 em vez de
  renumerar os módulos existentes). Sem `exemplo.py` (não ensina Python ainda) — exceção
  registrada em `.claude/rules/modulos.md` e `CLAUDE.md`. Tabela de módulos e carga horária
  (18h → 19h30) atualizadas em `docs/crescendo-como-jesus-conteudo-programatico.md`.
