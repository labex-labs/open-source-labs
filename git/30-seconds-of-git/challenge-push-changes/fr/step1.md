# Pousser les modifications locales vers le distant

En tant que développeur, vous devrez peut-être pousser vos modifications locales vers un référentiel distant pour partager votre travail avec d'autres membres de l'équipe ou pour déployer votre code dans un environnement de production. Cependant, avant de pousser les modifications, vous devez vous assurer que votre branche locale est à jour avec la branche distante. S'il y a des conflits entre les branches locales et distantes, vous devrez les résoudre avant de pousser les modifications.

## Tâches

Pour terminer ce défi, vous utiliserez le référentiel Git `git-playground` de votre compte GitHub, qui provient d'un fork de `https://github.com/labex-labs/git-playground.git`. Vous avez apporté quelques modifications à la branche `master` et souhaitez les pousser vers le référentiel distant.

1. Clonez le référentiel sur votre machine locale à partir de `https://github.com/your-username/git-playground`, accédez au répertoire et configurez l'identité.
2. Assurez-vous que votre branche locale est à jour avec la branche distante.
3. Après avoir extrait les dernières modifications de la branche distante, vous pouvez écrire "hello,world" dans le fichier `file1.txt` sur la branche `master`, ajoutez-la à la zone de préparation et validez-la avec le message "Ajout d'une nouvelle fonctionnalité ".
4. Enfin, poussez les modifications vers le référentiel distant.

Voici le résultat de l'exécution de `git log`:

```shell
commit 1f1949955387a1549f1bb5286d3d0a2b993f87e0 (HEAD -> master,origin/master,origin/HEAD)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Added new feature
```
