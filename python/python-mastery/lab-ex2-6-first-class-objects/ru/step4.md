# Столбцовое хранение данных

До сих пор мы хранили данные из CSV-файлов в виде списка словарей, представляющих строки. Это означает, что каждая строка в CSV-файле представлена в виде словаря, где ключами являются заголовки столбцов, а значениями - соответствующие данные в этой строке. Однако при работе с большими наборами данных этот метод может быть неэффективным. Хранение данных в столбцовом формате может быть более подходящим выбором. В столбцовом подходе данные каждого столбца хранятся в отдельном списке. Это может значительно уменьшить использование памяти, так как данные одного типа группируются вместе, и также может повысить производительность для определенных операций, таких как агрегирование данных по столбцам.

## Создание считывателя столбцовых данных

Теперь мы создадим новый файл, который поможет нам считывать данные из CSV-файла в столбцовом формате. Создайте новый файл с именем `colreader.py` в директории проекта со следующим кодом:

```python
import csv

class DataCollection:
    def __init__(self, headers, columns):
        """
        Initialize a column-oriented data collection.

        Parameters:
        headers (list): Column header names
        columns (dict): Dictionary mapping header names to column data lists
        """
        self.headers = headers
        self.columns = columns
        self._length = len(columns[headers[0]]) if headers else 0

    def __len__(self):
        """Return the number of rows in the collection."""
        return self._length

    def __getitem__(self, index):
        """
        Get a row by index, presented as a dictionary.

        Parameters:
        index (int): Row index

        Returns:
        dict: Dictionary representing the row at the given index
        """
        if isinstance(index, int):
            if index < 0 or index >= self._length:
                raise IndexError("Index out of range")

            return {header: self.columns[header][index] for header in self.headers}
        else:
            raise TypeError("Index must be an integer")

def read_csv_as_columns(filename, types):
    """
    Read a CSV file into a column-oriented data structure, converting each field
    according to the types provided.

    Parameters:
    filename (str): Name of the CSV file to read
    types (list): List of type conversion functions for each column

    Returns:
    DataCollection: Column-oriented data collection representing the CSV data
    """
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)  # Get the column headers

        # Initialize columns
        columns = {header: [] for header in headers}

        # Read data into columns
        for row in rows:
            # Convert values according to the specified types
            converted_values = [func(val) for func, val in zip(types, row)]

            # Add each value to its corresponding column
            for header, value in zip(headers, converted_values):
                columns[header].append(value)

    return DataCollection(headers, columns)
```

Этот код выполняет две важные задачи:

1. Он определяет класс `DataCollection`. Этот класс хранит данные в столбцах, но позволяет нам обращаться к данным, как если бы они были списком словарей, представляющих строки. Это полезно, так как предоставляет знакомый способ работы с данными.
2. Он определяет функцию `read_csv_as_columns`. Эта функция считывает данные из CSV-файла и хранит их в столбцовой структуре. Она также преобразует каждое поле в CSV-файле в соответствии с типами, которые мы предоставляем.

## Тестирование столбцового считывателя

Протестируем наш столбцовый считыватель на данных о автобусах CTA. Сначала откройте интерпретатор Python. Вы можете сделать это, запустив следующую команду в терминале:

```bash
python3
```

После открытия интерпретатора Python запустите следующий код:

```python
import colreader
import tracemalloc
from sys import intern

# Start memory tracking
tracemalloc.start()

# Read data into column-oriented structure with string interning
data = colreader.read_csv_as_columns('ctabus.csv', [intern, intern, intern, int])

# Check that we can access the data like a list of dictionaries
print(f"Number of rows: {len(data)}")
print("First 3 rows:")
for i in range(3):
    print(data[i])

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
```

Вывод должен выглядеть так:

```
Number of rows: 577563
First 3 rows:
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
{'route': '6', 'date': '01/01/2001', 'daytype': 'U', 'rides': 6048}
Current memory usage: 38.67 MB
Peak memory usage: 103.42 MB
```

Теперь сравним это с нашим предыдущим строковым подходом. Запустите следующий код в том же интерпретаторе Python:

```python
import reader
import tracemalloc
from sys import intern

# Reset memory tracking
tracemalloc.reset_peak()

# Read data into row-oriented structure with string interning
rows = reader.read_csv_as_dicts('ctabus.csv', [intern, intern, intern, int])

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage (row-oriented): {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage (row-oriented): {peak / 1024 / 1024:.2f} MB")
```

Вывод должен быть похожим на следующий:

```
Current memory usage (row-oriented): 170.23 MB
Peak memory usage (row-oriented): 190.05 MB
```

Как вы можете видеть, столбцовый подход использует значительно меньше памяти!

Давайте также проверим, что мы все еще можем анализировать данные, как и раньше. Запустите следующий код:

```python
# Find all unique routes in the column-oriented data
routes = {row['route'] for row in data}
print(f"Number of unique routes: {len(routes)}")

# Count rides per route (first 5)
from collections import defaultdict
route_rides = defaultdict(int)
for row in data:
    route_rides[row['route']] += row['rides']

# Show the top 5 routes by total rides
top_routes = sorted(route_rides.items(), key=lambda x: x[1], reverse=True)[:5]
print("Top 5 routes by total rides:")
for route, rides in top_routes:
    print(f"Route {route}: {rides:,} rides")
```

Вывод должен быть таким:

```
Number of unique routes: 181
Top 5 routes by total rides:
Route 9: 158,545,826 rides
Route 49: 129,872,910 rides
Route 77: 120,086,065 rides
Route 79: 109,348,708 rides
Route 4: 91,405,538 rides
```

Наконец, выйдите из интерпретатора Python, запустив следующую команду:

```python
exit()
```

Мы видим, что столбцовый подход не только экономит память, но и позволяет нам выполнять те же анализы, что и раньше. Это показывает, как разные стратегии хранения данных могут иметь значительное влияние на производительность, при этом предоставляя тот же интерфейс для работы с данными.
