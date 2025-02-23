# Supprimer un sous-module

Vous disposez d'un référentiel Git qui inclut un sous-module nommé `sha1collisiondetection`. Vous souhaitez supprimer ce sous-module de votre référentiel.

Pour ce laboratoire, nous utiliserons le référentiel Git nommé `https://github.com/git/git`. Ce référentiel inclut un sous-module nommé `sha1collisiondetection`.

Pour supprimer le sous-module `sha1collisiondetection` du référentiel, suivez ces étapes :

1. Ouvrez votre terminal et accédez au répertoire racine de votre référentiel Git :
   ```
   cd git
   ```
2. Exécutez la commande suivante pour désenregistrer le sous-module `sha1collisiondetection` :
   ```
   git submodule deinit -f -- sha1collisiondetection
   ```
3. Exécutez la commande suivante pour supprimer le répertoire du sous-module `sha1collisiondetection` :
   ```
   rm -rf.git/modules/sha1collisiondetection
   ```
4. Exécutez la commande suivante pour supprimer l'arborescence de travail du sous-module `sha1collisiondetection` :
   ```
   git rm -f sha1collisiondetection
   ```

Après ces étapes, le sous-module `sha1collisiondetection` sera supprimé de votre référentiel Git. Si vous exécutez la commande `git submodule status`, vous ne recevrez aucune information concernant le sous-module.
