# Mettre à jour une branche distante après avoir réécrit l'historique

Lorsque vous réécrivez l'historique localement, vous créez un nouveau commit avec un hash SHA-1 différent. Cela signifie que l'historique des commits sur votre branche locale est différent de l'historique des commits sur la branche distante. Si vous essayez d'envoyer vos modifications vers la branche distante, Git refusera le push car il considérera que l'historique des commits a divergé. Pour résoudre ce problème, vous devez forcer une mise à jour de la branche distante.

Pour terminer ce laboratoire, vous utiliserez le référentiel Git `git-playground` de votre compte GitHub, qui provient d'un fork de `https://github.com/labex-labs/git-playground.git`.

1. Clonez le référentiel `git-playground` sur votre machine locale :

```shell
git clone https://github.com/your-username/git-playground.git
```

2. Mettez à jour un commit avec le message "Added file2.txt" en un commit avec le message "Update file2.txt" :

```shell
git commit --amend
```

3. Poussez les modifications de la branche locale vers le référentiel distant :

```shell
git push
```

4. Si vous ne pouvez pas pousser avec succès, poussez avec force :

```shell
git push -f origin master
```

Le drapeau `-f` force Git à mettre à jour la branche distante avec vos modifications, même si l'historique des commits a divergé.

Voici le résultat final :

```shell

```
