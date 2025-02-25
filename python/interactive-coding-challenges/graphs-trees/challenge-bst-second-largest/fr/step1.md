# Bst Second Largest

## Problème

Étant donné un arbre binaire de recherche, trouver le deuxième nœud le plus grand de l'arbre. Si l'entrée est None ou un seul nœud, une exception doit être levée.

Pour résoudre ce problème, nous pouvons parcourir l'arbre dans un ordre spécifique et garder la trace du deuxième nœud le plus grand que nous ayons vu jusqu'à présent. Nous pouvons commencer en parcourant le sous-arbre droit du nœud racine, et si le sous-arbre droit est None, alors le nœud le plus grand est le nœud racine lui-même. Si le sous-arbre droit n'est pas None, nous pouvons continuer à parcourir le sous-arbre droit jusqu'à ce que nous atteignions un nœud qui n'a pas de fils droit. À ce stade, le nœud le plus grand de l'arbre est le parent de ce nœud. Si ce nœud parent a un fils gauche, alors le deuxième nœud le plus grand est le nœud le plus grand du sous-arbre gauche du nœud parent. Si le nœud parent n'a pas de fils gauche, alors le deuxième nœud le plus grand est le nœud parent lui-même.

## Exigences

Les exigences de ce défi sont les suivantes :

- Si l'entrée est None ou un seul nœud, une exception doit être levée.
  - Une entrée None doit lever une TypeError.
  - Une entrée de seul nœud doit lever une ValueError.
- Nous pouvons supposer qu'il existe déjà une classe Node avec une méthode insert.
- Nous pouvons supposer que ce problème s'adapte à la mémoire.

## Utilisation Exemple

Voici quelques exemples d'utilisation de cette fonction :

- None ou seul nœud -> Exception

```txt
Entrée :
                _10_
              _/    \_
             5        15
            / \       / \
           3   8     12  20
          /     \         \
         2       4        30

Sortie : 20

Entrée :
                 10
                 /
                5
               / \
              3   7
Sortie : 7
```
