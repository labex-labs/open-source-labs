# Recherche en profondeur (DFS) sur un graphe

## Problème

Implémenter la recherche en profondeur sur un graphe dirigé. L'algorithme devrait commencer à un nœud donné et visiter tous les nœuds atteignables dans le graphe. L'ordre dans lequel les nœuds sont visités devrait être enregistré et renvoyé sous forme de liste.

## Exigences

Pour implémenter la DFS sur un graphe dirigé, les exigences suivantes doivent être satisfaites :

- Le graphe est dirigé.
- Les classes Graph et Node sont déjà implémentées.
- Le graphe est connexe.
- Les entrées sont valides.
- L'algorithme s'adapte à la mémoire.

## Utilisation de l'exemple

Supposons qu'il existe un graphe dirigé avec les arêtes suivantes :

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

Si nous commençons la DFS au nœud 0, l'ordre des nœuds visités devrait être [0, 1, 3, 2, 4, 5].
