# Descartando Alterações Não Confirmadas

Você fez algumas alterações em seu repositório Git local, mas ainda não as confirmou (commit). No entanto, você decidiu que não deseja mais manter essas alterações e deseja descartá-las. O problema é encontrar uma maneira de descartar todas as alterações não confirmadas no branch atual.

Para completar este desafio, você usará o repositório Git chamado `https://github.com/labex-labs/git-playground` diretório. Siga os passos abaixo:

1. Clone o repositório para sua máquina local usando o comando `git clone https://github.com/labex-labs/git-playground.git`.
2. Navegue até o repositório clonado usando o comando `cd git-playground`.
3. Faça algumas alterações nos arquivos do repositório, mas não as confirme usando os comandos `echo "hello,world" > hello.txt` e `git add .`.
4. Use o comando `git status` para ver as alterações que você fez.
5. Descarte todas as alterações não confirmadas usando o comando `git reset --hard HEAD`.
6. Use o comando `git status` novamente para confirmar que todas as alterações foram descartadas.

Este é o resultado da execução de `git status`:

```shell
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```
