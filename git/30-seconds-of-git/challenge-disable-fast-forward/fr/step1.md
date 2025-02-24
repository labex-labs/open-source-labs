# Désactiver la fusion en avant rapide

Par défaut, Git utilise la fusion en avant rapide pour fusionner les branches qui n'ont pas de commits divergents. Cela signifie que si vous avez une branche sans nouveaux commits, Git déplacera simplement le pointeur de la branche dans laquelle vous effectuez la fusion vers le dernier commit de la branche à partir de laquelle vous effectuez la fusion. Bien que cela puisse être utile dans certains cas, cela peut également poser des problèmes, en particulier lorsqu'on travaille sur de grands projets avec de multiples contributeurs. Par exemple, si deux développeurs travaillent sur la même branche et apportent tous les deux des modifications, la fusion en avant rapide peut entraîner des conflits difficiles à résoudre.

## Tâches

Pour désactiver la fusion en avant rapide, utilisons le référentiel de `https://github.com/labex-labs/git-playground`.

1. Accédez au répertoire et configurez l'identité.
2. Créez et basculez sur une branche appelée `my-branch`, créez un fichier `hello.txt` et ajoutez "hello,world" à celui-ci, ajoutez-le à la zone de préparation et validez-le avec le message "Added hello.txt".
3. Désactivez la fusion en avant rapide pour toutes les branches.
4. Revenez sur la branche `master` et fusionnez la branche `my-branch`, enregistrez et quittez sans modifier le texte.

Maintenant, Git créera toujours un commit de fusion, même si une fusion en avant est possible :

```shell
commit 6e17a776ab51a89ace069614b0caf1c07915a92c (HEAD -> master)
Merge: ec5ea6d 6d7de91
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Mon Jul 17 13:30:44 2023 +0800

    Merge branch'my-branch'
```
