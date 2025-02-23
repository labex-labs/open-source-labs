# Annuler une validation

Supposons que vous ayez effectué une validation dans votre référentiel Git, mais que vous réalisez qu'elle contient une erreur. Vous voulez annuler la validation sans réécrire l'historique de votre référentiel. Comment pouvez-vous le faire?

Pour démontrer comment annuler une validation, utilisons le référentiel de `https://github.com/labex-labs/git-playground`. Suivez ces étapes :

1. Clonez le référentiel, accédez au répertoire et configurez l'identité :
   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   git config --global user.name "votre-nom-d'utilisateur"
   git config --global user.email "votre-email"
   ```
2. Affichez l'historique des validations :
   ```
   git log
   ```
   Vous devriez voir une liste de validations, chacune avec un identifiant unique (une longue chaîne de lettres et de chiffres).
3. Sélectionnez une validation avec le message "Added file1.txt" et copiez son identifiant.
4. Annulez la validation à l'aide de la commande `git revert` :
   ```
   git revert <commit>
   ```
   Remplacez `<commit>` par l'identifiant de la validation que vous voulez annuler.
5. Git ouvrira un éditeur de texte et vous laissera entrer un message de validation, en laissant le message par défaut en place.
6. Enregistrez et fermez l'éditeur de texte.
7. Affichez à nouveau l'historique des validations :
   ```
   git log
   ```
   Vous devriez voir une nouvelle validation qui annule les modifications apportées par la validation initiale.

Voici le résultat de l'exécution de la commande `git log` :

```
commit 0d01f357a798f8960959546750d89a7e56a04a44 (HEAD -> master)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Mon Jul 24 21:52:43 2023 +0800

    Revert "Added file1.txt"

    This reverts commit cf80005e40a3c661eb212fcea5fad06f8283f08f.
```
