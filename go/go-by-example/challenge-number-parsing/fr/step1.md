# Analyse de nombres

L'analyse de nombres à partir de chaînes de caractères est une tâche courante dans de nombreux programmes. Ce défi vous demande d'utiliser le package intégré `strconv` pour analyser différents types de nombres à partir de chaînes de caractères.

## Exigences

- Utiliser le package `strconv` pour analyser des nombres à partir de chaînes de caractères.
- Analyser un nombre à virgule flottante avec `ParseFloat`.
- Analyser un entier avec `ParseInt`.
- Analyser un nombre au format hexadécimal avec `ParseInt`.
- Analyser un entier non signé avec `ParseUint`.
- Analyser un entier en base 10 avec `Atoi`.
- Gérer les erreurs renvoyées par les fonctions d'analyse.

## Exemple

```sh
$ go run number-parsing.go
1,234
123
456
789
135
strconv.ParseInt: analyser "wat": syntaxe invalide

# Ensuite, nous examinerons une autre tâche courante d'analyse : les URL.
```
