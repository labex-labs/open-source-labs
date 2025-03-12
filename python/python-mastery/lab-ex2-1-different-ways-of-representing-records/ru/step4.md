# Сравнение различных структур данных

В Python структуры данных используются для организации и хранения связанных данных. Они похожи на контейнеры, которые хранят различные типы информации в структурированном виде. На этом этапе мы сравним различные структуры данных и посмотрим, сколько памяти они используют.

Создадим новый файл с именем `compare_structures.py` в каталоге `/home/labex/project`. Этот файл будет содержать код для чтения данных из CSV-файла и их хранения в различных структурах данных.

```python
# compare_structures.py
import csv
import tracemalloc
from collections import namedtuple

# Define a named tuple for rides data
RideRecord = namedtuple('RideRecord', ['route', 'date', 'daytype', 'rides'])

# A named tuple is a lightweight class that allows you to access its fields by name.
# It's like a tuple, but with named attributes.

# Define a class with __slots__ for memory optimization
class SlottedRideRecord:
    __slots__ = ['route', 'date', 'daytype', 'rides']

    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

# A class with __slots__ is a memory - optimized class.
# It avoids using an instance dictionary, which saves memory.

# Define a regular class for rides data
class RegularRideRecord:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

# A regular class is an object - oriented way to represent data.
# It has named attributes and can have methods.

# Function to read data as tuples
def read_as_tuples(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # Skip headers
        for row in rows:
            record = (row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

# This function reads data from a CSV file and stores it as tuples.
# Tuples are immutable sequences, and you access their elements by numeric index.

# Function to read data as dictionaries
def read_as_dicts(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # Get headers
        for row in rows:
            record = {
                'route': row[0],
                'date': row[1],
                'daytype': row[2],
                'rides': int(row[3])
            }
            records.append(record)
    return records

# This function reads data from a CSV file and stores it as dictionaries.
# Dictionaries use key - value pairs, so you can access elements by their names.

# Function to read data as named tuples
def read_as_named_tuples(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # Skip headers
        for row in rows:
            record = RideRecord(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

# This function reads data from a CSV file and stores it as named tuples.
# Named tuples combine the efficiency of tuples with the readability of named access.

# Function to read data as regular class instances
def read_as_regular_classes(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # Skip headers
        for row in rows:
            record = RegularRideRecord(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

# This function reads data from a CSV file and stores it as instances of a regular class.
# Regular classes allow you to add methods to your data.

# Function to read data as slotted class instances
def read_as_slotted_classes(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # Skip headers
        for row in rows:
            record = SlottedRideRecord(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

# This function reads data from a CSV file and stores it as instances of a slotted class.
# Slotted classes are memory - optimized and still provide named access.

# Function to measure memory usage
def measure_memory(func, filename):
    tracemalloc.start()

    records = func(filename)

    current, peak = tracemalloc.get_traced_memory()

    # Demonstrate how to use each data structure
    first_record = records[0]
    if func.__name__ == 'read_as_tuples':
        route, date, daytype, rides = first_record
    elif func.__name__ == 'read_as_dicts':
        route = first_record['route']
        date = first_record['date']
        daytype = first_record['daytype']
        rides = first_record['rides']
    else:  # named tuples and classes
        route = first_record.route
        date = first_record.date
        daytype = first_record.daytype
        rides = first_record.rides

    print(f"Structure type: {func.__name__}")
    print(f"Record count: {len(records)}")
    print(f"Example access: Route={route}, Date={date}, Rides={rides}")
    print(f"Current memory: {current/1024/1024:.2f} MB")
    print(f"Peak memory: {peak/1024/1024:.2f} MB")
    print("-" * 50)

    tracemalloc.stop()

    return current

if __name__ == "__main__":
    filename = '/home/labex/project/ctabus.csv'

    # Run all memory tests
    print("Memory usage comparison for different data structures:\n")

    results = []
    for reader_func in [
        read_as_tuples,
        read_as_dicts,
        read_as_named_tuples,
        read_as_regular_classes,
        read_as_slotted_classes
    ]:
        memory = measure_memory(reader_func, filename)
        results.append((reader_func.__name__, memory))

    # Sort by memory usage (lowest first)
    results.sort(key=lambda x: x[1])

    print("\nRanking by memory efficiency (most efficient first):")
    for i, (name, memory) in enumerate(results, 1):
        print(f"{i}. {name}: {memory/1024/1024:.2f} MB")
```

Запустите скрипт, чтобы увидеть результаты сравнения:

```bash
python3 /home/labex/project/compare_structures.py
```

Вывод показывает использование памяти для каждой структуры данных, а также рейтинг от самой экономичной по памяти до наименее экономичной.

## Понимание различных структур данных

1. **Кортежи (Tuples)**:

   - Кортежи - это легковесные и неизменяемые последовательности. Это означает, что после создания кортежа вы не можете изменить его элементы.
   - Вы получаете доступ к элементам кортежа по их числовому индексу, например, `record[0]`, `record[1]` и т.д.
   - Они очень экономичны по памяти, так как имеют простую структуру.
   - Однако они могут быть менее читаемыми, так как вам нужно помнить индекс каждого элемента.

2. **Словари (Dictionaries)**:

   - Словари используют пары ключ - значение, что позволяет получать доступ к элементам по их именам.
   - Они более читаемые, например, вы можете использовать `record['route']`, `record['date']` и т.д.
   - Они имеют более высокое использование памяти из - за накладных расходов хеш - таблицы, используемой для хранения пар ключ - значение.
   - Они гибкие, так как вы можете легко добавлять или удалять поля.

3. **Именнованные кортежи (Named Tuples)**:

   - Именнованные кортежи сочетают в себе эффективность кортежей и возможность доступа к элементам по имени.
   - Вы можете получать доступ к элементам с использованием точечной нотации, например, `record.route`, `record.date` и т.д.
   - Они неизменяемы, как и обычные кортежи.
   - Они более экономичны по памяти, чем словари.

4. **Обычные классы (Regular Classes)**:

   - Обычные классы следуют объектно - ориентированному подходу и имеют именованные атрибуты.
   - Вы можете получать доступ к атрибутам с использованием точечной нотации, например, `record.route`, `record.date` и т.д.
   - Вы можете добавлять методы в обычный класс, чтобы определить поведение.
   - Они используют больше памяти, так как каждый экземпляр имеет словарь экземпляра для хранения своих атрибутов.

5. **Классы с `__slots__`**:
   - Классы с `__slots__` - это классы, оптимизированные по памяти. Они не используют словарь экземпляра, что экономит память.
   - Они по - прежнему обеспечивают именованный доступ к атрибутам, например, `record.route`, `record.date` и т.д.
   - Они ограничивают добавление новых атрибутов после создания объекта.
   - Они более экономичны по памяти, чем обычные классы.

## Когда использовать каждый подход

- **Кортежи**: Используйте кортежи, когда память является критическим фактором и вам нужен только простой доступ к данным по индексу.
- **Словари**: Используйте словари, когда вам нужна гибкость, например, когда поля в ваших данных могут различаться.
- **Именнованные кортежи**: Используйте именнованные кортежи, когда вам нужна как читаемость, так и экономия памяти.
- **Обычные классы**: Используйте обычные классы, когда вам нужно добавить поведение (методы) к вашим данным.
- **Классы с `__slots__`**: Используйте классы с `__slots__`, когда вам нужно поведение и максимальная экономия памяти.

Выбрав правильную структуру данных для своих нужд, вы можете значительно повысить производительность и уменьшить использование памяти ваших Python - программ, особенно при работе с большими наборами данных.
