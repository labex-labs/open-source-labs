# Codes de formatage

Les codes de formatage (après le `:` à l'intérieur des `{}`) sont similaires à ceux de `printf()` en C. Les codes courants sont les suivants :

```code
d       Entier décimal
b       Entier binaire
x       Entier hexadécimal
f       Flottant sous la forme [-]m.dddddd
e       Flottant sous la forme [-]m.dddddde+-xx
g       Flottant, mais utilisation sélective de la notation scientifique
s       Chaîne de caractères
c       Caractère (à partir d'un entier)
```

Les modificateurs courants ajustent la largeur du champ et la précision décimale. Voici une liste partielle :

```code
:>10d   Entier aligné à droite dans un champ de 10 caractères
:<10d   Entier aligné à gauche dans un champ de 10 caractères
:^10d   Entier centré dans un champ de 10 caractères
:0.2f   Flottant avec une précision de 2 chiffres
```
