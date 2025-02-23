# Obtenez le nom de la branche actuelle

Écrivez une commande qui imprime le nom de la branche actuelle dans un référentiel Git.

Supposons que vous travailliez sur un projet stocké dans le référentiel `https://github.com/labex-labs/git-playground`. Vous avez apporté quelques modifications au fichier `README.md` et vous voulez les commettre à la branche actuelle. Cependant, avant de le faire, vous voulez vous assurer que vous êtes sur la bonne branche.

Pour vérifier la branche actuelle, vous pouvez utiliser la commande suivante :

```shell
git rev-parse --abbrev-ref HEAD
```

Cela imprimera le nom de la branche actuelle dans la console. Par exemple, si vous êtes actuellement sur la branche `master`, la sortie sera :

```shell
master
```

Si vous basculez sur une autre branche, telle que `feature-branch`, la sortie changera en conséquence :

```shell
git checkout -b feature-branch
git rev-parse --abbrev-ref HEAD
```

Cela produira la sortie suivante :

```shell
feature-branch
```
