# Ruta en la cuadrícula

## Problema

Dada una cuadrícula rectangular con celdas válidas e inválidas, implementa una función para encontrar una ruta válida para que el robot se mueva desde la esquina superior izquierda hasta la esquina inferior derecha. Si no hay una ruta válida, devuelve `None`. Si la entrada es inválida o la matriz está vacía, devuelve `None`.

## Requisitos

Los requisitos de este algoritmo son los siguientes:

- El robot solo puede moverse hacia la derecha y hacia abajo.
- Algunas celdas pueden estar fuera de límites.
- La cuadrícula es rectangular y no tiene bordes irregulares.
- No siempre habrá una ruta válida para que el robot llegue a la esquina inferior derecha.
- La entrada no siempre será válida.
- El algoritmo debe ajustarse a las restricciones de memoria.

## Uso de ejemplo

Considere la siguiente cuadrícula:

```txt
o = celda válida
x = celda inválida

   0  1  2  3
0  o  o  o  o
1  o  x  o  o
2  o  o  x  o
3  x  o  o  o
4  o  o  x  o
5  o  o  o  x
6  o  x  o  x
7  o  x  o  o
```

- Caso general:

```txt
esperado = [(0, 0), (1, 0), (2, 0),
            (2, 1), (3, 1), (4, 1),
            (5, 1), (5, 2), (6, 2),
            (7, 2), (7, 3)]
```

- Sin ruta válida: En el ejemplo anterior, la fila 7 columna 2 también es inválida -> `None`
- Entrada `None` -> `None`
- Matriz vacía -> `None`
