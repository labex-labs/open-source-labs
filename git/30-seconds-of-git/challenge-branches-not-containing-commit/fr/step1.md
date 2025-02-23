# Trouver les branches ne contenant pas un commit

Vous travaillez sur un projet avec plusieurs branches, et vous devez trouver toutes les branches qui ne contiennent pas un commit spécifique. Cela peut être utile si vous voulez vous assurer qu'un certain changement a été appliqué à toutes les branches, ou si vous voulez savoir quelles branches sont obsolètes et nécessitent d'être mises à jour.

## Tâches

Pour ce défi, nous utiliserons le référentiel Git nommé `https://github.com/your-username/git-playground`.

1. Clonez ce référentiel sur votre machine locale.
2. Une fois que vous avez cloné le référentiel, accédez au répertoire.
3. Créez et basculez sur une branche `new-branch` et apportez quelques modifications de code sur cette branche puis committez-les, le message de commit est "Créer une branche new-branch".
4. Vérifiez le hash du message de commit "Créer une branche new-branch".
5. Trouvez toutes les branches qui ne contiennent pas un hash avec le message de commit "Créer une branche new-branch".

Cela affichera une liste de toutes les branches qui ne contiennent pas le commit spécifié. Dans ce cas, la sortie sera :

```shell
master
```

Cela signifie que la branche `master` ne contient pas le commit avec le hash `31c5ac20129151af1`.
