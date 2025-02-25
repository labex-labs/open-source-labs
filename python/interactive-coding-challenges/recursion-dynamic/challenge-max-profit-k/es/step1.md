# Ganancia máxima K

## Problema

Dada una lista de precios de acciones en cada día consecutivo, determinar las ganancias máximas con k transacciones. El problema requiere determinar la máxima ganancia que se puede obtener a partir de una lista de precios de acciones en días consecutivos, considerando k transacciones. Las transacciones consisten en la compra y venta de acciones, y el número máximo de transacciones está limitado a k. La solución debe devolver la máxima ganancia y los días para comprar y vender.

## Requisitos

Para resolver el problema, deben cumplirse los siguientes requisitos:

- k representa el número de transacciones de venta.
- La entrada de precios es una matriz de enteros.
- Las entradas pueden no ser válidas.
- Si los precios están todos en descenso y no hay oportunidad de obtener una ganancia, la solución debe devolver 0.
- La salida debe ser la máxima ganancia y los días para comprar y vender.
- La solución debe ajustarse a la memoria.

## Uso de ejemplo

Los siguientes ejemplos ilustran el uso de la solución:

- Precios: Ninguno o k: Ninguno -> Ninguno
- Precios: [] o k <= 0 -> []
- Precios: [0, -1, -2, -3, -4, -5]
  - (ganancia máxima, lista de transacciones)
  - (0, [])
- Precios: [2, 5, 7, 1, 4, 3, 1, 3] k: 3
  - (ganancia máxima, lista de transacciones)
  - (10, [Tipo.VENTA día: 7 precio: 3,
    Tipo.COMPRA día: 6 precio: 1,
    Tipo.VENTA día: 4 precio: 4,
    Tipo.COMPRA día: 3 precio: 1,
    Tipo.VENTA día: 2 precio: 7,
    Tipo.COMPRA día: 0 precio: 2])
