# Créer un cache Git

En tant que développeur, vous pouvez vous trouver dans une situation où vous devez basculer sur une autre branche ou travailler sur une autre fonctionnalité, mais que vous n'êtes pas prêt à valider vos modifications. Vous ne voulez pas perdre votre progression, mais vous ne voulez pas non plus valider du code incomplet ou bugué. C'est là que le cache s'avère pratique.

Un cache vous permet de sauvegarder vos modifications sans les valider, de sorte que vous pouvez basculer sur une autre branche ou travailler sur une autre fonctionnalité. Vous pouvez ensuite appliquer votre cache plus tard lorsque vous serez prêt à continuer à travailler sur vos modifications.

## Tâches

Disons que vous travaillez sur une branche nommée `feature` dans le référentiel `git-playground` et que vous voulez sauvegarder vos modifications avant de basculer sur une autre branche :

1. D'abord, accédez au répertoire `git-playground`.
2. Basculez sur une branche nommée `feature`.
3. Ajoutez la ligne "Quelques modifications" au fichier `README.md`.
4. Sauvegardez vos modifications dans un cache et ajoutez un message descriptif "Mes modifications" à ce cache.
5. Basculez sur une autre branche.
6. Lorsque vous avez fini de faire des modifications sur l'autre branche, basculez de nouveau sur la branche `feature` et appliquez votre cache.

Voici le résultat final :

```shell
stash@{0}: On feature: My changes
```
