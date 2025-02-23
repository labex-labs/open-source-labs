# Configurez les sauts de ligne

Vous travaillez sur un projet avec une équipe de développeurs et vous remarquez que certains membres de l'équipe utilisent différents sauts de ligne que d'autres. Cela peut entraîner des problèmes lors de la fusion du code et peut entraîner des conflits. Vous devez configurer les sauts de ligne pour le référentiel pour garantir la cohérence et éviter les conflits.

## Tâches

Pour configurer les sauts de ligne pour le référentiel `git-playground`, suivez ces étapes :

1. Accédez au répertoire où se trouve le référentiel `git-playground` (`~/project/git-playground`).
2. Configurez les sauts de ligne pour utiliser les sauts de ligne UNIX (`\n`).
3. Vérifiez que les sauts de ligne ont été correctement configurés.

## Exemple

Pour vérifier que les sauts de ligne ont été correctement configurés, vous pouvez utiliser la commande suivante :

```bash
git config --get core.eol
```

Si les sauts de ligne ont été correctement configurés, la commande retournera `lf`.

![Configuration des sauts de ligne Git](../assets/20240702-15-01-34-S4a8vHzh@2x.png)
