# Effectuer un rebase interactif

Vous travaillez sur un projet avec une équipe de développeurs et vous avez effectué plusieurs commits sur votre branche. Cependant, vous constatez que certains des commits sont inutiles ou doivent être combinés. Vous voulez nettoyer votre historique de commits et le rendre plus organisé.

## Tâches

Pour ce défi, utilisons le référentiel de `https://github.com/labex-labs/git-playground`.

1. Accédez au répertoire.
2. Effectuez un rebase interactif des deux derniers commits.
3. Changez "pick" en "squash" dans le message de commit "Added file2.txt", appuyez sur <kbd>Esc</kbd> puis entrez la commande <kbd>:wq</kbd>, puis appuyez sur <kbd>Entrée</kbd> pour enregistrer vos modifications et quitter l'éditeur. Changez le message de commit en "Added file1.txt and file2.txt" de la même manière et quittez.

En exécutant `git log`, vous obtiendrez un résultat qui ressemblera à ceci :

```shell
commit 7575ded485555c28ecb09487c68e90639bebbe9d (HEAD -> master)
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file1.txt and file2.txt

commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```
