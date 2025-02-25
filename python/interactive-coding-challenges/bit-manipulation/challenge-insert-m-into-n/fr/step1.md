# Insérer M dans N

## Problème

Étant donné deux nombres sur 16 bits, `n` et `m`, et deux indices `i` et `j`, insérer `m` dans `n` de telle sorte que `m` commence au bit `j` et se termine au bit `i`. Le programme doit gérer les cas suivants :

- Si aucun n'est donné en entrée, une exception doit être levée.
- Si un indice négatif est donné pour `i` ou `j`, une exception doit être levée.
- Si les entrées sont invalides, une exception doit être levée.
- Si `i` jusqu'à `j` n'a pas assez d'espace pour `m`, une exception doit être levée.

Le programme doit renvoyer le nombre sur 16 bits résultant après l'insertion.

## Exigences

Le programme doit répondre aux exigences suivantes :

- `j` doit être supérieur à `i`.
- `i` jusqu'à `j` doit avoir assez d'espace pour `m`.
- Les entrées doivent être valides.
- Le programme doit tenir dans la mémoire.

## Utilisation de l'exemple

Voici un exemple d'utilisation du programme :

```txt
i      = 2
j      = 6
n      = 0000 0100 0000 0000
m      = 0000 0000 0001 0011
result = 0000 0100 0100 1100
```

Dans cet exemple, `m` est inséré dans `n` de telle sorte que `m` commence au bit `j = 6` et se termine au bit `i = 2`. Le nombre sur 16 bits résultant est `0000 0100 0100 1100`.
