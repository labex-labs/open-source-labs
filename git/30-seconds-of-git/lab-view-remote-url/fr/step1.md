# Afficher l'URL distante

En tant que développeur, vous devrez peut-être afficher l'URL d'un dépôt distant pour diverses raisons, telles que le dépannage de problèmes liés à votre configuration Git ou la vérification que vous travaillez avec le bon dépôt. Cependant, si vous n'êtes pas familier avec les commandes Git, il peut être difficile de savoir comment afficher l'URL distante.

Pour ce laboratoire, nous utiliserons le référentiel Git nommé `https://github.com/labex-labs/git-playground`. Pour afficher l'URL distante de ce référentiel, suivez ces étapes :

1. Ouvrez votre terminal ou invite de commandes.
2. Accédez au répertoire où vous avez cloné le référentiel `git-playground` :

```shell
cd git-playground
```

3. Exécutez la commande suivante pour afficher l'URL distante :

```shell
git config --get remote.origin.url
```

La sortie devrait afficher l'URL du référentiel distant, qui dans ce cas est `https://github.com/labex-labs/git-playground.git`.
