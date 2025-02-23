# Créer un stash Git

En tant que développeur, vous pouvez vous trouver dans une situation où vous devez basculer sur une autre branche ou travailler sur une autre fonctionnalité, mais que vous n'êtes pas prêt à valider vos modifications. Vous ne voulez pas perdre votre progression, mais vous ne voulez pas non plus valider du code incomplet ou bugué. C'est là que le stash s'avère pratique.

Un stash vous permet de sauvegarder vos modifications sans les valider, de sorte que vous pouvez basculer sur une autre branche ou travailler sur une autre fonctionnalité. Vous pouvez ensuite appliquer votre stash plus tard lorsque vous serez prêt à reprendre le travail sur vos modifications.

Pour créer un stash, vous pouvez utiliser la commande `git stash save`. Disons que vous travaillez sur une branche nommée `feature` dans le référentiel `git-playground` et que vous voulez sauvegarder vos modifications avant de basculer sur une autre branche :

1. Premièrement, accédez au répertoire `git-playground` :

```shell
cd git-playground
```

2. Basculez sur une branche nommée `feature` :

```shell
git checkout -b feature
```

3. Apportez quelques modifications aux fichiers dans le répertoire :

```shell
echo "Some changes" >> README.md
```

4. Sauvegardez vos modifications dans un stash :

```shell
git stash save "My changes"
```

5. Basculez sur une autre branche :

```shell
git checkout master
```

6. Lorsque vous avez fini de faire des modifications sur l'autre branche, revenez sur la branche `feature` et appliquez votre stash :

```shell
git stash apply
```

Voici le résultat final :

```shell
stash@{0}: On feature: My changes
```
