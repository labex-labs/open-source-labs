# Trouver des fichiers perdus

Vous avez travaillé sur un projet dans le référentiel `git-playground`. Cependant, vous avez remarqué que certains fichiers manquent et vous n'êtes pas sûr de quand ils ont été supprimés ou de la manière de les récupérer. Votre tâche consiste à utiliser Git pour trouver tout fichier perdu et tout commit dans le référentiel.

1. Clonez le référentiel `git-playground` :

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Accédez au répertoire et configurez l'identité :

```shell
cd git-playground
git config --global user.name "votre-nom-d'utilisateur"
git config --global user.email "votre-email"
```

3. Créez et basculez sur une branche nommée `one-branch`, supprimez `file2.txt` et validez avec le message "Supprimer file2" :

```shell
git checkout -b one-branch
git rm file2.txt
git commit -m "Supprimer file2"
```

4. Revenez sur la branche `master` et supprimez la branche `one-branch` :

```shell
git checkout master
git branch -D one-branch
```

5. Exécutez la commande `git fsck --lost-found` pour trouver tout fichier perdu et tout commit :

```shell
git fsck --lost-found
```

6. Vérifiez le répertoire `.git/lost-found` pour voir si des fichiers perdus ont été récupérés :

```shell
ls.git/lost-found
```

7. Si des fichiers perdus ont été trouvés, examinez-les pour déterminer s'ils sont les fichiers manquants.

Voici le résultat de l'exécution de la commande `ls.git/lost-found` :

```shell
commit
```
