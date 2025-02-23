# Supprimer un dépôt (stash) Git

Vous disposez d'un référentiel Git nommé `https://github.com/labex-labs/git-playground`. Vous avez créé un dépôt en utilisant la commande `git stash save "my stash"`. Maintenant, vous voulez supprimer ce dépôt car vous n'en avez plus besoin.

1. Accédez au répertoire du référentiel en utilisant la commande `cd git-playground`.
2. Liste tous les dépôts en utilisant la commande `git stash list`. Vous devriez voir le dépôt que vous venez de créer.
3. Supprimez le dépôt en utilisant la commande `git stash drop stash@{0}`.
4. Liste à nouveau tous les dépôts en utilisant la commande `git stash list`.

Le dépôt que vous venez de supprimer ne devrait plus être présent.
