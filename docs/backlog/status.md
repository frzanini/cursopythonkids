# Backlog — Crescendo como Jesus

Mantido pelo agente `backlog-keeper` (`.claude/agents/backlog-keeper.md`). Não é gerado por
git/gh (o repositório não usa controle de versão) — cada linha é registrada manualmente quando
uma entrega/decisão acontece ou uma pendência é identificada.

## Pendente

- **Módulo 0 não está no site.** O "Antes de começar" do mapa só diz "isto foi feito no Módulo
  0"; a instalação (uv, Python 3.12, VS Code, `.venv`) não tem caderno publicado.
- **Sobras da revisão de 2026-11-23 no `material-professor.md`** (o foco foi o material do
  aluno): Módulos 1-2 ainda citam `No module named 'pgzero'`, "`screen is not defined` = falta
  import/go" e `UnboundLocalError` no Módulo 2; Módulo 0 diz que `rmdir` "só remove pasta vazia,
  é por segurança" (falso no PowerShell); Módulo 2 diz "Módulo 8" para a estatura (é o 6).
- **Tabela de módulos × `def`:** a tabela põe "funções (`def`)" no Módulo 8, mas os Módulos 1-3
  já usam `def draw()`, `on_mouse_down(pos)` e `global`. Registrar que antes do 8 são só as
  funções especiais chamadas pelo Pygame Zero.
- **Módulo 2 lista `==` como conceito do dia** sem nenhum código obrigatório que use `==`.
- Pequenas divergências: comentário `uv run jogo.py` nos `exemplo.py` (o curso roda com
  `python jogo.py`/▶); texto do `VERSICULO` difere entre `exemplo.py` do Módulo 1 e o caderno.

- **`jogo/jogo.py` — playtest visual pendente.** A 1ª versão completa está escrita (ver Feito
  2026-08-27), mas só foi validada headless (sintaxe + conectividade do mapa + simulação de
  lógica). Falta rodar numa máquina com tela para ajustar velocidades, tamanho da janela,
  legibilidade e "sensação" do movimento. Sprites e sons continuam fora (item à parte).
- **Módulos 8 a 12** ainda não foram escritos — só existem como linha na tabela de
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

- 2026-11-23 — **Módulos 6 e 7 escritos e publicados** (`docs/modulo-06-a-estatura/`,
  `docs/modulo-07-as-tentacoes-entram/`: `material-professor.md`, `material-aluno.md`,
  `exemplo.py`) + **caderno das Fases 6 e 7** (`cadernos/caderno-de-missoes-modulos-6-7.html`),
  liberadas no mapa (7 de 12). Módulo 6: contador (`estatura = estatura + 10`), `str()` e o
  `TypeError` de propósito, placar com `topleft`/`topright` (`Estatura`, `Faltam`), régua da
  estatura com moldura (`screen.draw.rect`). Módulo 7: `random` (`randint`, `choice`), o
  `update()` volta como relógio (contador de quadros, `ESPERA_PERSONAGEM = 12`), o personagem
  passa a andar sozinho com direção como par e `proxima_direcao` guardada até dar para virar
  (decisão de design de 2026-09-29), e a tentação 😡 (crimson, com olhos) anda sozinha sorteando
  entre os caminhos livres, sem meia-volta (o mapa não tem beco sem saída; conferido por script).
  Validado: os dois `exemplo.py` compilam; aluno simulado seguindo o `material-aluno.md` passo a
  passo no Pygame Zero sem janela (estatura 1160 coletando os 116; 5 `tic`/s; para na parede no
  Passo 2 e vira no Passo 3; tentação 20 mil quadros sem parede nem meia-volta, visitando as 126
  casas); janelinhas do caderno idênticas às telas reais quadro a quadro; quiz, missões, guia,
  links e celular testados no Chrome. O túnel repetido 3× no `update()` é proposital: gancho para
  as funções (`def`) do Módulo 8.

- 2026-11-23 — **Revisão e validação dos Módulos 0-5 (material do aluno + cadernos do site).**
  O `jogo.py` do aluno foi reconstruído passo a passo a partir do `material-aluno.md` (33
  cenários) e rodado no Pygame Zero sem janela, com cliques e teclas simulados; os experimentos
  `listas.py`/`mochila.py` também. Tudo chega no resultado prometido. As janelinhas dos dois
  cadernos foram comparadas no Chrome, quadro a quadro, com as telas reais; quiz, missões, mapa,
  guia lateral, links e layout de celular testados no site publicado. Corrigido:
  - **Módulo 0:** `mkdir` no Windows mostra uma tabela; `rmdir` no PowerShell **pergunta se apaga
    tudo** numa pasta cheia (aviso: responder N); terminal novo com `(.venv)` antes do
    `python aula-01/teste.py`; aviso da Microsoft Store; `winget` com aceite dos termos; pasta do
    curso na pasta do usuário (fora do OneDrive); checklist sem `python --version`.
  - **Onde pôr o código:** regra de ouro "tudo entre o `import pgzrun` e o `pgzrun.go()`" e
    "antes do `pgzrun.go()`" nos passos que criam função (Módulos 1-3 e caderno).
  - **Mensagens de erro reais:** `No module named 'pgzrun'` (não `'pgzero'`); `screen is not
    defined` = linha sem recuo; sem `go()` nada abre; sem `global` no Módulo 2 a tela só não
    muda, mas nos Módulos 3 e 4 o jogo fecha com `UnboundLocalError`; desafio R do Módulo 5 quebra
    na seta, não no R; erros de recuo/`habitos` do Módulo 5.
  - **Módulo 4, passo 3:** trocar as **3 linhas** do `filled_circle` e o `personagem_raio`
    (antes não dito; a bola de raio 40 cobria as paredes).
  - **Acentos nos textos de tela** dos Módulos 3-5 (`Espaço`, `início`, `Parabéns! Você...
    hábitos!`): testado que a fonte do Pygame Zero desenha acentos.
  - **Conceito vazado:** desafio extra do Módulo 3 usava `<`/`>` (Módulo 4); trocado por "correr
    com o Shift" (`keyboard.lshift`, testado).
  - **Cadernos:** segurar a seta não repete o passo (como no Pygame Zero); trecho de código não
    vaza no celular; barra de cima numa linha só no celular; legenda da bola deslizando; mochila
    deixa claro que a recusa é brincadeira.

- 2026-11-23 — **Caderno de missões das Fases 4 e 5 publicado**
  (`cadernos/caderno-de-missoes-modulos-4-5.html`), no mesmo padrão do caderno das Fases 1-3:
  experimento no terminal + passos com código (linhas novas marcadas), janelinha do que deve
  aparecer, missão, quiz, desafios, código completo (idêntico ao `exemplo.py`), palavras novas e
  "deu erro?". Janelinhas interativas novas: laboratório da lista (índice, `len`, `for`, o
  `IndexError` do `habitos[5]`), leitor do mapa (`MAPA[linha][coluna]` ao passar o mouse) e os dois
  `for` desenhando as paredes em câmera lenta, labirinto jogável em três versões (atravessa
  parede / para na parede com o `IndexError` da ponta direita e o índice negativo da esquerda,
  igual ao Python / com túnel), laboratório da mochila (`append`, `in`, `remove`, `ValueError`) e
  coleta dos 116 hábitos com atalho para testar o parabéns. Mapa de missões (`cadernos/index.html`)
  libera as Fases 4 e 5 (5 de 12); o caderno das Fases 1-3 ganhou o link para o novo. Corrigido nos
  dois cadernos: a fonte de código juntava `!=` em `≠` e `>=` em `≥` (ligaduras desligadas).

- 2026-09-29 — **Cadernos publicados no GitHub Pages + mapa de missões** (`cadernos/`, workflow
  `.github/workflows/pages.yml`): caderno das Fases 1-3 com navegação lateral e `index.html` como
  trilha das fases 0-12, lendo o progresso das missões salvo no navegador.

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
