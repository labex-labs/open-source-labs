# Ordenar Branches do Git por Data

Você tem um repositório Git com múltiplos branches, e deseja ordená-los por data. Isso permitirá que você veja quais branches foram atualizados recentemente e quais não foram. Ordenar os branches por data também pode ajudá-lo a identificar branches que podem precisar de atenção ou merge (fusão).

Para este laboratório, vamos usar o repositório de `https://github.com/labex-labs/git-playground`.

1. Clone o repositório para sua máquina local:

```shell
git clone https://github.com/labex-labs/git-playground
```

2. Navegue até o diretório do repositório e configure sua identidade do GitHub:

```shell
cd git-playground
git config --global user.name "seu-nome-de-usuário"
git config --global user.email "seu-email"
```

3. Crie um branch chamado `one`, modifique o código e faça o commit:

```shell
git checkout -b one
touch hello.txt
git add .
git commit -m "hello.txt"
```

4. Mude para o branch chamado `master` e crie um branch chamado `two`:

```shell
git checkout master
git checkout -b two
```

5. Agora, para ordenar os branches por data, use o seguinte comando:

```shell
git branch --sort=-committerdate
```

Isso exibirá uma lista de todos os branches locais e os ordenará com base na data de seu último commit. Você pode usar as setas do teclado para navegar na lista e pressionar <kbd>Q</kbd> para sair.

Este é o resultado final:

![sorted git branches list](../assets/challenge-sort-branches-by-date.png)
