# Parcours en largeur d'un graphe

## Problème

La mise en œuvre du parcours en largeur (BFS - Breadth-First Search en anglais) sur un graphe consiste à visiter tous les sommets d'un graphe dans l'ordre de largeur, en partant d'un sommet source donné. L'algorithme fonctionne en visitant le sommet source, puis en visitant tous ses voisins, puis en visitant tous les voisins de ses voisins, et ainsi de suite. L'ordre dans lequel les sommets sont visités est important, car il détermine le plus court chemin du sommet source à tous les autres sommets du graphe.

## Exigences

Pour implémenter le parcours en largeur sur un graphe, les exigences suivantes doivent être satisfaites :

- Le graphe est dirigé.
- Les classes Graph et Node sont déjà disponibles.
- Le graphe est connexe.
- Les entrées sont valides.
- L'algorithme s'adapte à la mémoire.

## Utilisation exemple

Supposons qu'on ait un graphe avec les arêtes suivantes :

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

Si on lance le parcours en largeur à partir du sommet 0, l'ordre dans lequel les sommets sont visités sera [0, 1, 4, 5, 3, 2]. Cela signifie que le sommet 0 est visité en premier, suivi de ses voisins 1, 4 et 5, puis des voisins de 1 (3 et 4), puis du voisin de 3 (2).
