# Fusionner une branche

Votre tâche consiste à fusionner une branche dans la branche actuelle à l'aide de Git. Vous devrez basculer sur la branche cible puis fusionner la branche source dans celle-ci. Cela peut être utile lorsque vous voulez combiner les modifications provenant d'une branche `feature-branch-A` dans la branche `master` de votre projet.

Pour ce laboratoire, utilisons le référentiel de `https://github.com/labex-labs/git-playground`. Suivez ces étapes pour fusionner la branche `feature-branch-A` dans la branche `master`:

1. Clonez le référentiel, accédez au répertoire et configurez l'identité:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "votre-nom-d'utilisateur"
git config --global user.email "votre-email"
```

2. Créez une branche `feature-branch-A`. Basculez sur elle:

```shell
git checkout -b feature-branch-A
```

3. Ajoutez "hello,world" au fichier `file2.txt`, ajoutez-le à la zone de préparation et validez-le avec le message "fix file2.txt":

```shell
echo "hello,world" >> file2.txt
git add.
git commit -m "fix file2.txt"
```

4. Basculez sur la branche `master`:

```shell
git checkout master
```

5. Fusionnez la branche `feature-branch-A` dans la branche `master`:

```shell
git merge feature-branch-A
```

6. Résolvez tout conflit qui peut survenir pendant le processus de fusion.

Voici le résultat de l'exécution de `git log`:

```shell
commit e2b80358ae6e4c3b8439cf111a4672a188739290 (HEAD -> master, feature-branch-A)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 18:51:00 2023 +0800

    fix file2.txt
```
