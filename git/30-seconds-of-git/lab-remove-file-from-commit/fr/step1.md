# Supprimer un fichier du dernier commit

Vous avez ajouté un fichier au dernier commit que vous n'auriez pas dû inclure. Vous voulez supprimer le fichier du dernier commit sans modifier son message.

Pour cet exercice, utilisons le référentiel de `https://github.com/labex-labs/git-playground`. Supposons que vous ayez un référentiel Git nommé `git-playground` avec un fichier nommé `file2.txt` que vous avez accidentellement ajouté au dernier commit. Voici les étapes pour supprimer le fichier du dernier commit :

1. Clonez le référentiel, accédez au répertoire et configurez l'identité :

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "votre-nom-d'utilisateur"
git config --global user.email "votre-adresse-email"
```

2. Utilisez `git rm --cached <fichier>` pour supprimer le `<fichier>` spécifié de l'index :

```shell
git rm --cached file2.txt
```

3. Utilisez `git commit --amend` pour mettre à jour le contenu du dernier commit, sans modifier son message :

```shell
git commit --amend --allow-empty
```

Si le commit est un commit vide après la suppression du fichier, utilisez `--allow-empty`, sinon vous pouvez le laisser de côté.

Après avoir exécuté ces commandes, le fichier `file2.txt` sera supprimé du dernier commit sans modifier son message.

Voici ce qui se passe lorsque vous supprimez `file2.txt` du contrôle de version Git :

```shell
Sur la branche master

Changements à commettre :
(utilisez "git restore --staged <fichier>..." pour annuler le prélèvement)
supprimé : file2.txt

Fichiers non suivis :
(utilisez "git add <fichier>..." pour inclure dans ce qui sera commis)
file2.txt
```
