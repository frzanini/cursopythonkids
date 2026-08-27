# Como preparar o computador (VS Code)

Este guia serve para preparar o computador antes da aula de Python. Precisa de **computador**
(Windows/Mac/Linux) — o curso não usa mais tablet/celular.

## 0. Verificar o que já está instalado

Antes de instalar qualquer coisa, abra o terminal e confira o que a máquina já tem:

```
python --version
code --version
uv --version
```

Cada comando que já existir mostra uma versão; o que não existir dá erro de "comando não
encontrado" — normal, é só seguir os passos abaixo para instalar. Verificar antes evita
reinstalar algo que já está pronto.

## 1. Instalar o `uv` (gerenciador de Python e de ambientes virtuais)

O **`uv`** é uma ferramenta que junta, num só programa, instalação de versões do Python, criação
de ambiente virtual (venv) e instalação de pacotes — é o que vamos usar no curso.

- **Windows (PowerShell):**
  ```
  powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```
- **Linux:**
  ```
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

Feche e abra o terminal de novo, depois confirme:
```
uv --version
```

> **`pyenv` é parecido:** existe também o `pyenv`, uma ferramenta bem conhecida pra instalar e
> trocar entre várias versões do Python na mesma máquina. Ele resolve só a parte da versão do
> Python — a criação do venv e a instalação de pacotes ainda ficariam por conta de `venv`/`pip`
> separadamente. Usamos `uv` no curso porque ele faz as três coisas (versão do Python + venv +
> pacotes) com os mesmos comandos, mas se você já usa `pyenv` no seu dia a dia, ele funciona bem
> para gerenciar a versão do Python também.

## 2. Instalar o Python 3.12 (com o `uv`)

Com o `uv` instalado, pedir a versão certa do Python é um único comando — não precisa baixar
instalador nenhum:

```
uv python install 3.12
```

Confirme que instalou:
```
uv python list
```
(deve aparecer uma linha com `3.12` marcada como instalada)

> Por que 3.12 e não a versão mais nova? O `pygame` (usado pelo Pygame Zero) só publica
> instalação pronta (wheel) para algumas versões do Python. Uma versão nova demais pode não ter
> wheel disponível e travar a instalação — usar 3.12 evita esse problema.

## 3. Instalar o VS Code (pelo terminal)

- **Windows:**
  ```
  winget install -e --id Microsoft.VisualStudioCode
  ```
- **Linux (Debian/Ubuntu):**
  ```
  sudo snap install code --classic
  ```

Feche e abra o terminal de novo (o comando `code` só aparece depois disso), depois confirme:
```
code --version
```

Abra o VS Code (digite `code` no terminal, ou pelo menu Iniciar/de aplicativos) e instale a
extensão **Python** (da Microsoft) pelo ícone de extensões na barra lateral (ou `Ctrl+Shift+X`,
buscar "Python").

> **Sem `winget`/`snap` disponível?** Baixe o instalador manualmente em
> https://code.visualstudio.com — o resultado final é o mesmo, só muda o jeito de instalar.

## 4. Abrir a pasta do projeto e criar o ambiente virtual (venv) com `uv`

O projeto usa um **venv** (ambiente virtual) próprio, pra não instalar nada no Python global do
computador. Isso deixa o ambiente **determinístico** — todo mundo usa exatamente as mesmas
versões de pacote.

1. Abra a pasta do projeto no VS Code: pelo terminal, `cd` até a pasta e digite `code .` (ou,
   sem terminal, **File > Open Folder...** dentro do VS Code).
2. Abra o terminal integrado (**Terminal > New Terminal**, ou `` Ctrl+` ``).
3. Crie o venv com a versão certa do Python:
   ```
   uv venv --python 3.12 .venv
   ```
4. Instale os pacotes dentro do venv:
   - **Se a pasta já tem um `requirements.txt`** (ex.: projeto já existente, ou passado pelo
     professor): reinstale exatamente as mesmas versões com
     ```
     uv pip install -r requirements.txt
     ```
   - **Se é a primeira vez** (a pasta ainda não tem `requirements.txt`): instale o pacote direto
     e depois gere o arquivo a partir do que ficou instalado:
     ```
     uv pip install pgzero
     uv pip freeze > requirements.txt
     ```
     Esse `requirements.txt` gerado é o que garante que, numa próxima vez ou noutro
     computador, dá pra recriar o ambiente idêntico só com o comando `-r` acima.
5. Selecione o venv como interpretador do VS Code: `Ctrl+Shift+P` → **"Python: Select
   Interpreter"** → escolher o que aparece com `.venv` (geralmente já vem marcado como
   "Recommended"). Isso grava a configuração automaticamente num `.vscode/settings.json`, sem
   precisar editar nada à mão.

## 5. Testar se está tudo funcionando

1. Crie um arquivo `teste.py` com:
   ```python
   print("ambiente pronto para a aula")
   ```
2. Clique no botão ▶ **Run Python File** no canto superior direito (ou `Ctrl+F5`).
3. Se aparecer a frase no terminal, está tudo certo!

## Problemas comuns

- **`winget` não é reconhecido (Windows):** só existe no Windows 10/11 atualizado; se faltar,
  instale o "App Installer" pela Microsoft Store ou baixe o instalador manualmente (ver nota
  acima).
- **`code`/`uv` não é reconhecido logo após instalar:** feche e abra o terminal de novo — o PATH
  só é atualizado numa janela nova.
- **`uv python install 3.12` parece travado/demorado:** ele baixa o Python na primeira vez —
  aguardar; da próxima vez é instantâneo, pois já fica em cache.
- **VS Code não mostra o venv na lista de interpretadores:** confirme que a pasta `.venv` foi
  criada dentro da pasta do projeto aberta no VS Code, e recarregue a janela
  (`Ctrl+Shift+P` → "Developer: Reload Window").
- **Erro ao instalar `pygame` (build falhando):** normalmente é usar uma versão de Python sem
  wheel pronta pro `pygame` — confirme que o venv foi criado com `uv venv --python 3.12`, não
  com uma versão mais nova.
