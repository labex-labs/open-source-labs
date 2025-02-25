# Table de hachage

## Problème

Implémentez une table de hachage avec des méthodes de définition, de récupération et de suppression. La table de hachage devrait utiliser la chaînage pour la résolution des collisions. Les clés sont uniquement des entiers. Nous n'avons pas à nous soucier des facteurs de charge ou de valider les entrées. Nous pouvons supposer que la table de hachage tient en mémoire.

## Exigences

- Les clés sont uniquement des entiers.
- Le chaînage est utilisé pour la résolution des collisions.
- Les facteurs de charge n'ont pas besoin d'être considérés.
- Les entrées n'ont pas besoin d'être validées.
- La table de hachage tient en mémoire.

## Utilisation exemple

- Méthode `get`:
  - Si il n'y a pas de clé correspondante, une exception KeyError est levée.
  - Si il y a une clé correspondante, la valeur correspondante est renvoyée.
- Méthode `set`:
  - Si il n'y a pas de clé correspondante, une nouvelle paire clé-valeur est ajoutée à la table de hachage.
  - Si il y a une clé correspondante, la valeur correspondante est mise à jour.
- Méthode `remove`:
  - Si il n'y a pas de clé correspondante, une exception KeyError est levée.
  - Si il y a une clé correspondante, la paire clé-valeur correspondante est supprimée de la table de hachage.
