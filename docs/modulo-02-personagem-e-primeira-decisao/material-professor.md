# Módulo 2 — O personagem e a primeira decisão (material do professor)

**Duração:** 1h30 · **Ferramentas:** Python, VS Code

## Conceitos

- Objetos na tela e coordenadas (eixo X e eixo Y)
- Variáveis
- Valores lógicos (`True` / `False`)
- Comparação e decisão (`if` / `else`)
- Eventos de clique/toque

## Parte do jogo

O personagem aparece na tela e reage (cresce um pouco e sorri, ou encolhe e fica triste) à
resposta de uma pergunta sobre um hábito cristão — a primeira "decisão" programada no jogo.

## Por que lógica já no módulo 2

Em vez de aprender `if`/`else` de forma isolada, a criança já vê o próprio personagem do jogo
reagindo a uma decisão lógica — o mesmo tipo de lógica que, lá no Módulo 8, vai controlar o
crescimento de estatura ao coletar bons hábitos. Aqui a decisão é feita por clique (sim/não),
sem precisar do teclado ainda (isso vem no Módulo 3).

## Roteiro da aula

### 1. Apresentação do conceito (15 min)

- Relembrar rapidamente o jogo criado no Módulo 1.
- Explicar **coordenadas**: a tela é uma grade de números, o eixo X vai da esquerda pra direita,
  o eixo Y de cima pra baixo. Toda posição na tela é um par `(x, y)`.
- Explicar **valores lógicos**: no dia a dia, muita coisa só pode ser "verdade" ou "mentira" —
  "hoje é domingo" (verdadeiro ou falso), "eu orei hoje" (verdadeiro ou falso). No Python, isso
  vira `True` e `False`.
- Explicar **decisão**: assim como na vida a gente decide o que fazer dependendo da resposta
  ("se eu orar hoje, eu cresço um pouquinho"), o programa também pode decidir o que mostrar na
  tela usando `if` (se) e `else` (senão).

### 2. Demonstração (20 min)

- Mostrar o personagem (um círculo colorido, por enquanto — as imagens definitivas vêm depois)
  na posição `(WIDTH/2, HEIGHT/2)`, explicando o que são `WIDTH` e `HEIGHT`.
- Adicionar uma pergunta na tela ("Você orou hoje?") com dois botões: **Sim** e **Não**.
- Escrever ao vivo o código que detecta o clique (ver [`exemplo.py`](exemplo.py)) e usa
  `if`/`else` para decidir como o personagem reage.
- Rodar e clicar nos dois botões pra mostrar as duas reações diferentes.

### 3. Atividade prática (40 min)

Cada aluno deve:

1. Escolher a cor e o tamanho inicial do seu personagem;
2. Escolher a pergunta sobre um hábito cristão (ex.: "Você obedeceu aos seus pais hoje?", "Você
   leu a Bíblia hoje?");
3. Programar a reação de **crescer e mudar de cor** quando a resposta for "Sim", e **ficar do
   mesmo tamanho** (ou levemente menor) quando for "Não";
4. Exibir uma mensagem de acordo com a resposta (ex.: "Muito bem! Continue assim!" / "Que tal
   fazer isso hoje?").

Usar o arquivo [`exemplo.py`](exemplo.py) como ponto de partida.

### 4. Desafios (10 min)

- **Missão principal:** personagem na tela + pergunta com Sim/Não + reação visual diferente para
  cada resposta.
- **Desafio extra:** adicionar uma segunda pergunta que aparece depois da primeira ser respondida.
- **Desafio criativo:** personalizar as cores, o formato do personagem e o texto das mensagens.

### 5. Revisão e salvamento (5 min)

- Cada aluno salva o arquivo `jogo.py`.
- Roda rápida: 2 ou 3 alunos mostram as duas reações do personagem pros colegas.

## Fundamentos trabalhados

- Variáveis
- Coordenadas (posição X, Y)
- Valores lógicos (`True` / `False`)
- Comparação e decisão (`if` / `else`)
- Eventos (clique do mouse/toque na tela)

## Resultado esperado

O personagem aparece na tela, uma pergunta é exibida com dois botões, e o personagem reage de
forma diferente (visualmente) dependendo da resposta escolhida.

## Vocabulário novo para os alunos

| Termo | Explicação simples |
|---|---|
| Coordenada | Um endereço na tela, formado por um valor X (horizontal) e um valor Y (vertical) |
| Variável | Uma caixinha com nome que guarda um valor (número, texto, ou verdadeiro/falso) |
| `True` / `False` | Os dois únicos valores possíveis de uma resposta lógica: verdadeiro ou falso |
| `if` / `else` | "Se" isso for verdade, faça uma coisa; "senão", faça outra |
| Evento | Algo que acontece durante o jogo, como um clique ou toque na tela |

## Erros comuns e como ajudar

- **Esqueceu dos dois pontos (`:`) depois do `if`/`else`:** o Python vai acusar erro de sintaxe;
  mostrar a linha exata do erro.
- **Indentação errada dentro do `if`/`else`:** reforçar que tudo que pertence ao "se" precisa
  estar alinhado com o mesmo recuo.
- **Clique não é detectado:** conferir se a área do botão (retângulo) está calculada
  corretamente e se a função de clique foi nomeada como o Pygame Zero espera
  (`on_mouse_down`).
- **Comparação usando `=` em vez de `==`:** um erro clássico — `=` guarda um valor, `==` compara
  dois valores.
