# Mettre à jour une branche distante après avoir réécrit l'historique

Lorsque vous réécrivez l'historique localement, vous créez un nouveau commit avec un hachage SHA-1 différent. Cela signifie que l'historique des commits sur votre branche locale est différent de l'historique des commits sur la branche distante. Si vous essayez de pousser vos modifications vers la branche distante, Git refusera le push car il considérera que l'historique des commits s'est divergé. Pour résoudre ce problème, vous devez forcer la mise à jour de la branche distante.

## Tâches

Pour terminer ce défi, vous utiliserez le référentiel Git `git-playground` de votre compte GitHub, qui provient d'un fork de `https://github.com/labex-labs/git-playground.git`.

1. Clonez le référentiel `git-playground` sur votre machine locale.
2. Mettez à jour un commit avec le message "Added file2.txt" en un commit avec le message "Update file2.txt".
3. Poussez les modifications de la branche locale vers le référentiel distant.
4. Si vous ne pouvez pas pousser avec succès, forcez le push.

Voici le résultat final :

```shell

```
