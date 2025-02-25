# Parcours en largeur d'un arbre

## Problème

Étant donné un arbre binaire, implémentez une fonction qui effectue un parcours en largeur sur l'arbre. La fonction devrait appeler une méthode d'entrée `visit_func` sur chaque nœud lorsqu'il est traité.

## Exigences

Pour résoudre ce problème, les exigences suivantes doivent être satisfaites :

- Une classe `Node` avec une méthode `insert` est déjà disponible.
- La solution devrait tenir en mémoire.
- La méthode `visit_func` devrait être appelée sur chaque nœud lorsqu'il est traité.

## Exemple

### Parcours en largeur

Supposons qu'il existe un arbre binaire ayant la structure suivante :

```
    5
   / \
  2   8
 / \
1   3
```

Effectuer un parcours en largeur sur cet arbre entraînerait la visite des nœuds dans la séquence suivante : `5, 2, 8, 1, 3`.
