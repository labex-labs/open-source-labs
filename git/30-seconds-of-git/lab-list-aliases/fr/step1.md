# Lister tous les alias Git

En tant que développeur, vous pouvez vouloir lister tous les alias Git qui ont été configurés sur votre système. Cela peut être utile pour plusieurs raisons, telles que :

- Vérifier quels alias sont disponibles
- Découvrir les commandes auxquelles un alias est mappé
- Supprimer ou modifier les alias existants

Disons que vous avez un référentiel Git nommé `git-playground` situé à `https://github.com/labex-labs/git-playground`.

1. Accédez à ce référentiel sur votre machine locale :

```shell
cd git-playground
```

2. Configurez les alias suivants :

```shell
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.rb rebase
```

3. Utilisez la commande `sed` lors de la liste de tous les alias Git :

```shell
git config -l | grep alias | sed 's/^alias\.//g'
```

Exécuter la commande produira la sortie suivante :

```shell
st=status
co=checkout
rb=rebase
```
