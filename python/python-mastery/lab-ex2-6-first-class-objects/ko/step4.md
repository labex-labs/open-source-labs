# 열 중심 데이터 저장

지금까지 CSV 데이터를 행 딕셔너리 목록으로 저장해 왔습니다. 즉, CSV 파일의 각 행은 딕셔너리로 표시되며, 여기서 키는 열 헤더이고 값은 해당 행의 해당 데이터입니다. 그러나 대규모 데이터 세트를 처리할 때는 이 방법이 비효율적일 수 있습니다. 열 중심 형식으로 데이터를 저장하는 것이 더 나은 선택일 수 있습니다. 열 중심 접근 방식에서는 각 열의 데이터가 별도의 목록에 저장됩니다. 이로 인해 유사한 데이터 유형이 함께 그룹화되므로 메모리 사용량이 크게 줄어들 수 있으며, 열별 데이터 집계와 같은 특정 작업의 성능도 향상될 수 있습니다.

## 열 중심 데이터 리더 생성

이제 열 중심 형식으로 CSV 데이터를 읽는 데 도움이 되는 새 파일을 만들 것입니다. 프로젝트 디렉토리에 `colreader.py`라는 새 파일을 만들고 다음 코드를 입력합니다.

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

이 코드는 두 가지 중요한 작업을 수행합니다.

1. `DataCollection` 클래스를 정의합니다. 이 클래스는 데이터를 열에 저장하지만, 행 딕셔너리 목록인 것처럼 데이터에 액세스할 수 있도록 합니다. 이는 데이터로 작업하는 익숙한 방법을 제공하므로 유용합니다.
2. `read_csv_as_columns` 함수를 정의합니다. 이 함수는 파일에서 CSV 데이터를 읽어 열 중심 구조로 저장합니다. 또한 제공된 유형에 따라 CSV 파일의 각 필드를 변환합니다.

## 열 중심 리더 테스트

CTA 버스 데이터를 사용하여 열 중심 리더를 테스트해 보겠습니다. 먼저, Python 인터프리터를 엽니다. 터미널에서 다음 명령을 실행하여 이 작업을 수행할 수 있습니다.

```bash
python3
```

Python 인터프리터가 열리면 다음 코드를 실행합니다.

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

출력은 다음과 같아야 합니다.

```
Number of rows: 577563
First 3 rows:
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
{'route': '6', 'date': '01/01/2001', 'daytype': 'U', 'rides': 6048}
Current memory usage: 38.67 MB
Peak memory usage: 103.42 MB
```

이제 이전의 행 중심 접근 방식과 비교해 보겠습니다. 동일한 Python 인터프리터에서 다음 코드를 실행합니다.

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

출력은 다음과 같아야 합니다.

```
Current memory usage (row-oriented): 170.23 MB
Peak memory usage (row-oriented): 190.05 MB
```

보시다시피, 열 중심 접근 방식은 메모리를 훨씬 적게 사용합니다!

이전과 마찬가지로 데이터를 분석할 수 있는지 테스트해 보겠습니다. 다음 코드를 실행합니다.

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

출력은 다음과 같아야 합니다.

```
Number of unique routes: 181
Top 5 routes by total rides:
Route 9: 158,545,826 rides
Route 49: 129,872,910 rides
Route 77: 120,086,065 rides
Route 79: 109,348,708 rides
Route 4: 91,405,538 rides
```

마지막으로, 다음 명령을 실행하여 Python 인터프리터를 종료합니다.

```python
exit()
```

열 중심 접근 방식은 메모리를 절약할 뿐만 아니라 이전과 동일한 분석을 수행할 수 있도록 해줍니다. 이는 서로 다른 데이터 저장 전략이 성능에 큰 영향을 미칠 수 있으며, 데이터를 처리하기 위한 동일한 인터페이스를 제공하는 방법을 보여줍니다.
