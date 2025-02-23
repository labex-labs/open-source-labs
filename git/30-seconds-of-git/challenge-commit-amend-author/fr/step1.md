# Modifier l'auteur du dernier commit

Vous venez de faire un commit dans votre référentiel Git, mais vous vous êtes rendu compte que le nom et l'adresse e-mail de l'auteur sont incorrectes. Vous voulez mettre à jour les informations de l'auteur sans modifier le contenu du commit. Comment pouvez-vous le faire avec Git?

## Tâches

Pour modifier l'auteur du dernier commit, vous pouvez utiliser une commande. Cette commande vous permet de modifier le dernier commit de votre référentiel Git.

1. Accédez au référentiel et configurez les informations d'identité de Git à l'aide de votre compte GitHub.
2. Changez l'auteur du dernier commit en `Duck Quackers`, dont l'adresse e-mail est `cool.duck@qua.ck` et enregistrez le contenu.
3. Vérifiez que les informations de l'auteur ont été mises à jour.

Vous devriez voir que l'auteur du dernier commit est désormais `Duck Quackers` :

```shell
commit d5a385cc354f3528472a215b66cbb7c628ba47d5
Author: Duck Quackers <cool.duck@qua.ck>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt
```
