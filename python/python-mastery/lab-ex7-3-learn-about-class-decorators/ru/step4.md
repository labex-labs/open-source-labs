# Добавление функциональности преобразования строк

В программировании часто бывает полезно создавать экземпляры класса из строк данных, особенно при работе с данными из таких источников, как файлы CSV. В этом разделе мы добавим возможность создавать экземпляры класса `Structure` из строк данных. Мы сделаем это, реализовав классовый метод `from_row` в классе `Structure`.

1. Сначала откройте файл `structure.py` в вашем редакторе. Здесь мы внесем изменения в код.

2. Далее мы модифицируем функцию `validate_attributes`. Эта функция является декоратором класса, который извлекает экземпляры `Validator` и автоматически создает списки `_fields` и `_types`. Мы обновим ее, чтобы она также собирала информацию о типах.

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

В этой обновленной функции мы собираем атрибут `expected_type` из каждого валидатора и сохраняем его в классовой переменной `_types`. Это будет полезно позже, когда мы будем преобразовывать данные из строк в правильные типы.

3. Теперь мы добавим классовый метод `from_row` в класс `Structure`. Этот метод позволит нам создавать экземпляр класса из строки данных, которая может быть списком или кортежем.

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

4. После внесения этих изменений сохраните файл `structure.py`. Это гарантирует, что изменения в вашем коде будут сохранены.

5. Давайте протестируем наш метод `from_row`, чтобы убедиться, что он работает должным образом. Мы создадим простой тест с использованием класса `Stock`. Выполните следующую команду в терминале:

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock.from_row(['GOOG', '100', '490.1']); print(s); print(f'Cost: {s.cost}')"
```

Вы должны увидеть вывод, похожий на этот:

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

Обратите внимание, что строковые значения '100' и '490.1' были автоматически преобразованы в правильные типы (целое число и число с плавающей запятой). Это показывает, что наш метод `from_row` работает правильно.

6. Наконец, давайте попробуем прочитать данные из файла CSV с помощью нашего модуля `reader.py`. Выполните следующую команду в терминале:

```bash
cd ~/project
python3 -c "from stock import Stock; import reader; portfolio = reader.read_csv_as_instances('portfolio.csv', Stock); print(portfolio); print(f'Total value: {sum(s.cost for s in portfolio)}')"
```

Вы должны увидеть вывод, показывающий акции из файла CSV:

```
[Stock('GOOG', 100, 490.1), Stock('AAPL', 50, 545.75), Stock('MSFT', 200, 30.47)]
Total value: 82391.5
```

Метод `from_row` позволяет нам легко преобразовывать данные CSV в экземпляры класса `Stock`. В сочетании с функцией `read_csv_as_instances` мы получаем мощный способ загрузки и работы со структурированными данными.
