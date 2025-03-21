# Числа с плавающей точкой (float)

Используйте десятичную или экспоненциальную запись для указания значения с плавающей точкой:

```python
a = 37.45
b = 4e5 # 4 x 10**5 или 400 000
c = -1.345e-10
```

Числа с плавающей точкой представлены в виде двойной точности с использованием представления процессора [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754). Это то же самое, что и тип `double` в языке программирования C.

> 17 цифр точности\
> Показатель степени от -308 до 308

Обратите внимание, что числа с плавающей точкой не точны при представлении десятичных дробей.

```python
>>> a = 2.1 + 4.2
>>> a == 6.3
False
>>> a
6.300000000000001
>>>
```

Это **не проблема Python**, а базовое оборудование с плавающей точкой на процессоре.

Общие операции:

    x + y      Сложение
    x - y      Вычитание
    x * y      Умножение
    x / y      Деление
    x // y     Целочисленное деление
    x % y      Остаток от деления
    x ** y     Возведение в степень
    abs(x)     Абсолютное значение

Это те же операторы, что и для целых чисел, за исключением битовых операторов. Дополнительные математические функции находятся в модуле `math`.

```python
import math
a = math.sqrt(x)
b = math.sin(x)
c = math.cos(x)
d = math.tan(x)
e = math.log(x)
```
