# Создание удобного API для примесей

Примеси (mixins) мощны, но непосредственное использование множественного наследования (multiple inheritance) может показаться сложным. На этом шаге мы улучшим функцию `create_formatter()`, чтобы скрыть эту сложность, предоставив пользователям более простой API.

Сначала убедитесь, что `tableformat.py` открыт в вашем редакторе:

```bash
cd ~/project
touch tableformat.py
```

Найдите существующую функцию `create_formatter()`:

```python
# Existing function in tableformat.py
def create_formatter(name):
    """
    Create an appropriate formatter based on the name.
    """
    if name == 'text':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {name}')
```

Замените _все существующее_ определение функции `create_formatter()` улучшенной версией ниже. Эта новая версия принимает необязательные аргументы для форматов столбцов и преобразования заголовков в верхний регистр.

```python
# Replace the old create_formatter with this in tableformat.py

def create_formatter(name, column_formats=None, upper_headers=False):
    """
    Create a formatter with optional enhancements.

    Parameters:
    name : str
        Name of the formatter ('text', 'csv', 'html')
    column_formats : list, optional
        List of format strings for column formatting.
        Note: Relies on ColumnFormatMixin existing above this function.
    upper_headers : bool, optional
        Whether to convert headers to uppercase.
        Note: Relies on UpperHeadersMixin existing above this function.
    """
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError(f'Unknown format {name}')

    # Build the inheritance list dynamically
    bases = []
    if column_formats:
        bases.append(ColumnFormatMixin)
    if upper_headers:
        bases.append(UpperHeadersMixin)
    bases.append(formatter_cls) # Base formatter class comes last

    # Create the custom class dynamically
    # Need to ensure ColumnFormatMixin and UpperHeadersMixin are defined before this point
    class CustomFormatter(*bases):
        # Set formats if ColumnFormatMixin is used
        if column_formats:
            formats = column_formats

    return CustomFormatter() # Return an instance of the dynamically created class
```

_Самокоррекция: Динамически создайте кортеж классов для наследования вместо нескольких ветвей if/elif._

Эта улучшенная функция сначала определяет базовый класс форматтера (`TextTableFormatter`, `CSVTableFormatter` и т. д.). Затем, на основе необязательных аргументов `column_formats` и `upper_headers`, она динамически создает новый класс (`CustomFormatter`), который наследуется от необходимых примесей и базового класса форматтера. Наконец, она возвращает экземпляр этого пользовательского форматтера (custom formatter).

**Не забудьте сохранить изменения в `tableformat.py`.**

Теперь давайте протестируем нашу улучшенную функцию. **Убедитесь, что вы сохранили обновленную функцию `create_formatter` в `tableformat.py`.**

Сначала протестируйте форматирование столбцов. Создайте `step3_test1.py`:

```python
# step3_test1.py
from tableformat import create_formatter, portfolio, print_table

# Using the same formats as before, subject to type issues.
# Use formats compatible with strings if '%d', '%.2f' cause errors.
formatter = create_formatter('text', column_formats=['%10s', '%10s', '%10.2f'])

print("--- Running Step 3 Test 1 (create_formatter with column_formats) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("--------------------------------------------------------------------")
```

Запустите скрипт:

```bash
python3 step3_test1.py
```

Вы должны увидеть таблицу с отформатированными столбцами (опять же, с учетом обработки типов формата цены):

```
--- Running Step 3 Test 1 (create_formatter with column_formats) ---
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.10
       IBM        100      70.44
--------------------------------------------------------------------
```

Далее протестируйте заголовки в верхнем регистре. Создайте `step3_test2.py`:

```python
# step3_test2.py
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', upper_headers=True)

print("--- Running Step 3 Test 2 (create_formatter with upper_headers) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("-------------------------------------------------------------------")
```

Запустите скрипт:

```bash
python3 step3_test2.py
```

Вы должны увидеть таблицу с заголовками в верхнем регистре:

```
--- Running Step 3 Test 2 (create_formatter with upper_headers) ---
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
-------------------------------------------------------------------
```

Наконец, объедините оба варианта. Создайте `step3_test3.py`:

```python
# step3_test3.py
from tableformat import create_formatter, portfolio, print_table

# Using the same formats as before
formatter = create_formatter('text', column_formats=['%10s', '%10s', '%10.2f'], upper_headers=True)

print("--- Running Step 3 Test 3 (create_formatter with both options) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("------------------------------------------------------------------")
```

Это должно отобразить таблицу как с отформатированными столбцами, так и с заголовками в верхнем регистре:

```
--- Running Step 3 Test 3 (create_formatter with both options) ---
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.10
       IBM        100      70.44
------------------------------------------------------------------
```

Улучшенная функция также работает с другими типами форматтеров. Например, попробуйте ее с CSV-форматтером. Создайте `step3_test4.py`:

```python
# step3_test4.py
from tableformat import create_formatter, portfolio, print_table

# For CSV, ensure formats produce valid CSV fields.
# Adding quotes around the string name field.
formatter = create_formatter('csv', column_formats=['"%s"', '%d', '%.2f'], upper_headers=True)

print("--- Running Step 3 Test 4 (create_formatter with CSV) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("---------------------------------------------------------")
```

Запустите скрипт:

```bash
python3 step3_test4.py
```

Это должно создать заголовки в верхнем регистре и отформатированные столбцы в формате CSV (опять же, потенциальная проблема с типом для форматирования `%d`/`%.2f` для строк, переданных из `print_table`):

```
--- Running Step 3 Test 4 (create_formatter with CSV) ---
NAME,SHARES,PRICE
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
---------------------------------------------------------
```

Улучшив функцию `create_formatter()`, мы создали удобный API. Теперь пользователи могут легко применять функциональность примесей, не нуждаясь в управлении структурой множественного наследования самостоятельно.
