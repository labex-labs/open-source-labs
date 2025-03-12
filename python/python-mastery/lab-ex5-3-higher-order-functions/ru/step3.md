# Рефакторинг существующих функций

Теперь мы создали функцию высшего порядка с именем `convert_csv()`. Функции высшего порядка - это функции, которые могут принимать другие функции в качестве аргументов или возвращать функции в качестве результатов. Это мощная концепция в Python, которая помогает нам писать более модульный и переиспользуемый код. В этом разделе мы используем эту функцию высшего порядка для рефакторинга исходных функций `csv_as_dicts()` и `csv_as_instances()`. Рефакторинг - это процесс переструктурирования существующего кода без изменения его внешнего поведения, с целью улучшения его внутренней структуры, например, устранения дублирования кода.

Начнем с открытия файла `reader.py` в WebIDE. Мы обновим функции следующим образом:

1. Сначала заменим функцию `csv_as_dicts()`. Эта функция используется для преобразования строк данных в формате CSV в список словарей. Вот новый код:

```python
def csv_as_dicts(lines, types, *, headers=None):
    '''
    Convert lines of CSV data into a list of dictionaries
    '''
    def dict_converter(headers, row):
        return {name: func(val) for name, func, val in zip(headers, types, row)}

    return convert_csv(lines, dict_converter, headers=headers)
```

В этом коде мы определяем внутреннюю функцию `dict_converter`, которая принимает `headers` и `row` в качестве аргументов. Она использует генератор словаря для создания словаря, где ключами являются имена заголовков, а значениями - результаты применения соответствующих функций преобразования типов к значениям в строке. Затем мы вызываем функцию `convert_csv()` с функцией `dict_converter` в качестве аргумента.

2. Далее заменим функцию `csv_as_instances()`. Эта функция используется для преобразования строк данных в формате CSV в список экземпляров заданного класса. Вот новый код:

```python
def csv_as_instances(lines, cls, *, headers=None):
    '''
    Convert lines of CSV data into a list of instances
    '''
    def instance_converter(headers, row):
        return cls.from_row(row)

    return convert_csv(lines, instance_converter, headers=headers)
```

В этом коде мы определяем внутреннюю функцию `instance_converter`, которая принимает `headers` и `row` в качестве аргументов. Она вызывает метод класса `from_row` заданного класса `cls` для создания экземпляра из строки. Затем мы вызываем функцию `convert_csv()` с функцией `instance_converter` в качестве аргумента.

После рефакторинга этих функций нам нужно протестировать их, чтобы убедиться, что они по-прежнему работают как ожидается. Для этого мы выполним следующие команды в оболочке Python:

```bash
cd ~/project
python3 -i reader.py
```

Команда `cd ~/project` изменяет текущую рабочую директорию на директорию `project`. Команда `python3 -i reader.py` запускает файл `reader.py` в интерактивном режиме, что означает, что мы можем продолжать выполнять код Python после завершения выполнения файла.

Как только оболочка Python откроется, мы выполним следующий код для тестирования рефакторингованных функций:

```python
# Define a simple Stock class for testing
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        return cls(row[0], int(row[1]), float(row[2]))

    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'

# Test csv_as_dicts
with open('portfolio.csv') as f:
    portfolio_dicts = csv_as_dicts(f, [str, int, float])
print("First dictionary:", portfolio_dicts[0])

# Test csv_as_instances
with open('portfolio.csv') as f:
    portfolio_instances = csv_as_instances(f, Stock)
print("First instance:", portfolio_instances[0])
```

В этом коде мы сначала определяем простой класс `Stock` для тестирования. Метод `__init__` инициализирует атрибуты экземпляра `Stock`. Метод класса `from_row` создает экземпляр `Stock` из строки данных в формате CSV. Метод `__repr__` предоставляет строковое представление экземпляра `Stock`.

Затем мы тестируем функцию `csv_as_dicts()`, открывая файл `portfolio.csv` и передавая его в функцию вместе со списком функций преобразования типов. Мы выводим первый словарь в результирующем списке.

Наконец, мы тестируем функцию `csv_as_instances()`, открывая файл `portfolio.csv` и передавая его в функцию вместе с классом `Stock`. Мы выводим первый экземпляр в результирующем списке.

Если все работает правильно, вы должны увидеть вывод, похожий на следующий:

```
First dictionary: {'name': 'AA', 'shares': 100, 'price': 32.2}
First instance: Stock(AA, 100, 32.2)
```

Этот вывод показывает, что наши рефакторингованные функции работают правильно. Мы успешно устранили дублирование кода, сохранив при этом ту же функциональность.

Чтобы выйти из оболочки Python, вы можете ввести `exit()` или нажать Ctrl+D.
