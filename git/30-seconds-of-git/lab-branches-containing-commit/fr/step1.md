# Trouver les branches contenant un commit

Vous avez reçu un référentiel Git nommé `https://github.com/labex-labs/git-playground`. Votre tâche consiste à trouver toutes les branches qui contiennent un hachage avec le message de commit "Added file2.txt".

1. Accédez au répertoire du référentiel :

```shell
cd git-playground
```

2. Utilisez la commande `git branch --contains` pour trouver toutes les branches qui contiennent un hachage avec le message de commit "Added file2.txt" :

```shell
git branch --contains d22f46b
```

La sortie devrait être :

```shell
* master
new-branch
new-branch-1
new-branch-2
```
