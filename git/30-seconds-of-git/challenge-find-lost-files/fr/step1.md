# Trouver des fichiers perdus

Vous avez travaillé sur un projet dans le référentiel `git-playground`. Cependant, vous avez remarqué que certains fichiers manquent et vous n'êtes pas sûr de quand ils ont été supprimés ni de la manière de les récupérer. Votre tâche consiste à utiliser Git pour trouver tout fichier et tout commit perdu dans le référentiel.

## Tâches

1. Accédez au répertoire et configurez l'identité.
2. Créez et basculez sur une branche nommée `one-branch`, supprimez `file2.txt` et validez avec le message "Supprimer file2".
3. Revenez sur la branche `master` et supprimez la branche `one-branch`.
4. Trouvez tout fichier et tout commit perdu.
5. Vérifiez le répertoire `.git/lost-found` pour voir si des fichiers perdus ont été récupérés.
6. Si des fichiers perdus ont été trouvés, examinez-les pour déterminer s'ils sont les fichiers manquants.

Voici le résultat de l'exécution de la commande `ls.git/lost-found` :

```shell
commit
```
