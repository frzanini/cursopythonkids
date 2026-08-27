# Crescendo como Jesus

Curso de programação com Python para crianças de 9 a 11 anos, sem experiência prévia. Ao longo de 12 módulos, os alunos constroem — passo a passo — um jogo com temática cristã inspirado em Lucas 2:52:

> "E crescia Jesus em sabedoria, e em estatura, e em graça, para com Deus e os homens." (Lucas 2:52)

O jogo usa a mesma mecânica da cobrinha (o personagem cresce à medida que coleta itens), mas em vez de comida, o personagem cresce em **estatura espiritual** ao coletar bons hábitos: 🙏 Oração, 📖 Leitura da Bíblia, ⛪ Ir ao culto, ❤️ Obedecer aos pais, 🤝 Ajudar o próximo. Itens que atrapalham (😡 desobediência, 🤥 mentira, distrações) fazem o personagem perder uma vida ao serem tocados.

Usa **Python + Pygame Zero** no **VS Code**, com um venv próprio (ambiente determinístico —
versões de pacote fixas, ver `requirements.txt`).

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
- trabalhar com listas;
- compreender coordenadas na tela (eixos X e Y);
- capturar comandos do teclado;
- movimentar personagens e detectar colisões;
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

- 12 módulos que constroem o jogo + Módulo 0 de preparação (computador/SO/pastas), 1 aula cada,
  1h30 por aula → **19h30 totais**
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

O jogo final deve possuir: tela inicial, personagem controlado pelo teclado, itens bons que fazem o personagem crescer em estatura, itens ruins que custam uma vida, placar de estatura, sistema de vidas, condição de vitória, condição de derrota, pelo menos uma fase e identidade visual própria do aluno.

## Módulos

| # | Módulo | Conceitos-chave | Parte do jogo |
|---|--------|------------------|----------------|
| 0 | [Conhecendo o computador](modulo-00-sistema-operacional-e-pastas/material-professor.md) | sistema operacional, Windows/Linux, arquivos, pastas, caminho | *(preparação — não constrói o jogo)* |
| 1 | [Conhecendo a programação](modulo-01-conhecendo-a-programacao/material-professor.md) | jogo do curso, algoritmo, IDE, pacotes livres, instalação do VS Code e do Pygame Zero | Primeira janela do jogo |
| 2 | [O personagem e a primeira decisão](modulo-02-personagem-e-primeira-decisao/material-professor.md) | objetos, coordenadas, eixos X/Y, valores lógicos, `if`/`else`, eventos de clique | Personagem aparece e reage a uma decisão (sim/não) |
| 3 | Movimentando o personagem | entrada de dados, eventos de teclado | Movimento com as setas |
| 4 | Criando os limites da tela | `if`/`else` (reforço), operadores relacionais | Personagem não sai da tela |
| 5 | O corpo que cresce | listas, repetição | Corpo do personagem (estatura) segue a cabeça |
| 6 | Colisão com o próprio corpo | colisão, posição anterior | Cuidado ao se enrolar sobre os próprios passos |
| 7 | Colocando os bons hábitos no mapa | listas, laços, posição aleatória | Itens: oração, Bíblia, culto, obediência, ajudar o próximo |
| 8 | Criando a estatura (pontuação) | contadores, atualização de texto | Placar de estatura |
| 9 | Itens que atrapalham | condições, eventos | Desobediência, mentira, distrações no mapa |
| 10 | Sistema de vidas | colisão, reinício de posição | Perde vida ao tocar item ruim ou em si mesmo |
| 11 | Vitória, derrota e fases | condições compostas, estados do jogo | Fases: sabedoria, estatura, graça com Deus, graça com os homens |
| 12 | Personalização e apresentação final | revisão geral, criatividade | Finalização e customização |

Cada módulo tem sua própria pasta com três materiais (ver "Materiais por módulo" abaixo) e o
`exemplo.py` da aula.

## Materiais por módulo

Cada `docs/modulo-NN-slug/` deve conter:

- **`material-professor.md`** — roteiro completo da aula (conceitos, demonstração passo a passo,
  atividade prática, desafios, tempo por bloco, resultado esperado). É o material de referência
  do professor para conduzir a aula; hoje corresponde ao antigo `modulo-NN-slug.md`.
- **`material-aluno.md`** — versão enxuta que o aluno acompanha durante a aula (o que fazer,
  passo a passo, sem as notas de condução que só interessam ao professor).
- **`apresentacao.html`** — slides da aula em HTML, autocontido (sem dependência de internet
  durante a aula), para abrir e projetar.
- **`exemplo.py`** — código-exemplo da aula. Exceção: o Módulo 0 não tem esse arquivo, por não
  ensinar Python ainda.

> Status: módulos 0, 1 e 2 migrados para essa estrutura em 2026-08-22 (`apresentacao.html` ainda
> pendente para os três — ver `docs/backlog/status.md`). Módulos 3–12 ainda não existem.
