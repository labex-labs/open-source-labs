# Desafío de Conversión de Número Entero a Número Romano

## Problema

Escribe una función `to_roman_numeral(num)` que tome un número entero `num` entre 1 y 3999 (inclusive) y devuelva su representación en números romanos como una cadena.

Para convertir un número entero a su representación en números romanos, puedes utilizar una lista de búsqueda que contenga tuplas en la forma de (valor romano, número entero). Luego, puedes utilizar un bucle `for` para iterar sobre los valores de la lista de búsqueda y usar `divmod()` para actualizar `num` con el residuo, agregando la representación en números romanos al resultado.

Tu función debe devolver la representación en números romanos del número entero de entrada.

## Ejemplo

```python
to_roman_numeral(3) # 'III'
to_roman_numeral(11) # 'XI'
to_roman_numeral(1998) # 'MCMXCVIII'
```
