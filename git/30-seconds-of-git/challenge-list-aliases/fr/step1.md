# Lister tous les alias Git

En tant que développeur, vous pouvez vouloir lister tous les alias Git qui ont été configurés sur votre système. Cela peut être utile pour plusieurs raisons, telles que :

- Vérifier quels alias sont disponibles
- Découvrir les commandes auxquelles un alias est associé
- Supprimer ou modifier les alias existants

## Tâches

Disons que vous avez un référentiel Git nommé `git-playground` situé à `https://github.com/labex-labs/git-playground`.

Vous avez configuré les alias suivants :

```shell
alias.st=status
alias.co=checkout
alias.rb=rebase
```

1. Accédez à ce référentiel sur votre machine locale.
2. Utilisez la commande `sed` lors de la liste de tous les alias Git.

En exécutant la commande, la sortie sera :

```shell
st=status
co=checkout
rb=rebase
```
