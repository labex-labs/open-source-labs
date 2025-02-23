# Consulter un résumé bref des commits sans les commits de fusion

Vous avez travaillé sur un projet avec plusieurs autres développeurs, et vous voulez voir un résumé de tous les commits effectués sur le référentiel. Cependant, vous ne voulez pas voir les commits de fusion, car ils ne contiennent pas de modifications réelles dans le code. Comment pouvez-vous voir un résumé de tous les commits, en excluant les commits de fusion?

Pour ce laboratoire, utilisons le référentiel de `https://github.com/labex-labs/git-playground`.

1. Clonez le référentiel, accédez au répertoire et configurez l'identité :

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "votre-nom-d'utilisateur"
git config --global user.email "votre-adresse-email"
```

2. Créez et basculez sur une branche appelée `feature1`, créez un fichier appelé `file.txt` et écrivez `feature 1` dedans, ajoutez-le à la zone de préparation et validez-le avec le message "Ajouter la fonctionnalité 1" :

```shell
git checkout -b feature1
echo "Feature 1" >> file.txt
git add.
git commit -m "Ajouter la fonctionnalité 1"
```

3. Revenez sur la branche `master`, fusionnez la branche `feature1`, désactivez la fusion en avant, enregistrez et quittez sans modifier le texte :

```shell
git checkout master
git merge --no-ff feature1
```

4. Consultez un résumé bref de tous les commits, en excluant les commits de fusion :

```shell
git log --oneline --no-merges
```

Cela affichera une liste de tous les commits effectués sur le référentiel, en excluant tout commit de fusion. La sortie ressemblera à ceci :

```shell
430b986 (feature1) Ajouter la fonctionnalité 1
d22f46b (origin/master, origin/HEAD) Ajouté le fichier file2.txt
cf80005 Ajouté le fichier file1.txt
b00b937 Commit initial
```
