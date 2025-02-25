# Desafío del mínimo común múltiplo

## Problema

Escribe una función `lcm(numbers)` que tome una lista de números como argumento y devuelva su mínimo común múltiplo. Tu función debe utilizar la siguiente fórmula para calcular el MCM de dos números `x` e `y`: `mcm(x, y) = x * y / mcd(x, y)`, donde `mcd(x, y)` es el máximo común divisor de `x` e `y`.

Para resolver este problema, puedes utilizar la función `functools.reduce()` para aplicar la fórmula `mcm()` a todos los números de la lista. También puedes utilizar la función `math.gcd()` para calcular el máximo común divisor de dos números.

## Ejemplo

```python
lcm([12, 7]) # 84
lcm([1, 3, 4, 5]) # 60
```
