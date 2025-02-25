# Tri par sélection

## Problème

Implémentez le tri par sélection en Python. L'algorithme devrait prendre une liste d'entiers en entrée et renvoyer la liste triée. L'algorithme devrait fonctionner comme suit :

1. Trouvez l'élément minimum dans la partie non triée de la liste.
2. Échangez-le avec le premier élément de la partie non triée de la liste.
3. Décalez la limite de la partie triée de la liste d'un élément vers la droite.

Répétez les étapes 1-3 jusqu'à ce que toute la liste soit triée.

## Exigences

Pour implémenter le tri par sélection en Python, les exigences suivantes doivent être satisfaites :

- L'algorithme devrait prendre une liste d'entiers en entrée.
- L'algorithme devrait renvoyer une liste triée d'entiers.
- L'algorithme devrait être implémenté en utilisant l'algorithme de tri par sélection.
- L'algorithme devrait fonctionner pour des listes de toute longueur.
- L'algorithme devrait gérer les éléments dupliqués dans la liste.
- La liste d'entrée peut ne pas être triée.
- La liste d'entrée peut contenir des données invalides, telles que des valeurs non entières.
- L'algorithme devrait être efficace en mémoire et ne pas utiliser trop de mémoire.

## Utilisation exemple

Les exemples suivants démontrent l'utilisation de l'algorithme de tri par sélection :

- `selection_sort([])` renvoie `[]`
- `selection_sort([1])` renvoie `[1]`
- `selection_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])` renvoie `[1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]`
