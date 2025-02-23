# Pousser les modifications locales vers le distant

En tant que développeur, vous devrez peut-être pousser vos modifications locales vers un référentiel distant pour partager votre travail avec d'autres membres de l'équipe ou pour déployer votre code dans un environnement de production. La commande `git push` est utilisée pour pousser les dernières modifications de la branche locale vers le distant. Cependant, avant de pousser les modifications, vous devez vous assurer que votre branche locale est à jour avec la branche distante. S'il y a des conflits entre les branches locales et distantes, vous devrez les résoudre avant de pousser les modifications.

Pour terminer ce laboratoire, vous utiliserez le référentiel Git `git-playground` de votre compte GitHub, qui provient d'un fork de `https://github.com/labex-labs/git-playground.git`. Vous avez apporté quelques modifications à la branche `master` et souhaitez les pousser vers le référentiel distant. Voici les étapes à suivre :

1. Clonez le référentiel sur votre machine locale et accédez au répertoire en exécutant les commandes suivantes :

```shell
git clone https://github.com/your-username/git-playground
cd git-playground
```

2. Assurez-vous que votre branche locale est à jour avec la branche distante en exécutant la commande suivante :

```shell
git pull origin master
```

3. Une fois que vous avez extrait les dernières modifications de la branche distante, vous pouvez apporter vos modifications à la branche locale :

```shell
echo "hello,world" >> file1.txt
```

4. Après avoir apporté les modifications, préparez-les en utilisant la commande `git add` :

```shell
git add.
```

5. Validez les modifications en utilisant la commande `git commit` :

```shell
git commit -m "Added new feature"
```

6. Enfin, poussez les modifications vers le référentiel distant en utilisant la commande `git push` :

```shell
git push origin master
```

Voici le résultat de l'exécution de `git log` :

```shell
commit 1f1949955387a1549f1bb5286d3d0a2b993f87e0 (HEAD -> master,origin/master,origin/HEAD)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Added new feature
```
