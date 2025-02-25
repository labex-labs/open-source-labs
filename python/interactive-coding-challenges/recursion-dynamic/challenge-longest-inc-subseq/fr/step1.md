# Plus longue sous-suite croissante

## Problème

Étant donné une séquence d'entiers, trouver la plus longue sous-suite croissante. La sous-suite peut être non contiguë et peut contenir des doublons. S'il existe plusieurs solutions, renvoyer n'importe laquelle.

## Exigences

Pour résoudre ce problème, nous devons prendre en compte les exigences suivantes :

- Les doublons sont-ils possibles?
  - Oui
- Peut-on supposer que les entrées sont des entiers?
  - Oui
- Peut-on supposer que les entrées sont valides?
  - Non, nous devons gérer les entrées invalides.
- Est-ce que l'on s'attend à ce que le résultat soit un tableau de la plus longue sous-suite croissante?
  - Oui
- Peut-on supposer que cela rentre en mémoire?
  - Oui

## Utilisation de l'exemple

Voici quelques exemples de l'utilisation de cette fonction :

- Aucune -> Exception
- [] -> []
- [3, 4, -1, 0, 6, 2, 3] -> [-1, 0, 2, 3]
