# Supprimer une branche distante

Parfois, vous devrez peut-être supprimer une branche distante qui n'est plus nécessaire. Par exemple, si une branche de fonctionnalité a été fusionnée dans la branche principale, vous pouvez vouloir supprimer la branche de fonctionnalité distante pour nettoyer le référentiel.

Supposons qu'un référentiel GitHub appelé `git-playground` ait été cloné à partir de votre compte GitHub, qui provient d'un fork de `https://github.com/labex-labs/git-playground.git`. Vous voulez supprimer la branche distante nommée `feature-branch` qui n'est plus nécessaire. Voici les étapes pour supprimer la branche distante :

1. Clonez le référentiel, accédez au répertoire et configurez l'identité :
   ```shell
   git clone https://github.com/your-username/git-playground.git
   cd git-playground
   git config --global user.name "your-username"
   git config --global user.email "your-email"
   ```
2. Ajoutez la branche `feature-branch` au référentiel distant `origin` :
   ```shell
   git checkout -b feature-branch
   git push -u origin feature-branch
   ```
3. Utilisez la commande `git branch -r` pour lister toutes les branches distantes.
   ```shell
   git branch -r
   ```
   La sortie devrait inclure la branche distante `feature-branch` :
   ```
   origin/HEAD -> origin/master
   origin/feature-branch
   origin/master
   ```
4. Utilisez la commande `git push -d <remote> <branch>` pour supprimer la branche distante spécifiée `<branch>` sur le `<remote>` donné.
   ```shell
   git push -d origin feature-branch
   ```
   Cette commande supprime la branche distante `feature-branch` sur le référentiel distant `origin`.
5. Utilisez la commande `git branch -r` à nouveau pour vérifier que la branche distante a été supprimée.
   ```shell
   git branch -r
   ```
   La sortie ne devrait pas inclure la branche distante `feature-branch` :
   ```
   origin/HEAD -> origin/master
   origin/master
   ```
