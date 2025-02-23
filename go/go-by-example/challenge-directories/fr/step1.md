# Dossiers

Créez un programme Go qui crée un nouveau sous-dossier dans le répertoire de travail actuel, crée une hiérarchie de dossiers, y compris les parents, liste le contenu d'un dossier, change le répertoire de travail actuel et visite un dossier de manière récursive.

## Exigences

- Créez un nouveau sous-dossier dans le répertoire de travail actuel.
- Lors de la création de dossiers temporaires, il est recommandé de `déférer` leur suppression. `os.RemoveAll` supprimera tout l'arbre de dossiers (de manière similaire à `rm -rf`).
- Créez une hiérarchie de dossiers, y compris les parents avec `MkdirAll`. Cela est similaire à la commande de ligne `mkdir -p`.
- `ReadDir` liste le contenu d'un dossier, en retournant une slice d'objets `os.DirEntry`.
- `Chdir` nous permet de changer le répertoire de travail actuel, de manière similaire à `cd`.
- Visitez un dossier de manière récursive, y compris tous ses sous-dossiers. `Walk` accepte une fonction de rappel pour traiter chaque fichier ou dossier visité.

## Exemple

```sh
$ go run directories.go
Listing subdir/parent
child true
file2 false
file3 false
Listing subdir/parent/child
file4 false
Visiting subdir
subdir true
subdir/file1 false
subdir/parent true
subdir/parent/child true
subdir/parent/child/file4 false
subdir/parent/file2 false
subdir/parent/file3 false
```
