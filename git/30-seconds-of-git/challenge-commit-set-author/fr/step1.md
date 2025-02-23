# Créer un commit avec un autre auteur

Supposons que vous travailliez sur un projet avec une équipe de développeurs et qu'un de vos collègues ait apporté quelques modifications au code. Cependant, il n'est pas disponible pour commettre les modifications lui-même et vous devez les commettre à sa place. Dans ce scénario, vous pouvez utiliser l'option `--author` pour changer le nom et l'adresse e-mail de l'auteur du commit. Cette option est pratique lorsque vous devez attribuer un commit à une autre personne, par exemple lorsque vous commettez du code au nom d'un collègue en vacances ou en congé maladie.

## Tâches

Disons que vous travailliez sur un projet hébergé sur le référentiel `https://github.com/labex-labs/git-playground`. Vous avez apporté quelques modifications au code, par exemple, vous avez ajouté "Corrigez le bogue" au fichier `README.md` de votre compte GitHub, et vous devez effectuer un commit au nom de votre collègue John Doe, qui ne peut pas commettre ces modifications lui-même.

Cette commande créera un nouveau commit avec le message "Corrigez le bogue" et l'attribuera à John Doe :

![Git commit author command](../assets/challenge-commit-set-author-step1-1.png)
