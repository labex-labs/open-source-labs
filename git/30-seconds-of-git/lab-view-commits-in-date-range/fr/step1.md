# Afficher les commits (validations) dans une plage de dates spécifique

Votre tâche consiste à afficher tous les commits (validations) dans une plage de dates spécifique en utilisant Git. Vous devrez utiliser la commande `git log` avec les options `--since` et `--until` pour spécifier la plage de dates. Vous pouvez utiliser soit une date spécifique, soit une date relative (par exemple "il y a 12 semaines").

Pour relever ce défi, vous devrez utiliser le dépôt (repository) `https://github.com/labex-labs/git-playground`. Suivez ces étapes :

1. Clonez le dépôt sur votre machine locale en utilisant la commande `git clone https://github.com/labex-labs/git-playground`.
2. Accédez au répertoire du dépôt en utilisant la commande `cd git-playground`.
3. Utilisez la commande `git log --since='Apr 25 2023' --until='Apr 27 2023'` pour afficher tous les commits entre le 25 avril 2023 et le 27 avril 2023.
4. Utilisez la commande `git log --since='12 weeks ago'` pour afficher tous les commits effectués au cours des douze dernières semaines.

Voici le résultat final :

```
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
