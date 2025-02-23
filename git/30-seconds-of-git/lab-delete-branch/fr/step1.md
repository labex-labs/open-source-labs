# Supprimer une branche

Vous avez créé une branche locale dans votre référentiel Git, et vous n'en avez plus besoin. Vous voulez supprimer la branche pour maintenir votre référentiel propre et organisé.

1. Accédez au référentiel cloné :

```shell
cd git-playground
```

2. Affichez les branches actuelles :

```shell
git branch
```

3. Supprimez la branche `feature-1` :

```shell
git branch -d feature-1
```

4. Vérifiez que la branche a été supprimée :

```shell
git branch
```

Voici le résultat de l'exécution de la commande `git branch` :

```
* master
```
