# Liste chaînée

## Problème

Implémentez une liste chaînée avec les méthodes suivantes :

- insert(value) : insère un nouveau nœud avec la valeur donnée au début de la liste
- append(value) : insère un nouveau nœud avec la valeur donnée à la fin de la liste
- find(value) : renvoie le premier nœud de la liste avec la valeur donnée, ou None si aucun tel nœud n'existe
- delete(value) : supprime le premier nœud de la liste avec la valeur donnée, ou ne fait rien si aucun tel nœud n'existe
- length() : renvoie le nombre de nœuds dans la liste
- print() : affiche les valeurs de tous les nœuds de la liste, séparées par des espaces

## Exigences

L'implémentation de la liste chaînée doit répondre aux exigences suivantes :

- La liste chaînée est non circulaire et simplement chaînée.
- L'implémentation ne suit que la tête de la liste, pas la queue.
- Les valeurs None ne peuvent pas être insérées dans la liste.

## Utilisation exemple

### Insertion au début

- Insérer une None : Lève une erreur car les valeurs None ne peuvent pas être insérées dans la liste.
- Insérer dans une liste vide : Insère la valeur comme premier nœud de la liste.
- Insérer dans une liste avec un élément ou plus d'éléments : Insère la valeur comme premier nœud de la liste, déplaçant les nœuds existants vers la droite.

### Ajout à la fin

- Ajouter une None : Lève une erreur car les valeurs None ne peuvent pas être insérées dans la liste.
- Ajouter dans une liste vide : Insère la valeur comme premier nœud de la liste.
- Ajouter dans une liste avec un élément ou plus d'éléments : Insère la valeur comme dernier nœud de la liste, en mettant à jour la référence du précédent dernier nœud pour qu'il pointe vers le nouveau nœud.

### Recherche

- Rechercher une None : Renvoie None car les valeurs None ne peuvent pas être trouvées dans la liste.
- Rechercher dans une liste vide : Renvoie None car il n'y a aucun nœud dans la liste.
- Rechercher dans une liste avec un élément ou plus d'éléments correspondants : Renvoie le premier nœud de la liste avec la valeur donnée.
- Rechercher dans une liste sans correspondance : Renvoie None car il n'y a aucun nœud dans la liste avec la valeur donnée.

### Suppression

- Supprimer une None : Ne fait rien car les valeurs None ne peuvent pas être supprimées de la liste.
- Supprimer dans une liste vide : Ne fait rien car il n'y a aucun nœud dans la liste.
- Supprimer dans une liste avec un élément ou plus d'éléments correspondants : Supprime le premier nœud de la liste avec la valeur donnée, déplaçant les nœuds existants vers la gauche.
- Supprimer dans une liste sans correspondance : Ne fait rien car il n'y a aucun nœud dans la liste avec la valeur donnée.

### Longueur

- Longueur de zéro ou plus d'éléments : Renvoie le nombre de nœuds dans la liste.

### Affichage

- Afficher une liste vide : N'affiche rien.
- Afficher une liste avec un ou plus d'éléments : Affiche les valeurs de tous les nœuds de la liste, séparées par des espaces.
