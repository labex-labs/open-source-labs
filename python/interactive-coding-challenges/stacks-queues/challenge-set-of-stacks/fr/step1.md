# Ensemble de piles

## Problème

Implémentez une classe SetOfStacks qui encapsule une liste de piles, où chaque pile est limitée par une capacité. La classe devrait avoir les fonctionnalités suivantes :

- Empilez un élément au sommet de la dernière pile de la liste. Si la dernière pile est pleine, créez une nouvelle pile et ajoutez l'élément à la nouvelle pile.
- Dépilez l'élément supérieur de la dernière pile de la liste. Si la dernière pile est vide, supprimez-la de la liste et dépilez l'élément supérieur de la nouvelle dernière pile de la liste. Si la liste est vide, renvoyez None.
- Dépilez un élément d'une pile spécifique de la liste. Si la pile est vide, supprimez-la de la liste. Si la liste est vide, renvoyez None.

## Exigences

La classe SetOfStacks devrait répondre aux exigences suivantes :

- La classe devrait utiliser une classe de pile existante.
- Toutes les piles de la liste devraient être limitées par la même capacité.
- Si une pile devient pleine, une nouvelle pile devrait être créée automatiquement pour stocker les éléments supplémentaires.
- Si une pile devient vide, elle devrait être supprimée de la liste.
- Si nous dépilons sur une pile vide, la méthode devrait renvoyer None.
- L'implémentation devrait tenir dans la mémoire.

## Utilisation exemple

La classe SetOfStacks peut être utilisée dans les scénarios suivants :

- Empiler et dépiler sur une pile vide.
- Empiler et dépiler sur une pile non vide.
- Empiler sur une pile à capacité pour en créer une nouvelle.
- Dépiler sur une pile pour la détruire.
