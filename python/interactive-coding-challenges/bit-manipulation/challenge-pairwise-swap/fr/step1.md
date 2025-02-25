# Échange pair à pair

## Problème

Étant donné un entier positif, permute les bits pairs et impairs avec le moins d'opérations possible. Par exemple, si l'entrée est `1001 1111 0110`, la sortie devrait être `0110 1111 1001`.

## Exigences

Les exigences suivantes doivent être satisfaites :

- L'entrée est toujours un entier positif.
- Le programme fonctionne avec 32 bits.
- La sortie est un entier.
- Les entrées sont valides (pas None).
- Le programme s'adapte à la mémoire.

## Utilisation de l'exemple

Les exemples suivants illustrent l'utilisation du programme :

- None -> Exception
- 0 -> 0
- -1 -> -1
- Cas général :

```
    entrée  = 1001 1111 0110
    résultat = 0110 1111 1001
```
