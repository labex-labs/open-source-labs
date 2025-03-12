# Добавление функциональности преобразования строк

В программировании часто бывает полезно создавать экземпляры класса из строк данных, особенно когда работаешь с данными из источников, таких как CSV-файлы. В этом разделе мы добавим возможность создавать экземпляры класса `Structure` из строк данных. Мы сделаем это, реализовав метод класса `from_row` в классе `Structure`.

1. Сначала вам нужно открыть файл `structure.py`. Именно здесь мы внесем изменения в код. Используйте следующую команду в терминале:

```bash
code ~/project/structure.py
```

2. Затем мы изменим функцию `validate_attributes`. Эта функция является декоратором класса, который извлекает экземпляры `Validator` и автоматически создает списки `_fields` и `_types`. Мы обновим ее так, чтобы она также собирала информацию о типах.

```python
def validate_attributes(cls):
    """
    Class decorator that extracts Validator instances
    and builds the _fields and _types lists automatically
    """
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

    # Set _fields based on validator names
    cls._fields = [val.name for val in validators]

    # Set _types based on validator expected_types
    cls._types = [getattr(val, 'expected_type', lambda x: x) for val in validators]

    # Create initialization method
    cls.create_init()

    return cls
```

В этой обновленной функции мы собираем атрибут `expected_type` из каждого валидатора и сохраняем его в переменной класса `_types`. Это будет полезно позже, когда мы будем преобразовывать данные из строк в правильные типы.

3. Теперь мы добавим метод класса `from_row` в класс `Structure`. Этот метод позволит нам создавать экземпляр класса из строки данных, которая может быть списком или кортежем.

```python
@classmethod
def from_row(cls, row):
    """
    Create an instance from a data row (list or tuple)
    """
    rowdata = [func(val) for func, val in zip(cls._types, row)]
    return cls(*rowdata)
```

Вот как работает этот метод:

- Он принимает строку данных, которая может быть в виде списка или кортежа.
- Он преобразует каждое значение в строке в ожидаемый тип, используя соответствующую функцию из списка `_types`.
- Затем он создает и возвращает новый экземпляр класса, используя преобразованные значения.

4. После внесения этих изменений сохраните файл `structure.py`. Это гарантирует, что ваши изменения в коде будут сохранены.

5. Давайте протестируем метод `from_row`, чтобы убедиться, что он работает как ожидается. Мы создадим простой тест, используя класс `Stock`. Запустите следующую команду в терминале:

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock.from_row(['GOOG', '100', '490.1']); print(s); print(f'Cost: {s.cost}')"
```

Вы должны увидеть вывод, похожий на следующий:

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

Обратите внимание, что строковые значения '100' и '490.1' были автоматически преобразованы в правильные типы (целое число и число с плавающей точкой). Это показывает, что наш метод `from_row` работает правильно.

6. Наконец, давайте попробуем прочитать данные из CSV-файла, используя модуль `reader.py`. Запустите следующую команду в терминале:

```bash
cd ~/project
python3 -c "from stock import Stock; import reader; portfolio = reader.read_csv_as_instances('portfolio.csv', Stock); print(portfolio); print(f'Total value: {sum(s.cost for s in portfolio)}')"
```

Вы должны увидеть вывод, показывающий акции из CSV-файла:

```
[Stock('GOOG', 100, 490.1), Stock('AAPL', 50, 545.75), Stock('MSFT', 200, 30.47)]
Total value: 73444.0
```

Метод `from_row` позволяет нам легко преобразовывать данные из CSV в экземпляры класса `Stock`. В сочетании с функцией `read_csv_as_instances` у нас есть мощный способ загружать и работать со структурированными данными.
