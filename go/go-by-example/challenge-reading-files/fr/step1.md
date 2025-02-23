# Lecture de fichiers

Vous devez lire des fichiers dans votre programme Go et effectuer différentes opérations sur les données du fichier.

## Exigences

- Vous devriez être familier avec les concepts de base de la programmation Go.
- Vous devriez avoir Go installé sur votre ordinateur.

## Exemple

```sh
$ echo "hello" > /tmp/dat
$ echo "go" >> /tmp/dat
$ go run reading-files.go
hello
go
5 bytes: hello
2 bytes @ 6: go
2 bytes @ 6: go
5 bytes: hello

# Ensuite, nous examinerons l'écriture de fichiers.
```
