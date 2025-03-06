# Affichage des commits dans une plage de dates spécifique

Maintenant, nous allons apprendre à filtrer les commits en fonction de dates spécifiques. Git propose deux options utiles à cet effet :

- `--since` ou `--after` : Affiche les commits plus récents qu'une date spécifique
- `--until` ou `--before` : Affiche les commits plus anciens qu'une date spécifique

Lorsque nous combinons ces options, nous pouvons afficher les commits dans une plage de dates spécifique.

Affichons tous les commits qui ont eu lieu entre le 25 avril 2023 et le 27 avril 2023 :

```bash
git log --since='Apr 25 2023' --until='Apr 27 2023'
```

Cette commande affichera tous les commits qui ont été effectués entre le 25 et le 27 avril 2023. La sortie devrait ressembler à ceci :

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

Git accepte de nombreux formats de date, notamment :

- `"YYYY-MM-DD"` (par exemple, `2023-04-25`)
- `"Mois JJ YYYY"` (par exemple, `Apr 25 2023`)
- `"JJ Mois YYYY"` (par exemple, `25 Apr 2023`)

Essayons un autre format de date pour voir s'il y a des commits dans une autre plage :

```bash
git log --since='2023-04-20' --until='2023-04-24'
```

Cette commande peut ne renvoyer aucun résultat s'il n'y a eu aucun commit pendant cette période, ce qui est tout à fait normal.
