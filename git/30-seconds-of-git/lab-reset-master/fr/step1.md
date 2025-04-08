# Réinitialiser la branche locale master pour qu'elle corresponde à la branche distante

Vous avez travaillé sur un projet et apporté des modifications à la branche locale `master`. Cependant, vous constatez que la branche distante `master` a été mise à jour avec de nouvelles modifications que vous n'avez pas dans votre branche locale. Vous devez réinitialiser la branche locale `master` pour qu'elle corresponde à celle sur le distant.

1. Basculer sur la branche `master`:
   ```shell
   git checkout master
   ```
2. Récupérer les dernières mises à jour du distant:
   ```shell
   git fetch origin
   ```
3. Afficher l'historique des commits de la branche actuelle:
   ```shell
   git log
   ```
4. Réinitialiser la branche locale `master` pour qu'elle corresponde à celle sur le distant:
   ```shell
   git reset --hard origin/master
   ```
5. Vérifier que la branche locale `master` est maintenant à jour avec la branche distante `master`:
   ```shell
   git log
   ```

Voici le résultat final:

```shell

```
