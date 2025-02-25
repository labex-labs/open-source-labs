# File Liste

## Problème

Implémentez une file avec des méthodes d'enfilement et de défilement à l'aide d'une liste chaînée. La méthode d'enfilement devrait ajouter un élément à la fin de la file, et la méthode de défilement devrait supprimer un élément du début de la file. Si la file est vide, la défilement devrait renvoyer None.

## Exigences

Pour implémenter la file, nous devons suivre les exigences suivantes :

- Si une seule entrée se trouve dans la liste, les pointeurs first et last devraient tous les deux pointer vers elle.
- Si aucune entrée ne se trouve dans la liste, les pointeurs first et last devraient être None.
- Si vous effectuez un défilement sur une file vide, elle devrait renvoyer None.
- Nous pouvons supposer que cela s'adapte à la mémoire.

## Utilisation Exemple

### Enfilement

- Enfilement dans une file vide : Si la file est vide, la méthode d'enfilement devrait ajouter l'élément comme premier et dernier élément de la file.
- Enfilement dans une file non vide : Si la file n'est pas vide, la méthode d'enfilement devrait ajouter l'élément à la fin de la file.

### Défilement

- Défilement d'une file vide -> None : Si la file est vide, la méthode de défilement devrait renvoyer None.
- Défilement d'une file avec un seul élément : Si la file ne contient qu'un seul élément, la méthode de défilement devrait supprimer l'élément et définir les pointeurs first et last sur None.
- Défilement d'une file avec plus d'un élément : Si la file contient plus d'un élément, la méthode de défilement devrait supprimer le premier élément et définir le pointeur first sur l'élément suivant.
