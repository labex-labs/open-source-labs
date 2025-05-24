# Aplicar um "stash" (armazenamento temporário)

Você está trabalhando em uma branch de funcionalidade no repositório `git-playground` e precisa mudar para outra branch para trabalhar em uma correção de bug. No entanto, você tem algumas alterações que ainda não estão prontas para serem commitadas. Você quer salvar essas alterações e mudar para a outra branch. Depois de terminar a correção do bug, você quer aplicar o "stash" e continuar trabalhando em sua branch de funcionalidade.

As alterações foram armazenadas no "stash" na branch `feature-branch`, e a mensagem do "stash" é "my changes" (minhas alterações).

1. Mude para o diretório `git-playground`:

```shell
cd git-playground
```

2. Mude para a branch `master` e faça o "stash" após corrigir o bug, a mensagem do "stash" é "fix the bug" (corrigir o bug). Corrija o bug atualizando o conteúdo do arquivo `file1.txt` para "hello,world":

```shell
git checkout master
echo "hello,world" > file1.txt
git stash save "fix the bug"
```

3. Mude para a branch `feature-branch`, veja a lista de "stashes" e aplique o "stash" cuja informação é "my changes":

```shell
git checkout feature-branch
git stash apply stash@{1}
```

Este é o conteúdo do arquivo `README.md`:

```
# git-playground
Git Playground
some changes
```

Você deve ver que as alterações que você fez antes de fazer o "stash" agora foram aplicadas.
