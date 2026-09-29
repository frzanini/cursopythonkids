# Crescendo como Jesus

Curso de programação com Python para crianças de 9 a 11 anos, sem experiência prévia. Ao longo de 12 módulos (mais um Módulo 0 de preparação de ambiente), os alunos constroem — passo a passo — um jogo com temática cristã inspirado em Lucas 2:52:

> "E crescia Jesus em sabedoria, e em estatura, e em graça, para com Deus e os homens." (Lucas 2:52)

O jogo é um **labirinto no estilo Pac-Man**: a criança anda pelo "labirinto da vida" coletando **bons hábitos** — 🙏 Oração, 📖 Leitura da Bíblia, ⛪ Ir ao culto, ❤️ Obedecer aos pais, 🤝 Ajudar o próximo —, que aumentam sua **estatura espiritual**, e desviando das **tentações** — 😡 desobediência, 🤥 mentira, 😴 preguiça, 📱 distração —, que custam uma vida ao serem tocadas. A **oração** funciona como "power-pellet": por alguns segundos as tentações fogem e podem ser vencidas. São 4 fases: **Sabedoria → Estatura → Graça com Deus → Graça com os homens**. O versículo de Lucas 2:52 aparece na tela inicial e na de vitória.

Usa **Python + Pygame Zero** no **VS Code**, com um venv próprio (ambiente determinístico —
versões de pacote fixas, ver `requirements.txt`).

O jogo de referência completo vive na pasta `jogo/` e é **demonstrado pronto e jogável no Módulo 1**, como motivação ("é aqui que você vai chegar"). Design completo em `docs/design-do-jogo.md`.

## Objetivo geral

Ensinar os fundamentos básicos da programação por meio da criação de um jogo digital com valores cristãos.

## Objetivos específicos

Ao final do curso, o aluno deverá ser capaz de:

- compreender o que é um programa e um algoritmo;
- escrever e executar códigos em Python;
- utilizar variáveis, números, textos e valores lógicos;
- utilizar decisões (`if` / `else`);
- criar repetições (laços);
- criar e utilizar funções;
- trabalhar com listas e laços (`for`);
- compreender coordenadas na tela (eixos X e Y);
- capturar comandos do teclado;
- movimentar personagens por um labirinto e detectar colisões;
- usar o acaso com `random`;
- controlar o tempo e os estados do jogo (telas e fases);
- criar sistemas de estatura (pontuação) e vidas;
- organizar um pequeno projeto de programação;
- testar e corrigir erros no código (debugging).

## Ferramentas

- **Python 3.12** (versão fixa — garante wheel pronta de `pygame` disponível)
- **Pygame Zero** (`pgzero`)
- **VS Code** (com a extensão Python) — única IDE do curso
- Venv próprio do projeto (`.venv/`), com `requirements.txt` de versões fixas — ambiente
  determinístico, igual em qualquer computador
- Imagens e sons produzidos/selecionados para fins educacionais
- **Computador** (Windows/Mac/Linux) com teclado — o curso não usa mais tablet/celular; o
  teclado já é nativo do computador, sem necessidade de pareamento.

Pydroid 3 (Android), Thonny e Google Colab foram avaliados e descartados como ferramentas do
curso — ver `docs/backlog/status.md` para o histórico.

## Carga horária

- 12 módulos que constroem o jogo, 1 aula de 1h30 cada → 18h; + **Módulo 0** de preparação de
  ambiente (~3h, pode ser 2 encontros) → **~21h totais**
- Estrutura sugerida por aula:
  - 15 min — apresentação do conceito
  - 20 min — demonstração
  - 40 min — atividade prática
  - 10 min — desafio
  - 5 min — revisão e salvamento do projeto

## Metodologia (Descobrir → Experimentar → Construir → Compartilhar)

1. **Descobrir** — o professor apresenta um problema ligado à próxima parte do jogo.
2. **Experimentar** — os alunos testam pequenos comandos e observam resultados.
3. **Construir** — o conceito aprendido é aplicado na construção do jogo.
4. **Compartilhar** — os alunos mostram o resultado e explicam o que fizeram.

O erro é tratado como parte natural do aprendizado: o professor ajuda o aluno a investigar o que aconteceu, o que deveria acontecer, onde está o problema e qual mudança pode resolvê-lo — em vez de simplesmente corrigir o código por ele.

## Sistema de desafios (por módulo)

- **Missão principal** — necessária para concluir a parte do jogo daquele módulo.
- **Desafio extra** — para quem terminar mais rápido.
- **Desafio criativo** — personalização livre.

## Avaliação

Contínua, observando: participação, compreensão dos conceitos, capacidade de testar soluções, organização do código, colaboração, criatividade, evolução ao longo do curso e funcionamento do projeto final. Sem prova tradicional.

## Projeto final

O jogo final deve possuir: tela inicial (com o versículo), um **labirinto** com paredes, personagem controlado pelo teclado que não atravessa parede, **bons hábitos** espalhados pelo mapa que aumentam a estatura, **tentações** que se movem sozinhas e custam uma vida ao encostar, a **oração** como poder temporário (as tentações fogem e podem ser vencidas), placar de estatura, sistema de vidas, condição de vitória e de derrota, pelo menos uma fase (o alvo são 4) e identidade visual própria do aluno.

## Módulos

| # | Módulo | Conceitos-chave | Parte do jogo |
|---|--------|------------------|----------------|
| 0 | [Preparando o computador](modulo-00-sistema-operacional-e-pastas/material-professor.md) | SO, Windows/Linux, arquivos, pastas, caminho, terminal; Python 3.12, `uv`, VS Code + extensão, pacote/PyPI, ambiente virtual; estrutura de pastas do aluno | *(preparação de ambiente — não constrói o jogo)* |
| 1 | [Conhecendo a programação](modulo-01-conhecendo-a-programacao/material-professor.md) | jogo do curso, o que é programa e algoritmo, sequência de execução, primeira janela (`WIDTH`/`HEIGHT`, cor de fundo, título) | Primeira janela do jogo |
| 2 | [O personagem e a primeira decisão](modulo-02-personagem-e-primeira-decisao/material-professor.md) | objetos, coordenadas, eixos X/Y, valores lógicos, `if`/`else`, eventos de clique | Personagem aparece e reage a uma decisão (sim/não) |
| 3 | [Movimentando o personagem](modulo-03-movimentando-o-personagem/material-professor.md) | teclado (`keyboard`/`on_key_down`), atualizar posição em `update()` | Anda nas 4 direções (livre, ainda sem parede) |
| 4 | [Os muros do labirinto](modulo-04-os-muros-do-labirinto/material-professor.md) | **listas**, laço `for`, ler o mapa de uma grade (lista de strings), operadores relacionais | Paredes desenhadas a partir do mapa; o jogador não atravessa parede nem sai da tela |
| 5 | [Os bons hábitos no mapa](modulo-05-os-bons-habitos-no-mapa/material-professor.md) | reforço de listas e `for`; tirar um item da lista ao coletar | Bons hábitos espalhados pelo mapa; somem quando o jogador passa por cima |
| 6 | A estatura (pontuação) | contadores, texto/HUD na tela | Placar de estatura sobe a cada hábito coletado |
| 7 | As tentações entram | `random`, movimento aleatório nos cruzamentos | Um inimigo que anda sozinho pelo labirinto |
| 8 | Encostar na tentação | funções (`def`), sistema de vidas, tela de derrota | Perde vida ao encostar; game over ao zerar as vidas |
| 9 | A força da oração | estado com tempo (`dt`/timer), condições compostas | Power-pellet: as tentações fogem e podem ser vencidas |
| 10 | Tentação mais esperta | perseguição (mover em direção ao jogador), lista de tentações | Várias tentações, misturando andar aleatório e perseguir |
| 11 | Fases e vitória | estados do jogo, condição de fim de fase | 4 fases temáticas com dificuldade crescente + tela de vitória |
| 12 | Personalização e apresentação final | revisão geral, criatividade | Trocar cores/itens/labirinto, som, identidade visual do aluno |

> O **Módulo 4** carrega dois conceitos de peso (listas e laço `for`) antes de usá-los para ler o
> mapa do labirinto. É esperado que a parte teórica ocupe boa parte da aula e que a construção do
> labirinto termine de assentar no Módulo 5 — que é, de propósito, mais leve em conceito novo e
> serve de reforço. Não tem problema a atividade prática do Módulo 4 "vazar" para o encontro
> seguinte.

Cada módulo tem sua própria pasta com o material do professor, o material do aluno e o
`exemplo.py` da aula (ver "Materiais por módulo" abaixo). Os slides (`apresentacao.html`) são
entregues no fim do projeto, não por módulo.

## Materiais por módulo

Cada `docs/modulo-NN-slug/` deve conter:

- **`material-professor.md`** — roteiro completo da aula (conceitos, demonstração passo a passo,
  atividade prática, desafios, tempo por bloco, resultado esperado). É o material de referência
  do professor para conduzir a aula; hoje corresponde ao antigo `modulo-NN-slug.md`.
- **`material-aluno.md`** — versão enxuta que o aluno acompanha durante a aula (o que fazer,
  passo a passo, sem as notas de condução que só interessam ao professor).
- **`exemplo.py`** — código-exemplo da aula. Exceção: o Módulo 0 não tem esse arquivo, por não
  ensinar Python ainda.

O **`apresentacao.html`** (slides autocontidos, sem internet, para projetar) é o **último
entregável do curso**: será gerado de uma vez para todos os módulos no fim do projeto, quando o
conteúdo de todas as aulas estiver revisado (ver `docs/backlog/status.md` e issue #12). Não é
feito módulo a módulo. A prioridade agora é revisar e escrever o conteúdo das aulas.

> Status: módulos 0 a 5 já estão nessa estrutura. Módulos 6–12 ainda não existem.
