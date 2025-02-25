# Definir estilos de línea

Existen diferentes maneras de definir estilos de línea en Matplotlib. Podemos usar estilos predefinidos como 'solid' (sólido), 'dashed' (tracejado), 'dotted' (punteado) y 'dashdot' (punto y rayado). También podemos definir estilos de línea personalizados usando una tupla de guiones.

```python
linestyle_str = [
     ('solid', 'solid'),      # Lo mismo que (0, ()) o '-'
     ('dotted', 'dotted'),    # Lo mismo que (0, (1, 1)) o ':'
     ('dashed', 'dashed'),    # Lo mismo que '--'
     ('dashdot', 'dashdot')]  # Lo mismo que '-.'

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
