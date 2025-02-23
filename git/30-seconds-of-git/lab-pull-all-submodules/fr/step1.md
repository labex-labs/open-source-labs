# Extraire tous les sous-modules à partir du remote

Vous disposez d'un dépôt Git avec des sous-modules qui doivent être mis à jour à partir de leurs remotes respectives. Extraire manuellement chaque sous-module peut être fastidieux et sujet à des erreurs. Vous avez besoin d'un moyen d'extraire tous les sous-modules d'un coup.

En supposant que vous avez un dépôt Git nommé `git` qui contient des sous-modules, vous pouvez extraire tous les sous-modules de leurs remotes respectives en utilisant la commande suivante :

```shell
cd git
git submodule update --recursive --remote
```

Cette commande met à jour tous les sous-modules du dépôt à la dernière version disponible dans leurs remotes respectives.
