# Plus court chemin dans un graphe non pondéré

## Problème

Étant donné un graphe dirigé sans poids d'arête, trouver le plus court chemin entre deux nœuds.

## Exigences

Pour résoudre ce problème, les exigences suivantes doivent être satisfaites :

- Le graphe est dirigé.
- Le graphe est non pondéré.
- Les classes Graph et Node sont déjà disponibles.
- Les entrées sont deux nœuds.
- La sortie est une liste des clés de nœud qui constituent le plus court chemin.
- S'il n'y a pas de chemin, renvoyer None.
- Le graphe est connexe.
- Les entrées sont valides.
- L'algorithme doit tenir dans la mémoire.

## Utilisation de l'exemple

Supposons que nous ayons le graphe suivant :

```
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(0, 5)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 1)
graph.add_edge(3, 2)
graph.add_edge(3, 4)
```

Nous pouvons trouver le plus court chemin entre deux nœuds en utilisant la fonction `search_path` :

- `search_path(start=0, end=2) -> [0, 1, 3, 2]`
- `search_path(start=0, end=0) -> [0]`
- `search_path(start=4, end=5) -> None`
