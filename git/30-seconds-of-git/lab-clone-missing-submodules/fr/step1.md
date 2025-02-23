# Clone les sous-modules manquants

Vous travaillez sur un projet qui contient des sous-modules. Lorsque vous clonez le projet, les sous-modules ne sont pas automatiquement clonés. Cela pose des problèmes lors de la construction ou de l'exécution du projet. Vous devez cloner les sous-modules manquants et passer à des commits corrects.

Pour ce laboratoire, nous utiliserons le référentiel Git nommé `https://github.com/git/git`. Ce référentiel contient des sous-modules qui ne sont pas automatiquement clonés lorsque vous clonez le référentiel.

Pour cloner les sous-modules manquants et passer à des commits corrects, suivez ces étapes :

1. Accédez au répertoire du référentiel :
   ```
   cd git
   ```
2. Initialisez les sous-modules :
   ```
   git submodule update --init --recursive
   ```
3. Passez au commit correct du sous-module, c'est-à-dire à la branche `master` :
   ```
   git submodule foreach git checkout master
   ```
   Voici le résultat final :

```shell
Sous-module'sha1collisiondetection' (https://github.com/cr-marcstevens/sha1collisiondetection.git) enregistré pour le chemin'sha1collisiondetection'
Clonage dans '/home/labex/project/git/sha1collisiondetection'...
Chemin du sous-module'sha1collisiondetection' : mis à jour à '855827c583bc30645ba427885caa40c5b81764d2'
```
