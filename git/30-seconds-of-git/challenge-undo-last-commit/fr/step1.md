# Annuler le dernier commit

Vous venez de commettre des modifications dans votre référentiel Git, mais vous réalisez que vous avez fait une erreur. Vous voulez annuler le dernier commit sans perdre aucune des modifications que vous avez effectuées. Comment pouvez-vous le faire?

## Tâches

Pour ce défi, utilisons le référentiel de `https://github.com/labex-labs/git-playground`.

1. Vérifiez l'historique des commits.
2. Annulez le dernier commit, en créant un nouveau commit avec l'inverse des modifications du commit.

Voici le résultat de l'exécution de la commande `git log --oneline` :

```shell
532b49b (HEAD -> master) Revert "Added file2.txt"
d22f46b (origin/master, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```
