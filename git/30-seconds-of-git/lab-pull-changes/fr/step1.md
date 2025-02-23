# Télécharger les dernières modifications à partir d'un référentiel distant

Vous travaillez sur un projet avec une équipe de développeurs et vous devez vous assurer que votre copie locale de la base de code est à jour avec les dernières modifications apportées par vos collègues. Pour ce faire, vous devez télécharger les dernières modifications à partir du référentiel distant.

Pour ce laboratoire, nous utiliserons le référentiel Git nommé `https://github.com/labex-labs/git-playground`. Suivez les étapes ci-dessous pour terminer le laboratoire :

1. Accédez au répertoire du référentiel cloné :

```shell
cd git-playground
```

2. Téléchargez les dernières modifications à partir de la branche `master` du référentiel distant :

```shell
git pull origin master
```

Après avoir exécuté la commande `git pull`, vous devriez voir un message indiquant que votre copie locale du référentiel est à jour avec le référentiel distant.

Voici le résultat après le téléchargement :

![git pull command output](../assets/challenge-pull-changes-step1-1.png)
