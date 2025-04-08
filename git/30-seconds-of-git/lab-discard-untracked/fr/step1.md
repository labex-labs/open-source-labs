# Discard Untracked Changes

Vous travaillez sur un projet utilisant Git et avez apporté quelques modifications à votre répertoire de travail. Cependant, vous réalisez que vous n'avez pas besoin de ces modifications et que vous voulez les abandonner. Vous voulez abandonner toutes les modifications non suivies sur la branche actuelle.

Pour terminer ce laboratoire, vous utiliserez le référentiel Git nommé `https://github.com/labex-labs/git-playground`. Suivez ces étapes :

1. Accédez au répertoire du référentiel :

```shell
cd git-playground
```

2. Vérifiez l'état de votre répertoire de travail :

```shell
git status
```

Vous devriez voir la sortie suivante :

```shell

```

3. Abandonnez toutes les modifications non suivies sur la branche actuelle :

```shell
git clean -f -d
```

4. Vérifiez à nouveau l'état de votre répertoire de travail :

```shell
git status
```

Vous devriez voir la sortie suivante :

```shell
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

La commande `git clean -f -d` a abandonné toutes les modifications non suivies sur la branche actuelle.
