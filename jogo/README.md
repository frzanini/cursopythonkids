# `jogo/` — jogo de referência ("gabarito") e demo

Código-fonte do jogo completo **"Crescendo como Jesus"** (estilo Pac-Man). Tem dois papéis: é a
**demo pronta** mostrada aos alunos no início do curso (para animá-los a estudar) e o **alvo**
que o curso reconstrói — cada `docs/modulo-NN-*/exemplo.py` é um recorte parcial dele. Por ser
demo, é desenvolvido até o fim, não fatiado como os módulos.

Design e regras: `docs/design-do-jogo.md`.

O jogo de referência tem **ambiente próprio** em `jogo/.venv/` (Python 3.12), separado do `.venv`
que cada aluno cria durante o Módulo 1. Assim o gabarito roda sempre igual, independente do
ambiente da turma.

---

## Como subir o jogo (Windows / PowerShell)

Pré-requisitos: **[uv](https://docs.astral.sh/uv/)** instalado e **Python 3.12** disponível
(`uv python install 3.12` resolve se faltar).

### 1. Criar o ambiente virtual do jogo

Na raiz do repositório:

```powershell
uv venv --python 3.12 jogo\.venv
```

Isso cria a "caixa" `jogo\.venv\` com um Python 3.12 só para o jogo. A pasta é ignorada pelo Git
(`.gitignore`) — cada máquina cria a sua.

### 2. Instalar as dependências (versões travadas)

```powershell
uv pip install --python jogo\.venv\Scripts\python.exe -r jogo\requirements.txt
```

Instala exatamente `pgzero`, `pygame` e `numpy` nas versões de `jogo/requirements.txt`.

### 3. Ativar o ambiente (uma vez por terminal)

Os passos 1 e 2 só precisam rodar **uma vez por máquina**. No dia a dia, basta ativar o
ambiente uma vez em cada terminal novo:

```powershell
jogo\.venv\Scripts\Activate.ps1
```

O prompt passa a mostrar `(.venv)` no começo. A partir daí, `python` já é o Python do jogo —
não precisa mais repetir o caminho `jogo\.venv\Scripts\python.exe` em cada comando. Para sair,
`deactivate`.

> Se o PowerShell reclamar de *execution policy*, rode uma vez:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.

### 4. Rodar o jogo

Com o ambiente ativado:

```powershell
python jogo\jogo.py
```

Abre a janela do jogo. Controles: **setas do teclado**.

### 5. (opcional) Só checar a sintaxe, sem abrir a janela

```powershell
python -m py_compile jogo\jogo.py
```

Útil em máquina sem tela (servidor, CI). Não abre janela, só valida o código.

> **Sem ativar**, todos os comandos acima também funcionam prefixando o caminho completo:
> `jogo\.venv\Scripts\python.exe jogo\jogo.py`. É o que os agentes usam em terminais não
> interativos.

---

## No VS Code

1. `Ctrl+Shift+P` → **Python: Select Interpreter**.
2. Escolher o que aponta para `jogo\.venv` (às vezes é preciso *"Enter interpreter path"* →
   `jogo\.venv\Scripts\python.exe`).
3. Abrir `jogo/jogo.py` e usar o botão **Run Python File**.

---

## macOS / Linux

Mesmos passos, trocando as barras e o caminho do Python:

```sh
uv venv --python 3.12 jogo/.venv
uv pip install --python jogo/.venv/bin/python -r jogo/requirements.txt
source jogo/.venv/bin/activate    # ativa (uma vez por terminal)
python jogo/jogo.py
```

---

## Recriar o ambiente do zero

```powershell
Remove-Item -Recurse -Force jogo\.venv
uv venv --python 3.12 jogo\.venv
uv pip install --python jogo\.venv\Scripts\python.exe -r jogo\requirements.txt
```

## Problemas comuns

| Sintoma | Causa provável |
|---|---|
| `No module named 'pgzero'` / `screen is not defined` | interpretador errado — não é o `jogo\.venv` |
| `uv: command not found` | `uv` não instalado ou fora do PATH |
| Janela não abre, sem erro | máquina sem tela (use o `py_compile` do passo 5) |
| `Activate.ps1 ... não pode ser carregado` | execution policy — rode `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |
| `Python 3.12 not found` | rode `uv python install 3.12` |

## Estrutura

| Caminho | O que é |
|---|---|
| `jogo.py` | O jogo completo e jogável |
| `requirements.txt` | Dependências travadas do jogo |
| `.venv/` | Ambiente virtual do jogo (não versionado) |
| `images/` | Sprites (Pygame Zero procura imagens aqui) |
| `sounds/` | Efeitos sonoros e música |
