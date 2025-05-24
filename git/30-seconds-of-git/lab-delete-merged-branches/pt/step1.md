# Excluir Branches Merged

Sua tarefa é excluir todas as branches locais que foram merged (fundidas) na branch `master` do repositório `https://github.com/labex-labs/git-playground`.

1.  Mude para o diretório do repositório:

```shell
cd git-playground
```

2.  Liste todas as branches locais que foram merged na `master`:

```shell
git branch --merged
```

Saída:

```
* master
  new-branch
  new-branch-1
  new-branch-2
  new-branch-3
```

3.  Exclua todas as branches merged:

```shell
git branch --merged master | awk '!/^[ *]*$/ && !/master/ {print $1}' | xargs git branch -d
```

4.  Liste todas as branches novamente:

```shell
git branch
```

Este é o resultado final:

```
* master
```
