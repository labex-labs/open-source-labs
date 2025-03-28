# Преобразование целого числа в римскую цифру

Напишите функцию `to_roman_numeral(num)`, которая принимает целое число `num` в диапазоне от 1 до 3999 (включительно) и возвращает его римскую цифровую запись в виде строки.

Для преобразования целого числа в его римскую цифровую запись можно использовать список соответствий, содержащий кортежи в формате (римское значение, целое число). Затем можно использовать цикл `for` для перебора значений в списке соответствий и функцию `divmod()`, чтобы обновить `num` с остатком, добавляя римскую цифровую запись к результату.

Ваша функция должна возвращать римскую цифровую запись входного целого числа.

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
