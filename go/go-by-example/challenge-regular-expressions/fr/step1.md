# Expressions régulières

Le défi consiste à compléter le code pour effectuer diverses tâches liées aux expressions régulières en Golang.

## Exigences

- Utiliser le package `regexp` pour effectuer des tâches liées aux expressions régulières.
- Utiliser `MatchString` pour tester si un motif correspond à une chaîne de caractères.
- Utiliser `Compile` pour optimiser une structure `Regexp`.
- Utiliser `MatchString` pour tester une correspondance comme `Compile`.
- Utiliser `FindString` pour trouver la correspondance de l'expression régulière.
- Utiliser `FindStringIndex` pour trouver la première correspondance et retourner les index de début et de fin de la correspondance au lieu du texte correspondant.
- Utiliser `FindStringSubmatch` pour retourner des informations pour à la fois `p([a-z]+)ch` et `([a-z]+)`.
- Utiliser `FindStringSubmatchIndex` pour retourner des informations sur les index des correspondances et des sous-correspondances.
- Utiliser `FindAllString` pour trouver toutes les correspondances d'une expression régulière.
- Utiliser `FindAllStringSubmatchIndex` pour s'appliquer à toutes les correspondances de l'entrée, pas seulement à la première.
- Utiliser `Match` pour tester une correspondance avec des arguments de type `[]byte` et supprimer `String` du nom de la fonction.
- Utiliser `MustCompile` pour créer des variables globales avec des expressions régulières.
- Utiliser `ReplaceAllString` pour remplacer des sous-chaînes de caractères par d'autres valeurs.
- Utiliser `ReplaceAllFunc` pour transformer le texte correspondant avec une fonction donnée.

## Exemple

```sh
# Pour une référence complète sur les expressions régulières en Go, consultez
# la documentation du package [`regexp`](https://pkg.go.dev/regexp).
```
