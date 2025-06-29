# 다양한 데이터 구조 비교

Python 에서 데이터 구조는 관련 데이터를 구성하고 저장하는 데 사용됩니다. 이는 구조화된 방식으로 다양한 유형의 정보를 담는 컨테이너와 같습니다. 이 단계에서는 다양한 데이터 구조를 비교하고 메모리를 얼마나 사용하는지 살펴보겠습니다.

`/home/labex/project` 디렉토리에 `compare_structures.py`라는 새 파일을 만들어 보겠습니다. 이 파일에는 CSV 파일에서 데이터를 읽어 다양한 데이터 구조에 저장하는 코드가 포함됩니다.

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

스크립트를 실행하여 비교 결과를 확인합니다.

```bash
python3 /home/labex/project/compare_structures.py
```

출력에는 각 데이터 구조의 메모리 사용량과 메모리 효율성이 가장 높은 것부터 가장 낮은 것까지의 순위가 표시됩니다.

## 다양한 데이터 구조 이해

1. **튜플 (Tuples)**:
   - 튜플은 가볍고 불변 (immutable) 시퀀스입니다. 즉, 튜플을 생성한 후에는 요소를 변경할 수 없습니다.
   - `record[0]`, `record[1]` 등과 같이 숫자 인덱스로 튜플의 요소에 액세스합니다.
   - 단순한 구조를 가지고 있기 때문에 메모리 효율성이 매우 높습니다.
   - 그러나 각 요소의 인덱스를 기억해야 하므로 가독성이 떨어질 수 있습니다.

2. **딕셔너리 (Dictionaries)**:
   - 딕셔너리는 키 - 값 쌍을 사용하므로 이름으로 요소에 액세스할 수 있습니다.
   - `record['route']`, `record['date']` 등과 같이 더 읽기 쉽습니다.
   - 키 - 값 쌍을 저장하는 데 사용되는 해시 테이블 오버헤드로 인해 메모리 사용량이 더 많습니다.
   - 필드를 쉽게 추가하거나 제거할 수 있으므로 유연합니다.

3. **네임드 튜플 (Named Tuples)**:
   - 네임드 튜플은 튜플의 효율성과 이름으로 요소에 액세스하는 기능을 결합합니다.
   - `record.route`, `record.date` 등과 같이 점 표기법을 사용하여 요소에 액세스할 수 있습니다.
   - 일반 튜플과 마찬가지로 불변입니다.
   - 딕셔너리보다 메모리 효율성이 높습니다.

4. **일반 클래스 (Regular Classes)**:
   - 일반 클래스는 객체 지향 방식을 따르며 이름이 지정된 속성을 갖습니다.
   - `record.route`, `record.date` 등과 같이 점 표기법을 사용하여 속성에 액세스할 수 있습니다.
   - 동작을 정의하기 위해 일반 클래스에 메서드를 추가할 수 있습니다.
   - 각 인스턴스에 속성을 저장하기 위한 인스턴스 딕셔너리가 있으므로 더 많은 메모리를 사용합니다.

5. **\_\_slots\_\_가 있는 클래스 (Classes with \_\_slots\_\_)**:
   - `__slots__`가 있는 클래스는 메모리 최적화된 클래스입니다. 인스턴스 딕셔너리를 사용하지 않아 메모리를 절약합니다.
   - `record.route`, `record.date` 등과 같이 속성에 대한 이름 지정된 액세스를 계속 제공합니다.
   - 객체가 생성된 후 새 속성을 추가하는 것을 제한합니다.
   - 일반 클래스보다 메모리 효율성이 높습니다.

## 각 접근 방식을 사용해야 하는 경우

- **튜플 (Tuples)**: 메모리가 중요한 요소이고 데이터에 대한 간단한 인덱싱된 액세스만 필요한 경우 튜플을 사용합니다.
- **딕셔너리 (Dictionaries)**: 데이터의 필드가 다를 수 있는 경우와 같이 유연성이 필요한 경우 딕셔너리를 사용합니다.
- **네임드 튜플 (Named Tuples)**: 가독성과 메모리 효율성이 모두 필요한 경우 네임드 튜플을 사용합니다.
- **일반 클래스 (Regular Classes)**: 데이터에 동작 (메서드) 을 추가해야 하는 경우 일반 클래스를 사용합니다.
- **\_\_slots\_\_가 있는 클래스 (Classes with \_\_slots\_\_)**: 동작과 최대 메모리 효율성이 필요한 경우 `__slots__`가 있는 클래스를 사용합니다.

요구 사항에 맞는 올바른 데이터 구조를 선택하면 특히 대용량 데이터 세트로 작업할 때 Python 프로그램의 성능과 메모리 사용량을 크게 향상시킬 수 있습니다.
