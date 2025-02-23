# Appliquer un dépôt (stash)

Vous travaillez sur une branche de fonctionnalité dans le référentiel `git-playground` et vous devez passer à une autre branche pour corriger un bogue. Cependant, vous avez des modifications qui ne sont pas encore prêtes à être validées. Vous voulez sauvegarder ces modifications et passer à l'autre branche. Une fois que vous avez terminé la correction du bogue, vous voulez appliquer le dépôt et continuer à travailler sur votre branche de fonctionnalité.

## Tâches

Les modifications ont été stockées sur la branche `feature-branch`, et le message de dépôt est "mes modifications".

1. Changez au répertoire `git-playground`.
2. Basculez sur la branche `master` et stockez-la après avoir corrigé le bogue, le message de dépôt est "corriger le bogue". Corrigez le bogue en mettant à jour le contenu du fichier `file1.txt` en "hello,world".
3. Basculez sur la branche `feature-branch`, regardez la liste des dépôts, et appliquez le dépôt dont l'information est "mes modifications".

Voici le contenu du fichier `README.md` :

```
# git-playground
Git Playground
some changes
```

Vous devriez voir que les modifications que vous avez effectuées avant de stocker sont maintenant appliquées.
