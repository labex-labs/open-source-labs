# Filtres de ligne

Le problème à résoudre dans ce défi est d'écrire un programme Go qui lit le texte d'entrée à partir de stdin, met en majuscules toutes les lettres du texte puis imprime le texte modifié sur stdout.

## Exigences

- Le programme doit lire le texte d'entrée à partir de stdin.
- Le programme doit mettre en majuscules toutes les lettres du texte d'entrée.
- Le programme doit imprimer le texte modifié sur stdout.

## Exemple

```sh
# Pour tester notre filtre de ligne, commençons par créer un fichier
# avec quelques lignes en minuscules.
$ echo 'hello' > /tmp/lines
$ echo 'filter' >> /tmp/lines

# Ensuite, utilisez le filtre de ligne pour obtenir des lignes en majuscules.
$ cat /tmp/lines | go run line-filters.go
HELLO
FILTER
```
