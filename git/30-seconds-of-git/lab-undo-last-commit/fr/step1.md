# Annuler le dernier commit

Vous venez de commettre des modifications dans votre référentiel Git, mais vous constatez que vous avez fait une erreur. Vous voulez annuler le dernier commit sans perdre aucune des modifications que vous avez apportées. Comment pouvez-vous le faire?

Pour ce laboratoire, utilisons le référentiel de `https://github.com/labex-labs/git-playground`. Suivez ces étapes :

1. Clonez le référentiel, accédez au répertoire et configurez l'identité :

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "votre-nom-d'utilisateur"
git config --global user.email "votre-email"
```

2. Vérifiez l'historique des commits :

```shell
git log
```

3. Annulez le dernier commit, en créant un nouveau commit avec l'inverse des modifications du commit :

```shell
git revert HEAD
```

4. Vérifiez à nouveau l'historique des commits :

```shell
git log
```

Voici le résultat de l'exécution de la commande `git log --oneline` :

```shell
532b49b (HEAD -> master) Revert "Added file2.txt"
d22f46b (origin/master, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```
