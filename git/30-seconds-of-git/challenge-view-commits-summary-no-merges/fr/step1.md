# Afficher un résumé court des commits sans les commits de fusion

Vous travaillez sur un projet avec plusieurs autres développeurs, et vous voulez voir un résumé de tous les commits effectués sur le référentiel. Cependant, vous ne voulez pas voir les commits de fusion, car ils ne contiennent pas de modifications réelles dans le code. Comment pouvez-vous afficher un résumé de tous les commits, en excluant les commits de fusion?

## Tâches

Pour ce défi, utilisons le référentiel de `https://github.com/labex-labs/git-playground`.

1. Accédez au répertoire et configurez l'identité.
2. Créez et basculez sur une branche appelée `feature1`, créez un fichier appelé `file.txt` et écrivez "feature 1" dedans, ajoutez-le à la zone de préparation et validez-le avec le message "Ajouter la fonctionnalité 1".
3. Revenez sur la branche `master`, fusionnez la branche `feature1`, désactivez la fusion en avant, enregistrez et quittez sans modifier le texte.
4. Affichez un résumé court de tous les commits, en excluant les commits de fusion.

Cela produira une liste de tous les commits effectués sur le référentiel, en excluant tout commit de fusion. La sortie ressemblera à ceci :

```shell
430b986 (feature1) Add feature 1
d22f46b (origin/master, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```
