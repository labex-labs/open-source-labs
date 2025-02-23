# Écrire dans des fichiers

Vous devez écrire un programme Go qui écrit une chaîne de caractères et des octets dans un fichier et utilise des écrivains tamponnés.

## Exigences

- Le programme doit écrire une chaîne de caractères et des octets dans un fichier.
- Le programme doit utiliser des écrivains tamponnés.

## Exemple

```sh
# Essayez d'exécuter le code d'écriture dans un fichier.
$ go run writing-files.go
a écrit 5 octets
a écrit 7 octets
a écrit 9 octets

# Vérifiez ensuite le contenu des fichiers écrits.
$ cat /tmp/dat1
bonjour
go
$ cat /tmp/dat2
certaines
écritures
tamponnées

# Ensuite, nous allons voir comment appliquer certaines des idées d'entrée/sortie de fichiers
# que nous venons de voir aux flux `stdin` et `stdout`.
```
