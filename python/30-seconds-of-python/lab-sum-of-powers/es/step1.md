# Suma de potencias

Escribe una función de Python llamada `sum_of_powers` que tome tres parámetros:

- `end` - un entero que representa el final del rango (inclusive)
- `power` - un entero que representa la potencia a la que se debe elevar cada número en el rango (valor predeterminado es 2)
- `start` - un entero que representa el inicio del rango (valor predeterminado es 1)

La función debe devolver la suma de las potencias de todos los números desde `start` hasta `end` (ambos inclusive).

Para resolver este problema, puedes seguir estos pasos:

1. Utiliza `range()` en combinación con una comprensión de listas para crear una lista de elementos en el rango deseado elevados a la `power` dada.
2. Utiliza `sum()` para sumar los valores juntos.

```python
def sum_of_powers(end, power = 2, start = 1):
  return sum([(i) ** power for i in range(start, end + 1)])
```

```python
sum_of_powers(10) # 385
sum_of_powers(10, 3) # 3025
sum_of_powers(10, 3, 5) # 2925
```
