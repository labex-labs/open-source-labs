# Obtenir le suivant

## Problème

Étant donné un entier positif, vous devez trouver le plus grand nombre et le plus petit nombre suivants ayant le même nombre de 1 que le nombre donné. Par exemple, si l'entrée est 0000 0000 1101 0111, la sortie devrait être 0000 0000 1101 1011 pour le plus grand nombre suivant et 0000 0000 1100 1111 pour le plus petit nombre suivant.

## Exigences

Pour résoudre ce défi, vous devez répondre aux exigences suivantes :

- La sortie doit être un entier positif.
- Les entrées peuvent ne pas être valides, donc vous devez gérer les exceptions.
- La solution doit tenir en mémoire.

## Utilisation de l'exemple

Voici quelques exemples d'utilisation de cette fonction :

- Aucun -> Exception
- 0 -> Exception
- Entier négatif -> Exception
- Cas général :

```txt
    * Entrée :         0000 0000 1101 0111
    * Plus grand suivant :  0000 0000 1101 1011
    * Plus petit suivant : 0000 0000 1100 1111
```
