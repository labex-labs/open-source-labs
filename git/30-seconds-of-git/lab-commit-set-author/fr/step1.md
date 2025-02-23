# Créer un commit avec un autre auteur

Supposons que vous travailliez sur un projet avec une équipe de développeurs et qu'un de vos collègues ait apporté quelques modifications au code. Cependant, il n'est pas disponible pour commettre les modifications lui-même et vous devez le faire à sa place. Dans ce scénario, vous pouvez utiliser l'option `--author` pour changer le nom et l'adresse e-mail de l'auteur du commit. Cette option est pratique lorsque vous devez attribuer un commit à une autre personne, par exemple lorsque vous commettez du code au nom d'un collègue en vacances ou en congé maladie.

Pour créer un commit avec un autre auteur, vous pouvez utiliser la commande suivante :

```shell
git commit -m < message > --author="<name> <email>"
```

Disons que vous travaillez sur un projet hébergé sur le référentiel `https://github.com/labex-labs/git-playground`. Vous avez apporté quelques modifications au code et vous devez créer un commit au nom de votre collègue John Doe, qui n'est pas disponible pour commettre les modifications lui-même. Pour ce faire, vous pouvez utiliser la commande suivante :

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.email "votre adresse e-mail"
git config --global user.name "votre nom d'utilisateur"
echo "Fix the network bug" > README.md
git add.
git commit -m "Fix the bug" --author="John Doe <john.doe@example.com>"
```

Cette commande créera un nouveau commit avec le message "Fix the bug" et l'attribuera à John Doe.

Voici le résultat final :

![Git commit author change result](../assets/challenge-commit-set-author-step1-1.png)
