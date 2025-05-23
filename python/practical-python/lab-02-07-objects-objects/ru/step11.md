# Упражнение 2.24: Данные первого класса

В файле `portfolio.csv` мы читаем данные, организованные в столбцы, которые выглядят так:

```csv
name,shares,price
"AA",100,32.20
"IBM",50,91.10
...
```

В предыдущем коде мы использовали модуль `csv` для чтения файла, но все еще приходилось выполнять ручные преобразования типов. Например:

```python
for row in rows:
    name   = row[0]
    shares = int(row[1])
    price  = float(row[2])
```

Такой вид преобразования также можно выполнить более умело, используя некоторые базовые операции со списками.

Создайте Python-список, содержащий имена функций преобразования, которые вы бы использовали для преобразования каждого столбца в соответствующий тип:

```python
>>> types = [str, int, float]
>>>
```

Причина, по которой вы даже можете создать этот список, заключается в том, что все в Python является _первоклассным_. Поэтому, если вы хотите иметь список функций, это нормально. Элементы в списке, который вы создали, - это функции для преобразования значения `x` в заданный тип (например, `str(x)`, `int(x)`, `float(x)`).

Теперь прочитайте строку данных из вышеуказанного файла:

```python
>>> import csv
>>> f = open('portfolio.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>>
```

Как уже отмечалось, эта строка недостаточна для выполнения вычислений, потому что типы данных неправильные. Например:

```python
>>> row[1] * row[2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type'str'
>>>
```

Однако, возможно, данные можно сопоставить с типами, которые вы указали в `types`. Например:

```python
>>> types[1]
<type 'int'>
>>> row[1]
'100'
>>>
```

Попробуйте преобразовать одно из значений:

```python
>>> types[1](row[1])     # То же, что и int(row[1])
100
>>>
```

Попробуйте преобразовать другое значение:

```python
>>> types[2](row[2])     # То же, что и float(row[2])
32.2
>>>
```

Попробуйте выполнить вычисление с преобразованными значениями:

```python
>>> types[1](row[1])*types[2](row[2])
3220.0000000000005
>>>
```

Сопоставьте типы столбцов с полями и посмотрите на результат:

```python
>>> r = list(zip(types, row))
>>> r
[(<type'str'>, 'AA'), (<type 'int'>, '100'), (<type 'float'>,'32.20')]
>>>
```

Вы заметите, что это сопоставило преобразование типа с значением. Например, `int` сопоставлено со значением `'100'`.

Сопоставленный список полезен, если вы хотите выполнить преобразования для всех значений последовательно. Попробуйте это:

```python
>>> converted = []
>>> for func, val in zip(types, row):
          converted.append(func(val))
...
>>> converted
['AA', 100, 32.2]
>>> converted[1] * converted[2]
3220.0000000000005
>>>
```

Убедитесь, что понимаете, что происходит в вышеприведенном коде. В цикле переменная `func` - это одна из функций преобразования типов (например, `str`, `int` и т.д.), а переменная `val` - это одно из значений, таких как `'AA'`, `'100'`. Выражение `func(val)` преобразует значение (что-то вроде приведения типа).

Вышеприведенный код можно сократить до одной списочной генерации.

```python
>>> converted = [func(val) for func, val in zip(types, row)]
>>> converted
['AA', 100, 32.2]
>>>
```
