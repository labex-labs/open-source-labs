# Appliquer le dernier dépôt temporaire

Vous travaillez sur un projet dans votre référentiel Git et avez effectué certaines modifications qui ne sont pas encore prêtes à être validées. Cependant, vous devez passer à une autre branche ou à un autre commit pour travailler sur une fonctionnalité différente. Vous ne voulez pas perdre vos modifications, donc vous décidez de les stocker temporairement. Plus tard, lorsque vous êtes prêt à reprendre le travail sur vos modifications, vous devez appliquer le dernier dépôt temporaire à votre répertoire de travail.

Pour appliquer le dernier dépôt temporaire à votre référentiel Git, suivez ces étapes :

1. Clonez le référentiel Git nommé `https://github.com/labex-labs/git-playground` sur votre machine locale.
2. Accédez au répertoire `git-playground`.
3. Apportez quelques modifications au fichier `README.md`, par exemple, écrivez "Ceci est une nouvelle ligne" dans le fichier `README.md`.
4. Exécutez la commande `git stash` pour stocker temporairement vos modifications.
5. Exécutez la commande `git stash list` pour voir la liste de vos dépôts temporaires. Vous devriez voir un dépôt temporaire dans la liste.
6. Exécutez la commande `git stash apply` pour appliquer le dernier dépôt temporaire à votre répertoire de travail.
7. Vérifiez le fichier `README.md` pour voir que vos modifications ont été appliquées.

```shell
git clone https://github.com/labex-labs/git-playground.git
cd git-playground
echo "This is a new line" >> README.md
git stash
git stash list
git stash apply
cat README.md
```

Voici le résultat de l'exécution de `cat README.md` :

```shell
# git-playground
Git Playground
This is a new line
```
