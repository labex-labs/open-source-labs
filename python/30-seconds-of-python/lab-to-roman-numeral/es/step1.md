# Número Entero a Número Romano

Escribe una función `to_roman_numeral(num)` que tome un número entero `num` entre 1 y 3999 (inclusive) y devuelva su representación en números romanos como una cadena.

Para convertir un número entero a su representación en números romanos, puedes usar una lista de búsqueda que contenga tuplas en la forma de (valor romano, número entero). Luego, puedes usar un bucle `for` para iterar sobre los valores de la lista de búsqueda y usar `divmod()` para actualizar `num` con el residuo, agregando la representación en números romanos al resultado.

Tu función debe devolver la representación en números romanos del número entero de entrada.

```python
def to_roman_numeral(num):
  lookup = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I'),
  ]
  res = ''
  for (n, roman) in lookup:
    (d, num) = divmod(num, n)
    res += roman * d
  return res
```

```python
to_roman_numeral(3) # 'III'
to_roman_numeral(11) # 'XI'
to_roman_numeral(1998) # 'MCMXCVIII'
```
