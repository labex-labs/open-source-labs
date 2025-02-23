# Renommer une branche distante

Pour terminer ce laboratoire, vous utiliserez le référentiel Git `git-playground` de votre compte GitHub, qui provient d'un fork de `https://github.com/labex-labs/git-playground.git`. Veuillez décocher "Copier seulement la branche master" lors du forking.

Vous disposez d'un référentiel Git nommé `https://github.com/your-username/git-playground`. Vous avez créé une branche nommée `feature-branch` et l'avez poussée sur le distant. Maintenant, vous voulez renommer la branche en `new-feature-1` à la fois localement et sur le distant.

1. Clonez le référentiel, accédez au répertoire et configurez l'identité :
   ```shell
   git clone https://github.com/your-username/git-playground.git
   cd git-playground
   git config --global user.name "your-username"
   git config --global user.email "your-email"
   ```
2. Basculez sur la branche nommée `feature-branch` :
   ```shell
   git checkout feature-branch
   ```
3. Renommez la branche à la fois localement et sur le distant :
   ```shell
   git branch -m feature-branch new-feature-1
   git push origin --delete feature-branch
   git push -u origin new-feature-1
   ```
4. Vérifiez que la branche a été renommée :
   ```shell
   git branch -a
   ```

Voici le résultat de l'exécution de `git branch -a` :

```shell
* master
new-feature-1
remotes/origin/HEAD - > origin/master
remotes/origin/master
remotes/origin/new-feature-1
```
