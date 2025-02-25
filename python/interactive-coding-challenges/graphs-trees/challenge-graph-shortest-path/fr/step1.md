# Plus court chemin dans un graphe

## Problème

Étant donné un graphe dirigé avec des arêtes pondérées, trouver le plus court chemin entre deux nœuds.

## Exigences

Pour résoudre ce problème, nous devons prendre en compte les exigences suivantes :

- S'agit-il d'un graphe orienté? - Oui
- Le graphe peut-il avoir des cycles? - Oui
  - Note : Si la réponse était non, ce serait un DAG.
    - Les DAGs peuvent être résolus avec un [tri topologique](http://www.geeksforgeeks.org/shortest-path-for-directed-acyclic-graphs/)
- Les arêtes sont-elles pondérées? - Oui
  - Note : Si les arêtes n'étaient pas pondérées, on pourrait effectuer une BFS
- Les arêtes sont-elles toutes des nombres non négatifs? - Oui
  - Note : Les graphes avec des arêtes négatives peuvent être traités avec l'algorithme de Bellman-Ford
    - Les graphes avec des cycles à coût négatif n'ont pas de plus court chemin défini
- Dois-je vérifier les arêtes non négatives? - Non
- Peut-on supposer que c'est un graphe connexe? - Oui
- Peut-on supposer que les entrées sont valides? - Non
- Peut-on supposer que nous avons déjà une classe de graphe? - Oui
- Peut-on supposer que nous avons déjà une classe de file d'attente prioritaire? - Oui
- Peut-on supposer que cela tient dans la mémoire? - Oui

## Exemple

Considérez le graphe suivant :

```txt
graph.add_edge('a', 'b', weight=5)
graph.add_edge('a', 'c', weight=3)
graph.add_edge('a', 'e', weight=2)
graph.add_edge('b', 'd', weight=2)
graph.add_edge('c', 'b', weight=1)
graph.add_edge('c', 'd', weight=1)
graph.add_edge('d', 'a', weight=1)
graph.add_edge('d', 'g', weight=2)
graph.add_edge('d', 'h', weight=1)
graph.add_edge('e', 'a', weight=1)
graph.add_edge('e', 'h', weight=4)
graph.add_edge('e', 'i', weight=7)
graph.add_edge('f', 'b', weight=3)
graph.add_edge('f', 'g', weight=1)
graph.add_edge('g', 'c', weight=3)
graph.add_edge('g', 'i', weight=2)
graph.add_edge('h', 'c', weight=2)
graph.add_edge('h', 'f', weight=2)
graph.add_edge('h', 'g', weight=2)
```

Nous pouvons trouver le plus court chemin entre le nœud 'a' et le nœud 'i' en utilisant la classe ShortestPath :

```txt
shortest_path = ShortestPath(graph)
result = shortest_path.find_shortest_path('a', 'i')
```

Le résultat attendu est :

```txt
['a', 'c', 'd', 'g', 'i']
```

Nous pouvons également vérifier le poids du plus court chemin :

```txt
self.assertEqual(shortest_path.path_weight['i'], 8)
```
