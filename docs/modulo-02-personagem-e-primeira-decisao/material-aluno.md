# Módulo 2 — O personagem e a primeira decisão (material do aluno)

## O que vamos aprender hoje

- **Coordenadas**: como dizer onde algo fica na tela (X e Y)
- **Variáveis**: caixinhas que guardam valores
- **`True` / `False`**: verdadeiro ou falso
- **`if` / `else`**: fazer o programa decidir o que fazer

## A ideia de hoje

Nosso personagem vai aparecer na tela e reagir a uma pergunta sobre um hábito cristão — se você
clicar em "Sim" ele cresce e fica feliz, se clicar em "Não" ele fica do mesmo jeito (ou
levemente menor).

Comece a partir do [`exemplo.py`](exemplo.py) deste módulo.

## Sua missão

- [ ] Escolha a cor e o tamanho inicial do seu personagem;
- [ ] Escolha uma pergunta sobre um hábito cristão (ex.: "Você obedeceu aos seus pais hoje?",
      "Você leu a Bíblia hoje?");
- [ ] Programe a reação: **cresce e muda de cor** no "Sim", **fica do mesmo tamanho ou menor**
      no "Não";
- [ ] Mostre uma mensagem diferente para cada resposta.

## Desafios

- **Desafio extra:** adicione uma segunda pergunta que aparece depois da primeira ser respondida.
- **Desafio criativo:** personalize as cores, o formato do personagem e as mensagens.

## Palavras novas

| Termo | O que significa |
|---|---|
| Coordenada | Um endereço na tela: um valor X (horizontal) e um valor Y (vertical) |
| Variável | Uma caixinha com nome que guarda um valor |
| `True` / `False` | Verdadeiro ou falso — os dois únicos valores possíveis de uma resposta lógica |
| `if` / `else` | "Se" isso for verdade, faça uma coisa; "senão", faça outra |
| Evento | Algo que acontece durante o jogo, como um clique na tela |

## Deu erro? Tenta isso primeiro

- **Esqueceu os dois pontos (`:`) depois do `if`/`else`:** confira se colocou `:` no final da linha.
- **O clique não faz nada:** confira se a função se chama exatamente `on_mouse_down`.
- **Usou `=` em vez de `==`:** `=` guarda um valor; `==` compara dois valores — são diferentes!

Ao final, salve seu arquivo `jogo.py`.
