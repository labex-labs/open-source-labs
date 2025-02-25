# Validation d'un ABR

## Problème

Le problème consiste à écrire une fonction Python qui prend en entrée le nœud racine d'un arbre binaire et détermine s'il s'agit d'un arbre binaire de recherche valide. Un arbre binaire est un arbre binaire de recherche valide si et seulement si les conditions suivantes sont remplies :

1. Le sous-arbre gauche d'un nœud ne contient que des nœuds dont les valeurs sont inférieures à la valeur du nœud.
2. Le sous-arbre droit d'un nœud ne contient que des nœuds dont les valeurs sont supérieures à la valeur du nœud.
3. Les deux sous-arbres gauche et droit sont eux-mêmes des arbres binaires de recherche valides.

## Exigences

Pour résoudre ce défi, les exigences suivantes doivent être remplies :

- La fonction doit être capable de gérer des arbres binaires avec des doublons.
- Si la fonction est appelée avec une entrée None, elle doit lever une exception.
- La classe Node devrait déjà être définie.
- L'arbre binaire doit tenir en mémoire.

## Utilisation de l'exemple

```txt
Valide :
      5
    /   \
   5     8
  /     /
 4     6
        \
         7

Non valide :
      5
    /   \
   5     8
  / \   /
 4   9 7
```
