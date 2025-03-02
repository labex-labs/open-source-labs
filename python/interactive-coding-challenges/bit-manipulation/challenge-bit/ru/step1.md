# Операции с битами

## Задача

Реализуйте следующие общие операции с битами в Python:

- `get_bit`: Принимает число и индекс, возвращает значение бита по заданному индексу.
- `set_bit`: Принимает число и индекс, устанавливает значение бита по заданному индексу в 1.
- `clear_bit`: Принимает число и индекс, устанавливает значение бита по заданному индексу в 0.
- `clear_bits_msb_to_index`: Принимает число и индекс, устанавливает все биты от старшего значащего бита до заданного индекса в 0.
- `clear_bits_index_to_lsb`: Принимает число и индекс, устанавливает все биты от заданного индекса до младшего значащего бита в 0.
- `update_bit`: Принимает число, индекс и значение, обновляет значение бита по заданному индексу до заданного значения.

## Требования

Реализация должна соответствовать следующим требованиям:

- Входные данные могут быть недействительными, и реализация должна优雅но обрабатывать такие случаи.
- Реализация должна соответствовать требованиям к памяти.

## Примеры использования

Вот несколько примеров использования реализованных функций:

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
