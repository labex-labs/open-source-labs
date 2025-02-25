# Vérifier l'équilibre

## Problème

Étant donné un arbre binaire, écrire une fonction Python pour déterminer s'il est équilibré. Un arbre binaire est considéré comme équilibré si les hauteurs des deux sous-arbres de tout nœud diffèrent d'au plus un. La fonction devrait prendre le nœud racine de l'arbre binaire en entrée et renvoyer True si l'arbre est équilibré, et False sinon. Si l'entrée est None, la fonction devrait lever une exception.

## Exigences

Pour résoudre ce problème, nous devons répondre aux exigences suivantes :

- Un arbre équilibré est un arbre où les hauteurs des deux sous-arbres de tout nœud ne diffèrent pas de plus de 1.
- Si l'entrée est None, la fonction devrait lever une exception.
- Nous pouvons supposer qu'il existe déjà une classe Node avec une méthode d'insertion.
- Nous pouvons supposer que le programme s'adapte à la mémoire.

## Utilisation de l'exemple

Voici quelques exemples de comportement attendu de la fonction :

- None -> lever une exception
- 1 -> True
- 5, 3, 8, 1, 4 -> True
- 5, 3, 8, 9, 10 -> False
