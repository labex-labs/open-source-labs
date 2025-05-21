# 열 중심 데이터로 메모리 최적화

전통적인 데이터 저장 방식에서는 각 레코드를 별도의 딕셔너리로 저장하는 경우가 많은데, 이를 행 중심 접근 방식이라고 합니다. 그러나 이 방법은 상당한 양의 메모리를 소비할 수 있습니다. 대안은 데이터를 열로 저장하는 것입니다. 열 중심 접근 방식에서는 각 속성에 대해 별도의 리스트를 만들고, 각 리스트는 해당 특정 속성에 대한 모든 값을 저장합니다. 이는 메모리를 절약하는 데 도움이 될 수 있습니다.

1. 먼저, 프로젝트 디렉토리에 새 Python 파일을 만들어야 합니다. 이 파일에는 열 중심 방식으로 데이터를 읽는 코드가 포함됩니다. 파일 이름을 `readrides.py`로 지정합니다. 터미널에서 다음 명령을 사용하여 이를 수행할 수 있습니다.

```bash
cd ~/project
touch readrides.py
```

`cd ~/project` 명령은 현재 디렉토리를 프로젝트 디렉토리로 변경하고, `touch readrides.py` 명령은 `readrides.py`라는 새 빈 파일을 만듭니다.

2. 다음으로, WebIDE 편집기에서 `readrides.py` 파일을 엽니다. 그런 다음 다음 Python 코드를 파일에 추가합니다. 이 코드는 CSV 파일에서 버스 운행 데이터를 읽어 각 열을 나타내는 네 개의 별도 리스트에 저장하는 `read_rides_as_columns` 함수를 정의합니다.

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

이 코드에서는 먼저 필요한 모듈 `csv`, `sys`, `tracemalloc`을 가져옵니다. `csv` 모듈은 CSV 파일을 읽는 데 사용되고, `sys`는 시스템 관련 작업에 사용될 수 있으며 (이 함수에서는 사용되지 않음), `tracemalloc`은 메모리 프로파일링에 사용됩니다. 함수 내부에서, 데이터의 서로 다른 열을 저장하기 위해 네 개의 빈 리스트를 초기화합니다. 그런 다음 파일을 열고, 헤더 행을 건너뛰고, 파일의 각 행을 반복하면서 해당 값을 적절한 리스트에 추가합니다. 마지막으로, 이 네 개의 리스트를 포함하는 딕셔너리를 반환합니다.

3. 이제 열 중심 접근 방식이 메모리를 절약할 수 있는 이유를 분석해 보겠습니다. Python 셸에서 이 작업을 수행합니다. 다음 코드를 실행합니다.

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

이 코드에서는 먼저 방금 만든 `readrides` 모듈과 `tracemalloc` 모듈을 가져옵니다. 그런 다음 행 중심 접근 방식에 대한 메모리 사용량을 추정합니다. 각 딕셔너리의 오버헤드가 240 바이트라고 가정하고, 이를 원본 파일의 행 수로 곱하여 행 중심 데이터에 대한 총 메모리 사용량을 구합니다. 열 중심 접근 방식의 경우, 64 비트 시스템에서 각 포인터가 8 바이트를 차지한다고 가정합니다. 4 개의 열과 항목당 하나의 포인터가 있으므로 열 중심 데이터에 대한 총 메모리 사용량을 계산합니다. 마지막으로, 열 중심 메모리 사용량에서 행 중심 메모리 사용량을 빼서 메모리 절약량을 계산합니다.

이 계산은 열 중심 접근 방식이 딕셔너리를 사용하는 행 중심 접근 방식에 비해 약 120MB 의 메모리를 절약해야 함을 보여줍니다.

4. `tracemalloc` 모듈로 실제 메모리 사용량을 측정하여 이를 확인해 보겠습니다. 다음 코드를 실행합니다.

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

이 코드에서는 먼저 `tracemalloc.start()`를 사용하여 메모리 추적을 시작합니다. 그런 다음 `read_rides_as_columns` 함수를 호출하여 `ctabus.csv` 파일에서 데이터를 읽습니다. 그 후, `tracemalloc.get_traced_memory()`를 사용하여 현재 및 최대 메모리 사용량을 얻습니다. 마지막으로, `tracemalloc.stop()`을 사용하여 메모리 추적을 중지합니다.

출력은 열 중심 데이터 구조의 실제 메모리 사용량을 보여줍니다. 이는 행 중심 접근 방식에 대한 이론적 추정치보다 훨씬 적어야 합니다.

상당한 메모리 절약은 수천 개의 딕셔너리 객체의 오버헤드를 제거하여 얻을 수 있습니다. Python 의 각 딕셔너리는 포함된 항목 수에 관계없이 고정된 오버헤드를 갖습니다. 열 중심 스토리지를 사용하면 수천 개의 딕셔너리 대신 몇 개의 리스트만 있으면 됩니다.
