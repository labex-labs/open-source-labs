# Visualizar Branches Mescladas

Sua tarefa é imprimir uma lista de todas as branches locais mescladas no repositório Git chamado `https://github.com/labex-labs/git-playground`. Você precisará usar o comando `git branch -a --merged` para exibir a lista de branches mescladas. Depois de obter a lista, você deverá ser capaz de navegar por ela usando as setas do teclado e sair pressionando <kbd>Q</kbd>.

1. Navegue até o diretório do repositório:

```shell
cd git-playground
```

2. Visualize a lista de branches mescladas:

```shell
git branch -a --merged
```

Este é o resultado final:

```
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/feature-branch
  remotes/origin/master
```
