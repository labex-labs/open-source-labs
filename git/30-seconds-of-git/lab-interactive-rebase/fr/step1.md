# Effectuer un rebase interactif

Vous travaillez sur un projet avec une équipe de développeurs et vous avez effectué plusieurs commits sur votre branche. Cependant, vous constatez que certains des commits sont inutiles ou doivent être combinés. Vous voulez nettoyer votre historique de commits et le rendre plus organisé.

Pour ce laboratoire, utilisons le référentiel de `https://github.com/labex-labs/git-playground`. Suivez ces étapes :

1. Accédez au répertoire :
   ```shell
   cd git-playground
   ```
2. Effectuez un rebase interactif des deux derniers commits :
   ```shell
   git rebase -i HEAD~2
   ```
   Le fichier de rebase interactif s'ouvrira dans votre éditeur de texte par défaut. Vous pouvez modifier l'ordre des commits et l'action à effectuer pour chacun d'entre eux (pick, squash, drop, reword etc.).
3. Changez "pick" en "squash" dans le message de commit "Added file2.txt", appuyez sur <kbd>Esc</kbd> puis entrez la commande <kbd>:wq</kbd>, puis appuyez sur <kbd>Entrée</kbd> pour enregistrer vos modifications et quitter l'éditeur, changez le message de commit en "Added file1.txt and file2.txt" de la même manière et quittez.
4. Si des conflits de fusion se produisent ou si vous devez apporter des modifications, vous pouvez continuer le rebase lorsque vous êtes prêt en utilisant `git rebase --continue` ou l'abandonner en utilisant `git rebase --abort`.

Exécuter `git log` vous donnera un résultat ressemblant à ceci :

```shell

```
