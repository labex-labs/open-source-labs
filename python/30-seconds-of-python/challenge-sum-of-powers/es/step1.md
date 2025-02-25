# Desafío de la suma de potencias

## Problema

Escribe una función de Python llamada `sum_of_powers` que tome tres parámetros:

- `end` - un entero que representa el final del rango (inclusive)
- `power` - un entero que representa la potencia a la que se debe elevar cada número en el rango (valor predeterminado es 2)
- `start` - un entero que representa el inicio del rango (valor predeterminado es 1)

La función debe devolver la suma de las potencias de todos los números desde `start` hasta `end` (ambos inclusive).

Para resolver este problema, puedes seguir estos pasos:

1. Utiliza `range()` en combinación con una comprensión de listas para crear una lista de elementos en el rango deseado elevados a la `power` dada.
2. Utiliza `sum()` para sumar los valores juntos.

## Ejemplo

```python
sum_of_powers(10) # devuelve 385
sum_of_powers(10, 3) # devuelve 3025
sum_of_powers(10, 3, 5) # devuelve 2925
```
