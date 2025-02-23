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
commit d22f46ba8c2d4e07d773c5126e9c803933eb5898 (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD)
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt

commit cf80005e40a3c661eb212fcea5fad06f8283f08f
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file1.txt

commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```
