# Chemins de fichiers

Dans ce défi, vous devez utiliser le package `filepath` pour effectuer diverses opérations sur les chemins de fichiers, telles que la construction de chemins de manière portable, le découpage d'un chemin en composants de répertoire et de fichier, la vérification si un chemin est absolu, la recherche de l'extension d'un fichier et la recherche d'un chemin relatif entre deux chemins.

## Exigences

- Utiliser `Join` pour construire des chemins de manière portable.
- Utiliser `Dir` et `Base` pour découper un chemin en composants de répertoire et de fichier.
- Utiliser `IsAbs` pour vérifier si un chemin est absolu.
- Utiliser `Ext` pour trouver l'extension d'un fichier.
- Utiliser `TrimSuffix` pour supprimer l'extension d'un nom de fichier.
- Utiliser `Rel` pour trouver un chemin relatif entre deux chemins.

## Exemple

```sh
$ go run file-paths.go
p: dir1/dir2/filename
dir1/filename
dir1/filename
Dir(p): dir1/dir2
Base(p): filename
false
true
.json
config
t/file
../c/t/file

```
