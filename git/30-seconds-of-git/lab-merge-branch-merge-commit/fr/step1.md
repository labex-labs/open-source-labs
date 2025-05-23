# Fusionner une branche et créer un commit de fusion

En tant que développeur, vous devrez peut-être fusionner une branche dans la branche actuelle, en créant un commit de fusion. Cela peut être un peu difficile si vous n'êtes pas familier avec Git. Le problème est de fusionner une branche dans la branche actuelle, en créant un commit de fusion, en utilisant le référentiel Git nommé `https://github.com/labex-labs/git-playground` dans le répertoire.

Pour ce défi, utilisons le référentiel de `https://github.com/labex-labs/git-playground`.

1. Clonez un référentiel à partir de `https://github.com/labex-labs/git-playground.git` :

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Accédez au répertoire et configurez l'identité :

```shell
cd git-playground
git config --global user.name "votre-nom-d'utilisateur"
git config --global user.email "votre-adresse-email"
```

3. Créez et basculez sur une branche appelée `feature-branch` :

```shell
git checkout -b feature-branch
```

4. Ajoutez "Ceci est une nouvelle ligne." au fichier `README.md`, ajoutez-le à la zone de préparation et validez-le, le message de commit est "Ajouter une nouvelle ligne au README.md" :

```shell
echo "Ceci est une nouvelle ligne." >> README.md
git add.
git commit -am "Ajouter une nouvelle ligne au README.md"
```

5. Basculez sur la branche `master` :

```shell
git checkout master
```

6. Fusionnez la branche `feature-branch` dans la branche `master`, ce qui créera un commit de fusion avec le message "Fusionner feature-branch" :

```shell
git merge --no-ff -m "Fusionner feature-branch" feature-branch
```

Voici le résultat de l'exécution de `git log` :

```shell
[object Object]
```
