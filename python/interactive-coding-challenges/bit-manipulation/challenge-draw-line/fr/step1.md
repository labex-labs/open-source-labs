# Tracer une ligne

## Problème

Implémentez la méthode `draw_line(screen, width, x1, x2)` où `screen` est une liste d'octets, `width` est divisible par 8, et `x1`, `x2` sont des positions absolues de pixels. La méthode doit définir les bits correspondants dans `screen` pour tracer une ligne de `x1` à `x2`.

### Exigences

L'implémentation de `draw_line` doit répondre aux exigences suivantes :

- Les entrées ne peuvent pas être supposées valides.
- Les bits correspondants dans `screen` doivent être définis pour tracer la ligne.
- On peut supposer que l'implémentation rentre en mémoire.

## Utilisation de l'exemple

Les exemples suivants illustrent le comportement attendu de `draw_line` :

- Entrées invalides -> Exception
  - `screen` est vide
  - `width` = 0
  - tout paramètre d'entrée est `None`
  - `x1` ou `x2` est en dehors des limites
- Cas général pour `len(screen)` = 20, `width` = 32 :
  - `x1` = 2, `x2` = 6
    - `screen[0]` = `int('00111110', base=2)`
  - `x1` = 68, `x2` = 80
    - `screen[8]`, `int('00001111', base=2)`
    - `screen[9]`, `int('11111111', base=2)`
    - `screen[10]`, `int('10000000', base=2)`
