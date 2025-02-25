# Graphe

## Problème

Implémentez un graphe qui satisfait les exigences suivantes :

### Exigences

- Le graphe peut être dirigé ou non dirigé.
- Les arêtes peuvent avoir des poids.
- Le graphe peut avoir des cycles.
- Si on essaie d'ajouter un nœud qui existe déjà, on ne fait rien.
- Si on essaie de supprimer un nœud qui n'existe pas, on ne fait rien.
- On peut supposer que c'est un graphe connexe.
- On peut supposer que les entrées sont valides.
- On peut supposer que cela rentre en mémoire.

## Utilisation de l'exemple

Entrée :

```
graph.add_edge(0, 1, 5)
graph.add_edge(0, 5, 2)
graph.add_edge(1, 2, 3)
graph.add_edge(2, 3, 4)
graph.add_edge(3, 4, 5)
graph.add_edge(3, 5, 6)
graph.add_edge(4, 0, 7)
graph.add_edge(5, 4, 8)
graph.add_edge(5, 2, 9)
```

Résultat :

- Les nœuds `0`, `1`, `2`, `3`, `4` et `5` sont connectés avec les poids spécifiés.

Remarque :

- La classe Graph sera utilisée comme base pour des défis de graphe plus complexes.
