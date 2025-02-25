# Inverser un arbre

## Problème

Étant donné un arbre binaire, écrire une fonction pour inverser l'arbre. La fonction devrait prendre le nœud racine de l'arbre en entrée et renvoyer le nouveau nœud racine de l'arbre inversé.

## Exigences

Pour résoudre ce problème, vous devez répondre aux exigences suivantes :

- Vous devriez avoir une classe `Node` qui représente un nœud dans l'arbre binaire.
- Vous devriez échanger toutes les paires de nœuds gauche et droit dans l'arbre binaire.
- Vous devriez gérer les entrées invalides de manière appropriée.
- Votre solution devrait tenir dans la mémoire.

## Utilisation de l'exemple

Supposons que nous ayons l'arbre binaire suivant :

```txt
     5
   /   \
  2     7
 / \   / \
1   3 6   9
```

Après avoir inversé l'arbre, nous devrions obtenir :

```txt
     5
   /   \
  7     2
 / \   / \
9   6 3   1
```
