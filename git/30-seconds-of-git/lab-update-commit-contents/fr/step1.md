# Éditer le dernier commit

Vous venez de commettre quelques modifications dans votre référentiel Git, mais vous réalisez que vous avez oublié d'inclure un fichier ou d'apporter une petite modification. Vous ne voulez pas créer un nouveau commit uniquement pour cette petite modification, mais vous ne voulez pas non plus modifier le message du commit. Comment pouvez-vous éditer le dernier commit sans changer son message?

Pour démontrer comment éditer le dernier commit, utilisons le référentiel de `https://github.com/labex-labs/git-playground`.

1. Clonez le référentiel, accédez au répertoire et configurez l'identité :

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "votre-nom-d'utilisateur"
git config --global user.email "votre-email"
```

2. Découvrez que vous avez oublié d'inclure un fichier ou d'apporter une petite modification. Ajoutez le texte "Nouveau contenu" à la fin du fichier `README.md`. Ajoutez toutes les modifications préparées au dernier commit, sans changer son message :

```shell
echo "Nouveau contenu" >> README.md
git add README.md
git commit --amend --no-edit
```

3. Vérifiez que le dernier commit inclut désormais les modifications que vous avez effectuées :

```shell
git show HEAD
```

Voici le contenu du commit tardif :
![Affichage du contenu du commit mis à jour](../assets/challenge-update-commit-contents.png)
