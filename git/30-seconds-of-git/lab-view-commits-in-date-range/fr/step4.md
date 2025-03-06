# Utilisation de dates relatives et d'options de formatage

Git prend également en charge les dates relatives, ce qui peut être très pratique pour afficher rapidement l'activité récente.

Affichons tous les commits des 12 dernières semaines :

```bash
git log --since='12 weeks ago'
```

Selon le moment où vous exécutez cette commande, vous pourriez voir tous les commits ou seulement certains d'entre eux s'ils tombent dans cette période.

D'autres formats de dates relatives utiles incluent :

- `"Il y a X jours"`
- `"Il y a X mois"`
- `"Hier"`
- `"La semaine dernière"`

Essayons d'afficher les commits de l'année dernière :

```bash
git log --since='1 year ago'
```

Cette commande affichera tous les commits effectués au cours de l'année écoulée.

## Options de formatage supplémentaires

La commande `git log` propose diverses options de formatage pour personnaliser la sortie. En voici quelques-unes utiles :

1. Pour afficher un journal plus concis avec chaque commit sur une seule ligne :

```bash
git log --oneline --since='Apr 25 2023' --until='Apr 27 2023'
```

La sortie ressemblera à ceci :

```
d22f46b (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```

2. Pour voir les fichiers qui ont été modifiés dans chaque commit :

```bash
git log --name-status --since='Apr 25 2023' --until='Apr 27 2023'
```

Cette commande montre l'état des fichiers qui ont été modifiés dans chaque commit, ce qui peut être utile pour comprendre ce qui a été changé.

Ces options de formatage peuvent être combinées avec des filtres de dates pour créer des requêtes puissantes qui vous aident à mieux comprendre l'historique d'un projet.
