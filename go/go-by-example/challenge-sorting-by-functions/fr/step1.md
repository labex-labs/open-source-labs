# Tri par fonctions

Le problème à résoudre dans ce défi est d'implémenter une fonction de tri personnalisée en Go qui trie un slice de chaînes de caractères par leur longueur.

## Exigences

- Le type `byLength` doit être créé comme un alias pour le type `[]string`.
- L'interface `sort.Interface` doit être implémentée sur le type `byLength`.
- Les fonctions `Len` et `Swap` doivent être implémentées sur le type `byLength`.
- La fonction `Less` doit être implémentée sur le type `byLength` pour contenir la logique de tri personnalisée réelle.
- La fonction `main` doit convertir le slice original `fruits` en `byLength`, puis utiliser `sort.Sort` sur ce slice typé.

## Exemple

```sh
# Exécuter notre programme affiche une liste triée par la
# longueur des chaînes, comme souhaité.
$ go run sorting-by-functions.go
[kiwi peach banana]

# En suivant ce même modèle de création d'un type
# personnalisé, d'implémentation des trois méthodes
# `Interface` sur ce type, puis d'appel de sort.Sort sur
# une collection de ce type personnalisé, nous pouvons
# trier les slices Go par des fonctions arbitraires.
```
