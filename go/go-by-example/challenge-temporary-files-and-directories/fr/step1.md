# Fichiers et répertoires temporaires

Dans ce défi, vous devez créer des fichiers et des répertoires temporaires en Go.

## Exigences

- Utilisez `os.CreateTemp` pour créer un fichier temporaire.
- Utilisez `os.MkdirTemp` pour créer un répertoire temporaire.
- Utilisez `os.RemoveAll` pour supprimer le répertoire temporaire.
- Utilisez `os.WriteFile` pour écrire des données dans un fichier.

## Exemple

```sh
$ go run temporary-files-and-directories.go
Nom du fichier temporaire : /tmp/sample610887201
Nom du répertoire temporaire : /tmp/sampledir898854668
```
