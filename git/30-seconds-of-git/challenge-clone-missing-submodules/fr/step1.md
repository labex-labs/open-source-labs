# Clone les sous-modules manquants

Vous travaillez sur un projet qui contient des sous-modules. Lorsque vous clonez le projet, les sous-modules ne sont pas automatiquement clonés. Cela pose des problèmes lors de la construction ou de l'exécution du projet. Vous devez cloner les sous-modules manquants et passer à des commits corrects.

## Tâches

Pour ce défi, nous utiliserons le dépôt Git nommé `https://github.com/git/git`. Ce dépôt contient des sous-modules qui ne sont pas automatiquement clonés lorsque vous clonez le dépôt.

Pour cloner les sous-modules manquants et passer à des commits corrects, suivez ces étapes :

1. Accédez au répertoire du dépôt.
2. Initialisez les sous-modules.
3. Passez à la bonne version du sous-module, c'est-à-dire à la branche `master`.

Voici le résultat final :

```shell
Sous-module'sha1collisiondetection' (https://github.com/cr-marcstevens/sha1collisiondetection.git) enregistré pour le chemin'sha1collisiondetection'
Clonage dans '/home/labex/project/git/sha1collisiondetection'...
Chemin du sous-module'sha1collisiondetection' : mis à jour à '855827c583bc30645ba427885caa40c5b81764d2'
```
