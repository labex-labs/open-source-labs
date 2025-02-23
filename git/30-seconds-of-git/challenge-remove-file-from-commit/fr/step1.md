# Supprimer un fichier du dernier commit

Vous avez ajouté un fichier au dernier commit que vous n'avez pas l'intention d'inclure. Vous voulez supprimer le fichier du dernier commit sans changer son message.

## Tâches

Pour ce défi, utilisons le référentiel de `https://github.com/labex-labs/git-playground`. Supposons que vous ayez un référentiel Git nommé `git-playground` avec un fichier nommé `file2.txt` que vous avez accidentellement ajouté au dernier commit.

1. Accédez au répertoire du référentiel et configurez votre identité GitHub.
2. Supprimez le `file2.txt` spécifié de l'index.
3. Mettez à jour le contenu du dernier commit, sans changer son message.

Après avoir exécuté ces commandes, le fichier `file2.txt` sera supprimé du dernier commit sans changer son message.

Voici ce qui se passe lorsque vous supprimez `file2.txt` du contrôle de version Git :

```shell
On branch master

Changes to be committed:
(use "git restore --staged <file>..." to unstage)
deleted: file2.txt

Untracked files:
(use "git add <file>..." to include in what will be committed)
file2.txt
```
