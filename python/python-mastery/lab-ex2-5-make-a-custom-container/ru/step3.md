# Оптимизация памяти с использованием столбцовой организации данных

В традиционной хранении данных мы часто храним каждую запись в виде отдельного словаря, что называется строковой (row-oriented) организацией данных. Однако этот метод может потреблять значительное количество памяти. Альтернативный способ - хранить данные по столбцам. В столбцовой (column-oriented) организации данных мы создаем отдельные списки для каждого атрибута, и каждый список содержит все значения для этого конкретного атрибута. Это может помочь нам сэкономить память.

1. Сначала вам нужно создать новый файл Python в директории проекта. Этот файл будет содержать код для чтения данных в столбцовой организации. Назовите файл `readrides.py`. Вы можете использовать следующие команды в терминале для этого:

```bash
cd ~/project
touch readrides.py
```

Команда `cd ~/project` изменяет текущую директорию на директорию проекта, а команда `touch readrides.py` создает новый пустой файл с именем `readrides.py`.

2. Затем откройте файл `readrides.py` в редакторе WebIDE. Затем добавьте следующий код Python в файл. Этот код определяет функцию `read_rides_as_columns`, которая читает данные о поездках на автобусах из CSV-файла и хранит их в четырех отдельных списках, каждый из которых представляет столбец данных.

```python
# readrides.py
import csv
import sys
import tracemalloc

def read_rides_as_columns(filename):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)
```

В этом коде мы сначала импортируем необходимые модули `csv`, `sys` и `tracemalloc`. Модуль `csv` используется для чтения CSV-файлов, `sys` может быть использован для операций, связанных с системой (хотя в этой функции не используется), а `tracemalloc` используется для профилирования памяти. Внутри функции мы инициализируем четыре пустых списка для хранения разных столбцов данных. Затем мы открываем файл, пропускаем строку заголовков и проходим по каждой строке в файле, добавляя соответствующие значения в соответствующие списки. В конце мы возвращаем словарь, содержащий эти четыре списка.

3. Теперь давайте проанализируем, почему столбцовая организация данных может сэкономить память. Мы сделаем это в оболочке Python. Запустите следующий код:

```python
import readrides
import tracemalloc

# Estimate memory for row-oriented approach
nrows = 577563     # Number of rows in original file
dict_overhead = 240  # Approximate dictionary overhead in bytes
row_memory = nrows * dict_overhead
print(f"Estimated memory for row-oriented data: {row_memory} bytes ({row_memory/1024/1024:.2f} MB)")

# Estimate memory for column-oriented approach
pointer_size = 8   # Size of a pointer in bytes on 64-bit systems
column_memory = nrows * 4 * pointer_size  # 4 columns with one pointer per entry
print(f"Estimated memory for column-oriented data: {column_memory} bytes ({column_memory/1024/1024:.2f} MB)")

# Estimate savings
savings = row_memory - column_memory
print(f"Estimated memory savings: {savings} bytes ({savings/1024/1024:.2f} MB)")
```

В этом коде мы сначала импортируем модуль `readrides`, который мы только что создали, и модуль `tracemalloc`. Затем мы оцениваем использование памяти для строковой организации данных. Мы предполагаем, что каждый словарь имеет накладные расходы в 240 байт, и мы умножаем это на количество строк в исходном файле, чтобы получить общее использование памяти для строковой организации данных. Для столбцовой организации данных мы предполагаем, что на 64-битной системе каждый указатель занимает 8 байт. Поскольку у нас есть 4 столбца и один указатель на запись, мы вычисляем общее использование памяти для столбцовой организации данных. В конце мы вычисляем экономию памяти, вычитая использование памяти для столбцовой организации данных из использования памяти для строковой организации данных.

Этот расчет показывает, что столбцовая организация данных должна сэкономить около 120 МБ памяти по сравнению со строковой организацией данных с использованием словарей.

4. Давайте проверим это, измерив фактическое использование памяти с помощью модуля `tracemalloc`. Запустите следующий код:

```python
# Start tracking memory
tracemalloc.start()

# Read the data
columns = readrides.read_rides_as_columns('ctabus.csv')

# Get current and peak memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current/1024/1024:.2f} MB")
print(f"Peak memory usage: {peak/1024/1024:.2f} MB")

# Stop tracking memory
tracemalloc.stop()
```

В этом коде мы сначала начинаем отслеживать память с помощью `tracemalloc.start()`. Затем мы вызываем функцию `read_rides_as_columns` для чтения данных из файла `ctabus.csv`. После этого мы используем `tracemalloc.get_traced_memory()` для получения текущего и пикового использования памяти. В конце мы останавливаем отслеживание памяти с помощью `tracemalloc.stop()`.

Вывод показывает фактическое использование памяти вашей структуры данных с столбцовой организацией. Это должно быть значительно меньше, чем наше теоретическое предположение для строковой организации данных.

Значительная экономия памяти достигается за счет устранения накладных расходов тысяч объектов - словарей. Каждый словарь в Python имеет фиксированные накладные расходы, независимо от того, сколько элементов он содержит. Используя столбцовое хранение, нам нужно только несколько списков вместо тысяч словарей.
