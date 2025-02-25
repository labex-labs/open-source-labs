# Cambio de Bit

## Problema

Dado un número binario, necesitamos cambiar uno de sus bits de 0 a 1 para maximizar la secuencia más larga de 1s. Por ejemplo, si tenemos el número binario `000011110000`, podemos cambiar el cuarto bit de 0 a 1 para obtener `000111110000`, que tiene una secuencia de cinco 1s. Nuestro objetivo es escribir una función de Python que tome un número binario y devuelva la longitud de la secuencia más larga de 1s después de cambiar un bit.

## Requisitos

Los requisitos para nuestra función de Python son los siguientes:

- La entrada debe ser un número entero en base 2.
- Podemos suponer que la entrada es un número de 32 bits.
- No tenemos que validar la longitud de la entrada.
- La salida debe ser un número entero.
- No podemos suponer que las entradas son válidas.
- Podemos suponer que estamos usando un número positivo ya que Python no tiene un operador >>>.
- Podemos suponer que esto cabe en memoria.

## Uso de ejemplo

A continuación se presentan algunos ejemplos de cómo debe comportarse nuestra función de Python:

- `None` -> Excepción
- `11111111111111111111111111111111` -> 32
- `00000000000000000000000000000000` -> 1
- `00001111110111011111001111110000` -> 10
