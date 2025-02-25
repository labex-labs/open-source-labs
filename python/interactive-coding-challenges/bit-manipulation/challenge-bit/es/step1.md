# Operaciones de manipulación de bits

## Problema

Implemente las siguientes operaciones comunes de manipulación de bits en Python:

- `get_bit`: Dado un número y un índice, devuelva el valor del bit en el índice dado.
- `set_bit`: Dado un número y un índice, establezca el valor del bit en el índice dado en 1.
- `clear_bit`: Dado un número y un índice, establezca el valor del bit en el índice dado en 0.
- `clear_bits_msb_to_index`: Dado un número y un índice, establezca todos los bits desde el bit más significativo hasta el índice dado en 0.
- `clear_bits_index_to_lsb`: Dado un número y un índice, establezca todos los bits desde el índice dado hasta el bit menos significativo en 0.
- `update_bit`: Dado un número, un índice y un valor, actualice el valor del bit en el índice dado al valor dado.

## Requisitos

La implementación debe cumplir con los siguientes requisitos:

- Las entradas pueden no ser válidas y la implementación debe manejar estos casos adecuadamente.
- La implementación debe ajustarse a la memoria.

## Uso de ejemplo

A continuación, se presentan algunos ejemplos de cómo usar las funciones implementadas:

- `get_bit`:
  ```
  number   = 0b10001110
  index = 3
  expected = True
  ```
- `set_bit`:
  ```
  number   = 0b10001110
  index = 4
  expected = 0b10011110
  ```
- `clear_bit`:
  ```
  number   = 0b10001110
  index = 3
  expected = 0b10000110
  ```
- `clear_bits_msb_to_index`:
  ```
  number   = 0b10001110
  index = 3
  expected = 0b00000110
  ```
- `clear_bits_index_to_lsb`:
  ```
  number   = 0b10001110
  index = 3
  expected = 0b10000000
  ```
- `update_bit`:

  ```
  number   = 0b10001110
  index = 3
  value = 1
  expected = 0b10001110

  number   = 0b10001110
  index = 3
  value = 0
  expected = 0b10000110

  number   = 0b10001110
  index = 0
  value = 1
  expected = 0b10001111
  ```
