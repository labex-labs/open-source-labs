# Consulter un graphe visuel du référentiel

En tant que développeur, vous devrez peut-être consulter l'historique d'un référentiel pour comprendre comment le code a évolué au fil du temps. Cependant, simplement consulter une liste de commits peut être abondante et difficile à comprendre. C'est là que le graphe Git entre en jeu. En visualisant l'historique d'un référentiel, vous pouvez rapidement voir comment le code a évolué et identifier tout problème ou bogue qui peut avoir été introduit.

Pour consulter un graphe visuel d'un référentiel Git, vous pouvez utiliser la commande `git log` avec l'option `--graph`. Par exemple, supposons que vous vouliez consulter l'historique du référentiel `git-playground` sur GitHub.

Une fois que vous avez cloné le référentiel, vous pouvez accéder au répertoire et utiliser la commande `git log` pour afficher le graphe :

```shell
cd git-playground
git log --pretty=oneline --graph --decorate --all
```

Cela affichera un graphe visuel de tous les commits et les branches du référentiel, vous permettant de voir comment le code a évolué au fil du temps.

Voici le résultat final :

```
* d22f46ba8c2d4e07d773c5126e9c803933eb5898 (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD) Added file2.txt
* cf80005e40a3c661eb212fcea5fad06f8283f08f Added file1.txt
* b00b9374a7c549d1af111aa777fdcc868d8a2a01 Initial commit
```
