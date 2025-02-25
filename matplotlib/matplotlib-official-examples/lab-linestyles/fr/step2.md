# Définissez les styles de ligne

Il existe différentes manières de définir les styles de ligne dans Matplotlib. Nous pouvons utiliser des styles prédéfinis tels que'solid' (solide), 'dashed' (tracé discontinu), 'dotted' (tracé pointillé) et 'dashdot' (tracé pointillé et discontinu). Nous pouvons également définir des styles de ligne personnalisés en utilisant un tuple de tirets.

```python
linestyle_str = [
     ('solid','solide'),      # Identique à (0, ()) ou '-'
     ('dotted', 'pointillé'),    # Identique à (0, (1, 1)) ou ':'
     ('dashed', 'tracé discontinu'),    # Identique à '--'
     ('dashdot', 'tracé pointillé et discontinu')]  # Identique à '-.'

linestyle_tuple = [
     ('loosely dotted',        (0, (1, 10))),
     ('dotted',                (0, (1, 1))),
     ('densely dotted',        (0, (1, 1))),
     ('long dash with offset', (5, (10, 3))),
     ('loosely dashed',        (0, (5, 10))),
     ('dashed',                (0, (5, 5))),
     ('densely dashed',        (0, (5, 1))),

     ('loosely dashdotted',    (0, (3, 10, 1, 10))),
     ('dashdotted',            (0, (3, 5, 1, 5))),
     ('densely dashdotted',    (0, (3, 1, 1, 1))),

     ('dashdotdotted',         (0, (3, 5, 1, 5, 1, 5))),
     ('loosely dashdotdotted', (0, (3, 10, 1, 10, 1, 10))),
     ('densely dashdotdotted', (0, (3, 1, 1, 1, 1, 1)))]
```
