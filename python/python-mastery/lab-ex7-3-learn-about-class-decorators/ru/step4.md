# Преобразование строки

Одной из отсутствующих функций класса `Structure` является метод `from_row()`, который позволяет ему работать с более ранним кодом чтения CSV. Исправим это. Добавьте в класс `Structure` переменную класса `_types` и следующий метод класса:

```python
# structure.py

class Structure:
    _types = ()
 ...
    @classmethod
    def from_row(cls, row):
        rowdata = [ func(val) for func, val in zip(cls._types, row) ]
        return cls(*rowdata)
 ...
```

Измените декоратор `@validate_attributes` так, чтобы он проверял различные валидаторы на наличие атрибута `expected_type` и использовал его для заполнения переменной `_types` выше.

После этого вы должны быть в состоянии делать следующее:

```python
>>> s = Stock.from_row(['GOOG', '100', '490.1'])
>>> s
Stock('GOOG', 100, 490.1)
>>> import reader
>>> port = reader.read_csv_as_instances('portfolio.csv', Stock)
>>>
```
