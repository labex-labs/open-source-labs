# Abandonner les modifications non validées

Vous avez apporté quelques modifications à votre référentiel Git local, mais vous ne les avez pas encore validées. Cependant, vous avez décidé que vous ne voulez plus conserver ces modifications et que vous voulez les abandonner. Le problème est de trouver un moyen d'abandonner toutes les modifications non validées sur la branche actuelle.

Pour accomplir ce défi, vous utiliserez le référentiel Git nommé `https://github.com/labex-labs/git-playground` dans le répertoire. Suivez les étapes ci-dessous :

1. Clonez le référentiel sur votre machine locale en utilisant la commande `git clone https://github.com/labex-labs/git-playground.git`.
2. Accédez au référentiel cloné en utilisant la commande `cd git-playground`.
3. Apportez quelques modifications aux fichiers dans le référentiel, mais n'utilisez pas les commandes `echo "hello,world" > hello.txt` et `git add.` pour les valider.
4. Utilisez la commande `git status` pour voir les modifications que vous avez apportées.
5. Abandonnez toutes les modifications non validées en utilisant la commande `git reset --hard HEAD`.
6. Utilisez la commande `git status` à nouveau pour confirmer que toutes les modifications ont été abandonnées.

Voici le résultat de l'exécution de `git status` :

```shell
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```
