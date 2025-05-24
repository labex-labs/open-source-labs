# Aplicar o Último Stash

Você está trabalhando em um projeto em seu repositório Git e fez algumas alterações que ainda não estão prontas para serem _commitadas_ (confirmadas). No entanto, você precisa mudar para outra _branch_ (ramificação) ou _commit_ (confirmação) para trabalhar em uma funcionalidade diferente. Você não quer perder suas alterações, então decide fazer um _stash_ (armazenamento temporário) delas. Mais tarde, quando estiver pronto para continuar trabalhando em suas alterações, você precisará aplicar o último _stash_ ao seu diretório de trabalho.

Para aplicar o último _stash_ ao seu repositório Git, siga estas etapas:

1.  Clone o repositório Git chamado `https://github.com/labex-labs/git-playground` para sua máquina local.
2.  Navegue até o diretório `git-playground`.
3.  Faça algumas alterações no arquivo `README.md`, por exemplo, escreva "This is a new line" no arquivo `README.md`.
4.  Execute o comando `git stash` para fazer o _stash_ de suas alterações.
5.  Execute o comando `git stash list` para ver uma lista de seus _stashes_. Você deve ver um _stash_ na lista.
6.  Execute o comando `git stash apply` para aplicar o último _stash_ ao seu diretório de trabalho.
7.  Verifique o arquivo `README.md` para ver se suas alterações foram aplicadas.

```shell
git clone https://github.com/labex-labs/git-playground.git
cd git-playground
echo "This is a new line" >> README.md
git stash
git stash list
git stash apply
cat README.md
```

Este é o resultado da execução de `cat README.md`:

```shell
# git-playground
Git Playground
This is a new line
```
