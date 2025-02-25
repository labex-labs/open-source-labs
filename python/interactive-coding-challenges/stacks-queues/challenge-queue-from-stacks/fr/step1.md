# File à partir de piles

## Problème

Implémenter une file à l'aide de deux piles peut être un problème difficile. L'idée de base est d'utiliser une pile pour les opérations d'enfilement et l'autre pile pour les opérations de défilement. Lorsqu'un élément est enfilé, il est empilé sur la première pile. Lorsqu'un élément est défilé, il est dépilé de la deuxième pile. Si la deuxième pile est vide, on dépile tous les éléments de la première pile et on les empile sur la deuxième pile dans l'ordre inverse. Cela assure que le premier élément qui a été enfilé est le premier élément qui est défilé.

## Exigences

Pour résoudre ce problème, nous devons prendre en compte les exigences suivantes :

- Nous devons implémenter deux méthodes : enfile et défile.
- Nous supposons qu'il existe déjà une classe Pile qui peut être utilisée pour ce problème.
- Nous ne pouvons pas empiler une valeur None sur la Pile.
- Nous pouvons supposer que ce problème s'adapte à la mémoire.

## Utilisation exemple

Voici quelques exemples de manière dont nous pouvons utiliser notre implémentation d'une file à l'aide de deux piles :

- Enfiler et défiler sur une pile vide : Nous pouvons enfiler un élément sur la file puis le défiler pour nous assurer que la file fonctionne correctement.
- Enfiler et défiler sur une pile non vide : Nous pouvons enfiler plusieurs éléments sur la file puis les défiler pour nous assurer que la file fonctionne correctement.
- Plusieurs enfilements consécutifs : Nous pouvons enfiler plusieurs éléments sur la file successivement puis les défiler pour nous assurer que la file fonctionne correctement.
- Plusieurs défilements consécutifs : Nous pouvons enfiler plusieurs éléments sur la file puis les défiler successivement pour nous assurer que la file fonctionne correctement.
- Enfiler après un défilement : Nous pouvons enfiler un élément sur la file, le défiler, puis enfiler un autre élément sur la file pour nous assurer que la file fonctionne correctement.
- Défiler après un enfilement : Nous pouvons enfiler un élément sur la file, le défiler, puis enfiler un autre élément sur la file pour nous assurer que la file fonctionne correctement.
