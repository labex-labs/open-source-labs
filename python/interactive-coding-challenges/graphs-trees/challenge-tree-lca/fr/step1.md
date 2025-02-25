# Arbre Binaire - LCA

## Problème

Étant donné un arbre binaire et deux nœuds, trouver leur ancêtre commun le plus proche.

## Exigences

Pour résoudre ce problème, nous devons prendre en compte les exigences suivantes :

- L'arbre donné est un arbre binaire, pas un arbre de recherche binaire.
- Nous ne pouvons pas supposer que les deux nœuds sont déjà présents dans l'arbre.
- Nous pouvons supposer que l'arbre binaire tient en mémoire.

## Utilisation Exemple

Considérez l'arbre binaire suivant :

```txt
          _10_
        /      \
       5        9
      / \      / \
     12  3    18  20
        / \       /
       1   8     40
```

Nous pouvons tester notre fonction avec les entrées et les sorties attendues suivantes :

- 0, 5 -> None (les deux nœuds ne sont pas dans l'arbre)
- 5, 0 -> None (les deux nœuds ne sont pas dans l'arbre)
- 1, 8 -> 3
- 12, 8 -> 5
- 12, 40 -> 10
- 9, 20 -> 9
- 3, 5 -> 5
