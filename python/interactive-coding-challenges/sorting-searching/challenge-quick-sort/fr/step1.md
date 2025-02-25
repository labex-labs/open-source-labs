# Tri Rapide

## Problème

Implémentez l'algorithme de Tri Rapide en Python. L'algorithme devrait prendre une liste non triée en entrée et renvoyer une liste triée. L'algorithme devrait fonctionner pour des listes de toute taille, y compris des listes vides et des listes avec des éléments dupliqués. L'algorithme devrait également gérer les entrées invalides de manière appropriée.

L'algorithme de Tri Rapide fonctionne comme suit :

1. Choisissez un élément pivot dans la liste.
2. Partitionnez la liste en deux sous-listes : une avec les éléments inférieurs au pivot et une avec les éléments supérieurs au pivot.
3. Appliquez récursivement l'algorithme de Tri Rapide aux sous-listes.
4. Concaténez les sous-listes triées avec l'élément pivot au milieu.

## Exigences

Pour implémenter l'algorithme de Tri Rapide en Python, les exigences suivantes doivent être satisfaites :

- L'algorithme ne doit pas être une solution en place.
- L'algorithme doit gérer les éléments dupliqués dans la liste.
- L'algorithme doit gérer les entrées invalides, telles que None ou une entrée non liste.
- L'algorithme doit être capable de gérer des listes de toute taille, y compris des listes vides.

## Utilisation Exemple

Voici quelques exemples d'utilisation de l'algorithme de Tri Rapide en Python :

- None -> Exception

```python
quick_sort(None)
```

- Entrée vide -> []

```python
quick_sort([])
```

- Un élément -> [élément]

```python
quick_sort([5])
```

- Deux éléments ou plus

```python
quick_sort([5, 2, 8, 3, 1, 9])
```
