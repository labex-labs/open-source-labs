# Descartar Alterações Não Rastreadas

Você está trabalhando em um projeto usando Git e fez algumas alterações no seu diretório de trabalho. No entanto, você percebe que não precisa dessas alterações e deseja descartá-las. Você quer descartar todas as alterações não rastreadas no branch atual.

Para completar este laboratório, você usará o repositório Git chamado `https://github.com/labex-labs/git-playground`. Siga estes passos:

1. Navegue até o diretório do repositório:

```shell
cd git-playground
```

2. Verifique o status do seu diretório de trabalho:

```shell
git status
```

Você deve ver a seguinte saída:

```shell
[object Object]
```

3. Descarte todas as alterações não rastreadas no branch atual:

```shell
git clean -f -d
```

4. Verifique o status do seu diretório de trabalho novamente:

```shell
git status
```

Você deve ver a seguinte saída:

```shell
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

O comando `git clean -f -d` descartou todas as alterações não rastreadas no branch atual.
