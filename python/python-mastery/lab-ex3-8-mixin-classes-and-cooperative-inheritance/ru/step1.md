# Понимание проблемы с форматированием столбцов

На этом шаге мы рассмотрим ограничение в нашей текущей реализации форматирования таблиц. Мы также изучим некоторые возможные решения этой проблемы.

Сначала давайте поймем, что мы собираемся делать. Мы откроем редактор VSCode и посмотрим на файл `tableformat.py` в каталоге проекта. Этот файл важен, потому что он содержит код, который позволяет нам форматировать табличные данные различными способами, например, в текстовом формате, CSV или HTML.

Чтобы открыть файл, мы будем использовать следующие команды в терминале. Команда `cd` изменяет каталог на каталог проекта, а команда `code` открывает файл `tableformat.py` в VSCode.

```bash
cd ~/project
touch tableformat.py
```

Когда вы откроете файл, вы заметите, что определено несколько классов. Эти классы играют разные роли в форматировании табличных данных.

- `TableFormatter`: Это абстрактный базовый класс (abstract base class). Он имеет методы, которые используются для форматирования заголовков и строк таблицы. Думайте об этом как о чертеже для других классов форматирования.
- `TextTableFormatter`: Этот класс используется для вывода таблицы в формате обычного текста (plain text format).
- `CSVTableFormatter`: Он отвечает за форматирование табличных данных в формате CSV (Comma-Separated Values).
- `HTMLTableFormatter`: Этот класс форматирует табличные данные в формате HTML.

В файле также есть функция `print_table()`. Эта функция использует классы форматирования, которые мы только что упомянули, для отображения табличных данных.

Теперь давайте посмотрим, как работают эти классы. В вашем каталоге `/home/labex/project` создайте новый файл с именем `step1_test1.py`, используя ваш редактор или команду `touch`. Добавьте в него следующий код Python:

```python
# step1_test1.py
from tableformat import print_table, TextTableFormatter, portfolio

formatter = TextTableFormatter()
print("--- Running Step 1 Test 1 ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("-----------------------------")
```

Сохраните файл и запустите его из терминала:

```bash
python3 step1_test1.py
```

После запуска скрипта вы должны увидеть вывод, подобный этому:

```
--- Running Step 1 Test 1 ---
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
-----------------------------
```

Теперь давайте найдем проблему. Обратите внимание, что значения в столбце `price` отформатированы непоследовательно. Некоторые значения имеют один десятичный знак, например, 32.2, а другие - два десятичных знака, например, 51.23. В финансовых данных мы обычно хотим, чтобы форматирование было последовательным.

Вот как мы хотим, чтобы выглядел вывод:

```
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

Один из способов исправить это - изменить функцию `print_table()`, чтобы она принимала спецификации формата (format specifications). Давайте посмотрим, как это работает _без_ фактического изменения `tableformat.py`. Создайте новый файл с именем `step1_test2.py` со следующим содержимым. Этот скрипт переопределяет функцию `print_table` локально для демонстрационных целей.

```python
# step1_test2.py
from tableformat import TextTableFormatter

# Re-define Stock and portfolio locally for this example
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

portfolio = [
    Stock('AA', 100, 32.20), Stock('IBM', 50, 91.10), Stock('CAT', 150, 83.44),
    Stock('MSFT', 200, 51.23), Stock('GE', 95, 40.37), Stock('MSFT', 50, 65.10),
    Stock('IBM', 100, 70.44)
]

# Define a modified print_table locally
def print_table_modified(records, fields, formats, formatter):
    formatter.headings(fields)
    for r in records:
        # Apply formats to the original attribute values
        rowdata = [(fmt % getattr(r, fieldname))
                   for fieldname, fmt in zip(fields, formats)]
        # Pass the already formatted strings to the formatter's row method
        formatter.row(rowdata)

print("--- Running Step 1 Test 2 ---")
formatter = TextTableFormatter()
# Note: TextTableFormatter.row expects strings already formatted for width.
# This example might not align perfectly yet, but demonstrates passing formats.
print_table_modified(portfolio,
                     ['name', 'shares', 'price'],
                     ['%10s', '%10d', '%10.2f'], # Using widths
                     formatter)
print("-----------------------------")

```

Запустите этот скрипт:

```bash
python3 step1_test2.py
```

Этот подход демонстрирует передачу форматов, но изменение `print_table` имеет недостаток: изменение интерфейса функции может сломать существующий код, который использует исходную версию.

Другой подход - создать пользовательский форматтер (custom formatter) путем создания подкласса (subclassing). Мы можем создать новый класс, который наследуется от `TextTableFormatter`, и переопределить метод `row()`. Создайте файл `step1_test3.py`:

```python
# step1_test3.py
from tableformat import TextTableFormatter, print_table, portfolio

class PortfolioFormatter(TextTableFormatter):
    def row(self, rowdata):
        # Example: Add a prefix to demonstrate overriding
        # Note: The original lab description's formatting example had data type issues
        # because print_table sends strings to this method. This is a simpler demo.
        print("> ", end="") # Add a simple prefix to the line start
        super().row(rowdata) # Call the parent method

print("--- Running Step 1 Test 3 ---")
formatter = PortfolioFormatter()
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("-----------------------------")
```

Запустите скрипт:

```bash
python3 step1_test3.py
```

Это решение работает для демонстрации создания подклассов, но создание нового класса для каждого варианта форматирования неудобно. Кроме того, вы привязаны к базовому классу, от которого наследуетесь (здесь, `TextTableFormatter`).

На следующем шаге мы рассмотрим более элегантное решение с использованием классов-примесей (mixin classes).
