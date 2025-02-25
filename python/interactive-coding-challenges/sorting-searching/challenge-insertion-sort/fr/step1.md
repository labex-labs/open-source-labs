# Tri par insertion

## Problème

Le problème est d'implémenter le tri par insertion en Python. Étant donné une liste non triée d'éléments, l'algorithme devrait trier la liste par ordre croissant. L'algorithme fonctionne en itérant sur la liste et en insérant chaque élément à sa position correcte dans la partie triée de la liste.

L'algorithme commence en supposant que le premier élément de la liste est déjà trié. Il itère ensuite sur les éléments restants de la liste, en comparant chaque élément aux éléments de la partie triée de la liste. Si l'élément est plus petit que l'élément actuel dans la partie triée de la liste, il est inséré avant cet élément. Si l'élément est plus grand que tous les éléments de la partie triée de la liste, il est inséré à la fin de la partie triée de la liste.

## Exigences

Pour implémenter le tri par insertion en Python, les exigences suivantes doivent être satisfaites :

- Une solution naïve est suffisante.
- Les doublons sont autorisés.
- L'entrée n'est pas nécessairement valide, donc l'algorithme devrait gérer gracefully les entrées invalides.
- L'algorithme devrait tenir dans la mémoire.

## Utilisation exemple

Voici quelques exemples d'utilisation de l'algorithme de tri par insertion :

- None -> Exception : Si l'entrée est None, une exception devrait être levée.
- Entrée vide -> [] : Si l'entrée est une liste vide, la sortie devrait également être une liste vide.
- Un élément -> [élément] : Si l'entrée est une liste avec un seul élément, la sortie devrait être la même liste.
- Deux éléments ou plus : Si l'entrée est une liste avec deux éléments ou plus, la sortie devrait être une liste triée par ordre croissant.
