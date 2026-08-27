# CLAUDE.md — Crescendo como Jesus (curso de Python para crianças)

> Este arquivo é um índice de fatos duráveis, não documentação — **nunca ultrapassar 200
> linhas**. Detalhe extenso vai para `docs/` ou `.claude/rules/`, não aqui.

## O que é este repositório

Conteúdo didático (não é um produto de software): 12 módulos de aula (mais um Módulo 0 de
preparação, sem código) ensinando programação a crianças de 9–11 anos através da construção
incremental de um jogo cristão inspirado em Lucas 2:52. Ver
`docs/crescendo-como-jesus-conteudo-programatico.md` para o programa completo.

O jogo de referência em `jogo/` é entregue **pronto e jogável** (não fatiado): serve de gabarito
para os módulos e, principalmente, de **demonstração** para animar os alunos no início do curso
("no fim, o seu vai ficar assim"). Design completo em `docs/design-do-jogo.md`.

## Stack

Python + Pygame Zero, editado e executado no **VS Code**. Thonny, Pydroid 3 (Android) e Google
Colab foram avaliados e descartados como ferramentas do curso — não citar como opção em
conteúdo novo. Motivo de descartar o Thonny: seu Python embutido (muito recente) não tem wheel
pré-compilada de `pygame` disponível, e compilar do zero quebra (`distutils.msvccompiler`
removido) — ver `docs/backlog/status.md`.

## Ambiente

Dois ambientes, ambos Python 3.12 (versão fixa — wheel de `pygame` disponível) e geridos com
`uv`. Nenhum usa o Python global da máquina.

- **Jogo de referência:** venv próprio em `jogo/.venv/` + `jogo/requirements.txt` (versões
  travadas). Setup completo em `jogo/README.md`. É o ambiente que os agentes usam para rodar/
  validar o gabarito (a demo pronta).
- **Lado do aluno:** cada aluno cria o `.venv/` dele na raiz durante o Módulo 1 (ver
  `docs/modulo-01-*/` e `docs/preparacao-ambiente/instalacao_vscode.md`). Não é versionado nem
  mantido aqui.

## Comandos

- validar sintaxe de um exemplo: `jogo\.venv\Scripts\python.exe -m py_compile docs/<modulo>/exemplo.py`
  (o hook em `.claude/settings.json` também roda `py_compile` via `py` a cada edição de `exemplo.py`)
- rodar/validar o jogo: `jogo\.venv\Scripts\python.exe jogo\jogo.py` (abre a janela) ou
  `... -m py_compile jogo\jogo.py` — este ambiente de agente não tem display, então aqui só dá
  pra checar sintaxe/import, não abrir a janela.

## Invariantes (nunca quebrar)

- **Nunca vazar conceito futuro:** um módulo não pode exigir/usar um conceito Python que só é
  ensinado num módulo posterior (ex.: módulo 3 não pode depender de listas, que só vem no
  módulo 5). Ver a tabela de módulos em `docs/crescendo-como-jesus-conteudo-programatico.md`
  para saber o que já foi ensinado até cada ponto.
- Público-alvo é criança de 9–11 anos sem experiência prévia: linguagem simples, sem jargão
  desnecessário.
- Tema bíblico (Lucas 2:52 — sabedoria, estatura, graça com Deus, graça com os homens) é
  consistente em todo o conteúdo; itens bons/ruins do jogo mantêm o espírito catequético do curso.
- Todo `exemplo.py` deve compilar sem erro (`py_compile`) antes de considerar o módulo pronto.

## Estrutura de módulo

Cada módulo tem sua própria pasta (`docs/modulo-NN-slug/`) com quatro arquivos:

- `material-professor.md` — roteiro completo da aula (conceitos, demonstração, atividade,
  desafios, tempo por bloco). Segue um padrão comum mas **não é rígido** — adapte ao conteúdo,
  não force a divisão de minutos.
- `material-aluno.md` — versão enxuta que o aluno acompanha durante a aula.
- `apresentacao.html` — slides autocontidos (sem dependência de internet) da aula.
- `exemplo.py` — código-exemplo do módulo. **Exceção: Módulo 0** não tem `exemplo.py` (não
  ensina Python ainda, é preparação de SO/pastas).

Módulos 0, 1 e 2 já estão no formato novo (falta só `apresentacao.html` dos três — pendente de
propósito, ver `docs/backlog/status.md`). Módulos 3–12 ainda não foram escritos. Ver
`docs/crescendo-como-jesus-conteudo-programatico.md` § Materiais por módulo.

## Onde fica o quê

- regras por área: `.claude/rules/`
- programa completo do curso: `docs/crescendo-como-jesus-conteudo-programatico.md`
- preparação de ambiente: `docs/preparacao-ambiente/instalacao_vscode.md`
  (`instalacao_pydroid.md.obsoleto` é histórico, Pydroid foi descartado)
