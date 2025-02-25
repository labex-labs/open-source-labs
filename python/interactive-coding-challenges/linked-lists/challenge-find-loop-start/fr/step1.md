# Trouver le début de la boucle

## Problème

Étant donné une liste chaînée simple, nous devons trouver le début d'une boucle s'il existe. Une boucle est définie comme un nœud de la liste qui pointe vers un nœud précédent, créant un cycle. Si n'y a pas de boucle, nous retournons None. Si une boucle existe, nous retournons le nœud où la boucle commence.

## Exigences

Pour résoudre ce problème, nous devons prendre en compte les exigences suivantes :

- La liste chaînée est une liste chaînée simple.
- Nous ne pouvons pas supposer que nous recevons toujours une liste chaînée circulaire.
- Lorsque nous trouvons une boucle, nous retournons le nœud où la boucle commence.
- Nous pouvons supposer que nous avons déjà une classe de liste chaînée qui peut être utilisée pour ce problème.

## Utilisation de l'exemple

Voici quelques exemples de manière dont cette fonction peut être utilisée :

- Liste vide -> None
- Pas une liste chaînée circulaire -> None
  - Un élément
  - Deux éléments ou plus
- Cas général d'une liste chaînée circulaire
