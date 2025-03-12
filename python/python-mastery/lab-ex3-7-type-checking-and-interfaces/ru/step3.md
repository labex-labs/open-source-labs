# Создание классов - шаблонов алгоритмов

На этом этапе мы будем использовать абстрактные базовые классы для реализации шаблонного метода (template method pattern). Цель - уменьшить дублирование кода в функциональности парсинга CSV - файлов. Дублирование кода делает его сложнее в поддержке и обновлении. Используя шаблонный метод, мы можем создать общую структуру для кода парсинга CSV и позволить подклассам обрабатывать конкретные детали.

## Понимание шаблонного метода

Шаблонный метод - это поведенческий паттерн проектирования. Он похож на чертеж алгоритма. В методе он определяет общую структуру или "скелет" алгоритма. Однако он не полностью реализует все шаги. Вместо этого он откладывает некоторые шаги на подклассы. Это означает, что подклассы могут переопределить определенные части алгоритма, не меняя его общую структуру.

В нашем случае, если вы посмотрите на файл `reader.py`, вы заметите, что функции `read_csv_as_dicts()` и `read_csv_as_instances()` имеют много схожего кода. Основное различие между ними - это то, как они создают записи из строк в CSV - файле. Используя шаблонный метод, мы можем избежать многократной записи одного и того же кода.

## Добавление базового класса CSVParser

Начнем с добавления абстрактного базового класса для парсинга CSV. Откройте файл `reader.py`. Мы добавим абстрактный базовый класс `CSVParser` сразу в начало файла, сразу после инструкций импорта.

```python
# reader.py
import csv
from abc import ABC, abstractmethod

class CSVParser(ABC):
    def parse(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = self.make_record(headers, row)
                records.append(record)
        return records

    @abstractmethod
    def make_record(self, headers, row):
        pass
```

Класс `CSVParser` служит шаблоном для парсинга CSV. Метод `parse` содержит общие шаги для чтения CSV - файла, такие как открытие файла, получение заголовков и итерация по строкам. Конкретная логика создания записи из строки абстрагирована в метод `make_record()`. Поскольку это абстрактный метод, любой класс, наследующийся от `CSVParser`, должен реализовать этот метод.

## Реализация конкретных классов парсеров

Теперь, когда у нас есть базовый класс, нам нужно создать конкретные классы парсеров. Эти классы будут реализовывать конкретную логику создания записей.

```python
class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types = types

    def make_record(self, headers, row):
        return { name: func(val) for name, func, val in zip(headers, self.types, row) }

class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls

    def make_record(self, headers, row):
        return self.cls.from_row(row)
```

Класс `DictCSVParser` используется для создания записей в виде словарей. Он принимает список типов в конструкторе. Метод `make_record` использует эти типы для преобразования значений в строке и создания словаря.

Класс `InstanceCSVParser` используется для создания записей в виде экземпляров класса. Он принимает класс в конструкторе. Метод `make_record` вызывает метод `from_row` этого класса для создания экземпляра из строки.

## Рефакторинг исходных функций

Теперь давайте выполним рефакторинг исходных функций `read_csv_as_dicts()` и `read_csv_as_instances()` для использования этих новых классов.

```python
def read_csv_as_dicts(filename, types):
    '''
    Read a CSV file into a list of dictionaries with appropriate type conversion.
    '''
    parser = DictCSVParser(types)
    return parser.parse(filename)

def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances of a class.
    '''
    parser = InstanceCSVParser(cls)
    return parser.parse(filename)
```

Эти рефакторингнутые функции имеют тот же интерфейс, что и исходные. Но внутри они используют новые классы парсеров, которые мы только что создали. Таким образом, мы разделили общую логику парсинга CSV от конкретной логики создания записей.

## Тестирование вашей реализации

Давайте проверим, работает ли наш рефакторингнутый код правильно. Создайте файл с именем `test_reader.py` и добавьте в него следующий код.

```python
import reader
import stock

# Test the refactored read_csv_as_instances function
portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
print("First stock:", portfolio[0])

# Test the refactored read_csv_as_dicts function
portfolio_dicts = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("First stock as dict:", portfolio_dicts[0])

# Test direct use of a parser
parser = reader.DictCSVParser([str, int, float])
portfolio_dicts2 = parser.parse('portfolio.csv')
print("First stock from direct parser:", portfolio_dicts2[0])
```

Чтобы запустить тест, откройте терминал и выполните следующую команду:

```bash
python test_reader.py
```

Вы должны увидеть вывод, похожий на следующий:

```
First stock: Stock('AA', 100, 32.2)
First stock as dict: {'name': 'AA', 'shares': 100, 'price': 32.2}
First stock from direct parser: {'name': 'AA', 'shares': 100, 'price': 32.2}
```

Если вы видите такой вывод, это означает, что ваш рефакторингнутый код работает правильно. И исходные функции, и прямой вызов парсеров дают ожидаемые результаты.
