# Définir le nom de la branche de poussée par défaut

Lorsque vous poussez des modifications vers un référentiel distant, Git utilisera le nom de la branche locale actuelle comme nom par défaut pour la branche distante. Cependant, parfois vous souhaiterez peut-être pousser vos modifications vers une autre branche. Dans ce cas, vous devrez spécifier explicitement le nom de la branche distante chaque fois que vous poussez vos modifications. Cela peut être fastidieux et propice à des erreurs, en particulier si vous travaillez avec plusieurs branches.

## Tâches

Pour terminer ce défi, vous utiliserez le référentiel Git `git-playground` de votre compte GitHub, qui provient d'un fork de `https://github.com/labex-labs/git-playground.git`. Suivez les étapes ci-dessous pour définir le nom de la branche de poussée par défaut :

1. Clonez le référentiel à partir de `https://github.com/your-username/git-playground.git`.
2. Changez dans le répertoire du référentiel.
3. Définissez le nom de la branche de poussée par défaut sur le nom de la branche locale actuelle.
4. Créez une nouvelle branche nommée `my-branch` et basculez sur elle.
5. Créez un nouveau fichier appelé `hello.txt` et écrivez la chaîne de caractères "Hello, World" dedans. Ajoutez le nouveau fichier `hello.txt` à la zone de préparation Git et committez-le, en utilisant le message de commit "Add hello.txt" pour décrire les modifications effectuées dans ce commit.
6. Poussez vos modifications vers le référentiel distant. Git poussera vos modifications vers une branche nommée `my-branch` sur le référentiel distant.

Voici le résultat de l'exécution de `git log` :

```shell
commit 1f1949959887a1549f1bb5286d3d0a2b993f87e0 (HEAD -> my-branch, origin/my-branch)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Add hello.txt
```
