# Desfazer um Commit

Suponha que você tenha feito um commit em seu repositório Git, mas percebe que ele contém um erro. Você quer desfazer o commit sem reescrever o histórico do seu repositório. Como você pode fazer isso?

Para demonstrar como desfazer um commit, vamos usar o repositório de `https://github.com/labex-labs/git-playground`. Siga estes passos:

1. Clone o repositório, navegue até o diretório e configure a identidade:
   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   git config --global user.name "seu-nome-de-usuário"
   git config --global user.email "seu-email"
   ```
2. Visualize o histórico de commits:
   ```
   git log
   ```
   Você deve ver uma lista de commits, cada um com um identificador único (uma longa sequência de letras e números).
3. Selecione um commit com a mensagem "Added file1.txt" e copie seu identificador.
4. Reverta o commit usando o comando `git revert`:
   ```
   git revert <commit>
   ```
   Substitua `<commit>` pelo identificador do commit que você deseja reverter.
5. Git abrirá um editor de texto e permitirá que você insira uma mensagem de commit, deixando a mensagem padrão no lugar.
6. Salve e feche o editor de texto.
7. Visualize o histórico de commits novamente:
   ```
   git log
   ```
   Você deve ver um novo commit que desfaz as alterações feitas pelo commit original.

Este é o resultado da execução do comando `git log`:

```
commit 0d01f357a798f8960959546750d89a7e56a04a44 (HEAD -> master)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Mon Jul 24 21:52:43 2023 +0800

    Revert "Added file1.txt"

    This reverts commit cf80005e40a3c661eb212fcea5fad06f8283f08f.
```
