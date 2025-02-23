# Appliquer un dépôt (stash)

Vous travaillez sur une branche de fonctionnalité dans le référentiel `git-playground` et vous devez basculer sur une autre branche pour corriger un bogue. Cependant, vous avez des modifications qui ne sont pas encore prêtes à être validées. Vous voulez sauvegarder ces modifications et basculer sur l'autre branche. Une fois que vous avez terminé la correction du bogue, vous voulez appliquer le dépôt (stash) et continuer à travailler sur votre branche de fonctionnalité.

Les modifications ont été stockées sur la branche `feature-branch`, et le message du dépôt (stash) est "mes modifications".

1. Changez au répertoire `git-playground` :

```shell
cd git-playground
```

2. Basculez sur la branche `master` et stockez-le après avoir corrigé le bogue, le message du dépôt (stash) est "corriger le bogue". Corrigez le bogue en mettant à jour le contenu du fichier `file1.txt` avec "hello,world" :

```shell
git checkout master
echo "hello,world" > file1.txt
git stash save "corriger le bogue"
```

3. Basculez sur la branche `feature-branch`, regardez la liste des dépôts (stashes) et appliquez le dépôt (stash) dont l'information est "mes modifications" :

```shell
git checkout feature-branch
git stash apply stash@{1}
```

Voici le contenu du fichier `README.md` :

```
# git-playground
Git Playground
some changes
```

Vous devriez voir que les modifications que vous avez effectuées avant de stocker sont maintenant appliquées.
