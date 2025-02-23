# Désactiver le regroupement rapide

Par défaut, Git utilise le regroupement rapide pour fusionner les branches qui n'ont pas de commits divergents. Cela signifie que si vous avez une branche sans nouveaux commits, Git déplacera simplement le pointeur de la branche dans laquelle vous effectuez la fusion vers le dernier commit de la branche à partir de laquelle vous effectuez la fusion. Bien que cela puisse être utile dans certains cas, cela peut également poser des problèmes, en particulier lorsqu'on travaille sur de grands projets avec de nombreux contributeurs. Par exemple, si deux développeurs travaillent sur la même branche et apportent tous les deux des modifications, le regroupement rapide peut entraîner des conflits difficiles à résoudre.

Pour désactiver le regroupement rapide, utilisons le référentiel à partir de `https://github.com/labex-labs/git-playground`.

1. Clonez le référentiel, accédez au répertoire et configurez l'identité :

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "votre-nom-d'utilisateur"
git config --global user.email "votre-email"
```

2. Créez et basculez sur une branche appelée `my-branch`, créez un fichier `hello.txt` et ajoutez "hello,world" à celui-ci, ajoutez-le à la zone de préparation et validez-le avec le message "Ajouté hello.txt" :

```shell
git checkout -b my-branch
echo "hello,world" > hello.txt
git add.
git commit -m "Ajouté hello.txt"
```

3. Exécutez la commande suivante pour désactiver le regroupement rapide :

```shell
git config --add merge.ff false
```

Cela désactivera le regroupement rapide pour toutes les branches, même si cela est possible. Vous pouvez utiliser le drapeau `--global` pour configurer cette option globalement :

```shell
git config --global --add merge.ff false
```

4. Revenez sur la branche `master` et fusionnez la branche `my-branch`, enregistrez et quittez sans modifier le texte :

```shell
git checkout master
git merge my-branch
```

Maintenant, Git créera toujours un commit de fusion, même si il est possible de regrouper rapidement :

```shell
commit 6e17a776ab51a89ace069614b0caf1c07915a92c (HEAD -> master)
Merge: ec5ea6d 6d7de91
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Mon Jul 17 13:30:44 2023 +0800

    Fusionner la branche'my-branch'
```
