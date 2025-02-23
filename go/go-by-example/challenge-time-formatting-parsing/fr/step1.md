# Mise en forme et analyse du temps

Le problème consiste à formater et à analyser le temps en Golang à l'aide des formats fournis.

## Exigences

- Utiliser le package `time` pour formater et analyser le temps.
- Utiliser le format `time.RFC3339` pour formater et analyser le temps.
- Utiliser l'heure de référence `Mon Jan 2 15:04:05 MST 2006` pour montrer le modèle avec lequel formater/analyser une heure/une chaîne donnée.
- Utiliser la fonction `Parse` pour analyser le temps.
- Utiliser la fonction `Format` pour formater le temps.
- Utiliser la fonction `fmt.Println` pour afficher l'heure formatée.
- Utiliser la fonction `fmt.Printf` pour afficher l'heure formatée avec les composants extraits.

## Exemple

```sh
$ go run time-formatting-parsing.go
2014-04-15T18:00:15-07:00
2012-11-01 22:08:41 +0000 +0000
6:00PM
Tue Apr 15 18:00:15 2014
2014-04-15T18:00:15.161182-07:00
0000-01-01 20:41:00 +0000 UTC
2014-04-15T18:00:15-00:00
parsing time "8:41PM" as "Mon Jan _2 15:04:05 2006":...
```
