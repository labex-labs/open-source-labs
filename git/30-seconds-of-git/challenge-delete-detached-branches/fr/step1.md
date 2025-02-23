# Supprimer les branches détachées

Vous disposez d'un référentiel Git avec plusieurs branches détachées que vous n'avez plus besoin. Ces branches encombrent votre référentiel et le rendent difficile à gérer. Vous voulez supprimer toutes les branches détachées pour nettoyer votre référentiel.

## Tâches

Pour terminer ce défi, vous utiliserez le référentiel Git `git-playground` de votre compte GitHub, qui provient d'un fork de `https://github.com/labex-labs/git-playground.git`. Ne cochez pas "Copier seulement la branche master".

1. Clonez le référentiel, accédez au répertoire et configurez l'identité.
2. Puisque la branche `feature-branch` existe dans le référentiel distant, basculez vers `feature-branch`, ce qui fera en sorte que la branche `feature-branch` locale suive la branche `feature-branch` du référentiel distant et supprime la branche `feature-branch` dans le référentiel distant.
3. Affichez la relation de suivi entre les branches locales et les branches distantes qu'elles suivent.
4. Revenez sur la branche `master`.
5. Supprimez toutes les branches détachées de votre référentiel local.
6. Vérifiez que les branches détachées ont été supprimées.

La sortie ne devrait montrer que les branches associées à une branche spécifique :

```shell
* master d22f46b [origin/master] Added file2.txt
```
