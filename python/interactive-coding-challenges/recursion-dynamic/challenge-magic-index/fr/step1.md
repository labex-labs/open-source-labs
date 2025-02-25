# Indice magique

## Problème

Étant donné un tableau trié d'entiers avec des doublons possibles, écrire une fonction Python pour trouver l'indice magique, s'il existe, dans le tableau. Si plusieurs valeurs magiques existent, retourner la plus à gauche. Si aucun indice magique n'existe, retourner -1.

## Exigences

Pour résoudre le problème, les exigences suivantes doivent être satisfaites :

- Le tableau est trié.
- Les éléments du tableau ne sont pas nécessairement distincts.
- Des valeurs négatives sont autorisées dans le tableau.
- Si aucun indice magique n'existe, retourner -1.

## Utilisation de l'exemple

Les exemples suivants illustrent l'utilisation de la fonction :

- Aucune entrée -> -1
- Tableau vide -> -1

```txt
a[i]  -4 -2  2  6  6  6  6 10
  i    0  1  2  3  4  5  6  7
```

Résultat : 2

```txt
a[i]  -4 -2  1  6  6  6  6 10
  i    0  1  2  3  4  5  6  7
```

Résultat : 6

```txt
a[i]  -4 -2  1  6  6  6  7 10
  i    0  1  2  3  4  5  6  7
```

Résultat : -1
