# Supprimer le nœud du milieu

## Problème

Etant donné une liste chaînée simple non circulaire, supprimer un nœud au milieu de la liste, étant donné qu'on n'a accès qu'à ce nœud. Si le dernier nœud est supprimé, le transformer en un nœud fictif avec la valeur None. On peut supposer qu'on a déjà une classe de liste chaînée qui peut être utilisée pour ce problème.

## Exigences

Pour résoudre ce problème, nous devons prendre en compte les exigences suivantes :

- La liste chaînée est non circulaire et simple.
- Si le dernier nœud est supprimé, le transformer en un nœud fictif avec la valeur None.
- On a déjà une classe de liste chaînée qui peut être utilisée pour ce problème.

## Utilisation de l'exemple

Voici quelques exemples d'utilisation de cette fonction :

- Supprimer sur une liste vide devrait renvoyer None.
- Supprimer None devrait renvoyer None.
- Supprimer sur une liste avec un seul nœud devrait renvoyer [None].
- Supprimer sur une liste avec plusieurs nœuds devrait renvoyer la liste mise à jour avec le nœud supprimé.
