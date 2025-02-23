# Éditer le fichier de configuration Git

En tant que développeur, vous devrez peut-être modifier le fichier de configuration Git pour personnaliser le comportement de Git. Le fichier de configuration Git est un fichier texte brut qui contient des paramètres sous forme de paires clé-valeur. Le fichier peut être édité à l'aide de n'importe quel éditeur de texte, mais Git fournit un éditeur de texte intégré qui peut être utilisé pour modifier le fichier de configuration.

Dans cet exemple, nous utiliserons le référentiel Git nommé `https://github.com/labex-labs/git-playground` pour démontrer comment éditer le fichier de configuration Git.

1. Ouvrez le terminal et accédez au répertoire du référentiel Git :

```shell
cd git-playground
```

2. Utilisez la commande suivante pour ouvrir le fichier de configuration Git dans l'éditeur de texte Git :

```shell
git config --global -e
```

3. La commande ci-dessus ouvrira le fichier de configuration Git dans l'éditeur de texte Git par défaut. Vous pouvez modifier le paramètre pour que le nom d'utilisateur soit `labex_git` et l'adresse e-mail de l'utilisateur soit `labex_git@example.com`.
4. Une fois que vous avez effectué les modifications nécessaires, appuyez sur <kbd>Esc</kbd> puis entrez la commande <kbd>:wq</kbd>, puis appuyez sur <kbd>Entrée</kbd> pour enregistrer vos modifications et quitter l'éditeur.

Voici le résultat après la fin :

```shell
# This is Git's per-user configuration file.
[user]
name = labex_git
email = labex_git@example.com
# Please adapt and uncomment the following lines:
#   name =
#   email = labex@64b8c76af840a200973e9d16.(none)
```
