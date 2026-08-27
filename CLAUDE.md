# CLAUDE.md — Crescendo como Jesus (curso de Python para crianças)

> Este arquivo é um índice de fatos duráveis, não documentação — **nunca ultrapassar 200
> linhas**. Detalhe extenso vai para `docs/` ou `.claude/rules/`, não aqui.

## O que é este repositório

Conteúdo didático (não é um produto de software): 12 módulos de aula (mais um Módulo 0 de
preparação, sem código) ensinando programação a crianças de 9–11 anos através da construção
incremental de um jogo cristão inspirado em Lucas 2:52. Ver
`docs/crescendo-como-jesus-conteudo-programatico.md` para o programa completo.

## Stack

Python + Pygame Zero, editado e executado no **VS Code**. Thonny, Pydroid 3 (Android) e Google
Colab foram avaliados e descartados como ferramentas do curso — não citar como opção em
conteúdo novo. Motivo de descartar o Thonny: seu Python embutido (muito recente) não tem wheel
pré-compilada de `pygame` disponível, e compilar do zero quebra (`distutils.msvccompiler`
removido) — ver `docs/backlog/status.md`.

## Ambiente

Projeto **determinístico**: venv próprio em `ambiente-virtual/.venv/` (Python 3.12 — versão fixa,
com wheel de `pygame` disponível) + `requirements.txt` com versões exatas (`pip freeze`). Não
usar o Python global da máquina. Criar/recriar: `py -3.12 -m venv ambiente-virtual/.venv` seguido
de `ambiente-virtual\.venv\Scripts\python.exe -m pip install -r requirements.txt`. No VS Code,
selecionar esse venv como interpretador (`Ctrl+Shift+P` → *Python: Select Interpreter* →
`ambiente-virtual/.venv`).

## Comandos

- validar sintaxe de um exemplo: `ambiente-virtual\.venv\Scripts\python.exe -m py_compile docs/<modulo>/exemplo.py`
  (roda automaticamente via hook a cada edição de `exemplo.py`, ver `.claude/settings.json`)
- rodar de fato o jogo: no VS Code, com o venv selecionado como interpretador, botão **Run
  Python File** ou terminal `ambiente-virtual\.venv\Scripts\python.exe jogo.py` — este ambiente de
  agente não tem display, então não dá pra abrir a janela do jogo aqui, só checar sintaxe/import.

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
