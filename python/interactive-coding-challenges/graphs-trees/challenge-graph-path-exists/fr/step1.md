# Existence d'un chemin dans un graphe

## Problème

Étant donné un graphe dirigé et deux nœuds, écrire une fonction Python pour déterminer s'il existe un chemin entre les deux nœuds.

## Exigences

Pour résoudre ce problème, nous devons faire les hypothèses suivantes :

- Le graphe est dirigé.
- Nous disposons déjà des classes Graph et Node.
- Le graphe est connexe.
- Les entrées sont valides.
- La solution s'adapte à la mémoire.

## Utilisation de l'exemple

Supposons que nous ayons le graphe suivant :

```
graph.add_edge(0, 1, 5)
graph.add_edge(0, 4, 3)
graph.add_edge(0, 5, 2)
graph.add_edge(1, 3, 5)
graph.add_edge(1, 4, 4)
graph.add_edge(2, 1, 6)
graph.add_edge(3, 2, 7)
graph.add_edge(3, 4, 8)
```

Nous pouvons utiliser la fonction suivante pour déterminer s'il existe un chemin entre deux nœuds :

```
search_path(start=0, end=2) -> True
search_path(start=0, end=0) -> True
search_path(start=4, end=5) -> False
```

Les deux premiers appels de fonction renvoient True car il existe un chemin entre les nœuds de départ et d'arrivée. Le dernier appel de fonction renvoie False car il n'y a pas de chemin entre les nœuds de départ et d'arrivée.
