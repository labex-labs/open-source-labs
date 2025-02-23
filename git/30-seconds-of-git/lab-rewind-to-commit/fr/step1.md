# Remonter à un commit spécifique

En tant que développeur, vous pouvez avoir besoin d'annuler des modifications apportées à votre base de code. Par exemple, vous avez peut-être fait une erreur et avez besoin de revenir à une version antérieure de votre code. Dans ce défi, vous utiliserez Git pour remonter à un commit spécifique dans un référentiel.

Pour terminer ce laboratoire, vous utiliserez le référentiel Git `git-playground` de `https://github.com/labex-labs/git-playground.git`. Suivez ces étapes pour terminer le défi :

1. Clonez le référentiel sur votre machine locale :

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Accédez au référentiel :

```shell
cd git-playground
```

3. Affichez l'historique des commits du référentiel :

```shell
git log --oneline
```

4. Vérifiez que le message de commit auquel vous voulez remonter est le hash du commit "Initial commit".
5. Utilisez la commande `git reset <commit>` pour remonter au commit spécifié. Par exemple, vous voulez remonter au commit avec le hash `3050fc0d3` :

```shell
git reset 3050fc0d3
```

6. Affichez à nouveau l'historique des commits du référentiel :

```shell
git log --oneline
```

7. Si vous voulez supprimer les modifications et revenir à l'ancienne version de votre code, utilisez la commande `git reset --hard <commit>`. Par exemple, vous voulez supprimer les modifications et revenir au commit avec le hash `c0d30f305` :

```shell
git reset --hard c0d30f305
```

Voici le résultat de l'exécution de `git log --oneline` :

```shell
c0d30f305 (HEAD -> master) Initial commit
```
