# Remonter les commits

En tant que développeur, vous avez travaillé sur un projet et effectué plusieurs commits. Cependant, vous constatez que les derniers commits contiennent des erreurs et que vous devez revenir à une version précédente de votre code. Vous devez utiliser Git pour remonter vos commits et retrouver la version précédente de votre code.

Pour terminer ce laboratoire, vous utiliserez le référentiel Git `git-playground` de votre compte GitHub, qui provient d'un fork de `https://github.com/labex-labs/git-playground.git`. Suivez ces étapes :

1. Clonez le référentiel sur votre machine locale :

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
```

2. Créez une nouvelle branche appelée `rewind-commits` :

```shell
git checkout -b rewind-commits
```

3. Affichez l'historique des commits du référentiel et constatez que le dernier commit contient des erreurs et que vous devez revenir à la version précédente de votre code :

```shell
git log
```

4. Utilisez Git pour remonter vos commits d'un cran :

```shell
git reset HEAD~1 --hard
```

5. Vérifiez que vous avez réussi à remonter vos commits :

```shell
git log
```

6. Poussez vos modifications sur la branche `rewind-commits` :

```shell
git push --force origin rewind-commits
```

Voici le résultat final :

```shell
cf80005 (HEAD -> rewind-commits, origin/rewind-commits) Added file1.txt
b00b937 Initial commit
```
