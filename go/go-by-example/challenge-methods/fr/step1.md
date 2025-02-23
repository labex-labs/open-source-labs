# Méthodes

Le code fourni définit un type de structure appelé `rect` avec deux champs, `width` et `height`. Deux méthodes sont définies pour ce type de structure, `area` et `perim`. La méthode `area` calcule l'aire du rectangle, et la méthode `perim` calcule le périmètre du rectangle. La fonction principale appelle ces deux méthodes et imprime leurs résultats.

## Exigences

- La méthode `area` doit avoir un type de récepteur de `*rect`.
- La méthode `perim` doit avoir un type de récepteur de `rect`.
- La méthode `area` doit retourner l'aire du rectangle.
- La méthode `perim` doit retourner le périmètre du rectangle.
- La fonction `main` doit appeler les deux méthodes et imprimer leurs résultats.

## Exemple

```sh
$ go run methods.go
area: 50
perim: 30
area: 50
perim: 30

# Ensuite, nous examinerons le mécanisme de Go pour regrouper et
# nommer des ensembles de méthodes apparentées : les interfaces.
```
