# Supprimer une branche distante

Parfois, vous devrez peut-être supprimer une branche distante qui n'est plus nécessaire. Par exemple, si une branche de fonctionnalité a été fusionnée dans la branche principale, vous voudrez peut-être supprimer la branche de fonctionnalité distante pour garder le référentiel propre.

## Tâches

Supposons qu'un référentiel GitHub appelé `git-playground` ait été cloné à partir de votre compte GitHub, qui provient d'un fork de `https://github.com/labex-labs/git-playground.git`. Vous voulez supprimer la branche distante nommée `feature-branch` qui n'est plus nécessaire.

1. Ouvrez le terminal et accédez au répertoire du référentiel local.
2. Ajoutez la branche `feature-branch` au référentiel distant `origin`.
3. Liste toutes les branches distantes.
4. Supprime la branche distante `feature-branch` sur le référentiel distant `origin`.
5. Vérifiez que la branche distante a été supprimée.

La sortie ne devrait pas inclure la branche distante `feature-branch` :

```
origin/HEAD -> origin/master
origin/master
```
