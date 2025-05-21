# 사용자 정의 컨테이너 클래스 만들기

데이터 처리에서 열 중심 접근 방식은 메모리 절약에 매우 효과적입니다. 그러나 기존 코드가 데이터를 딕셔너리 목록 형태로 예상하는 경우 문제가 발생할 수 있습니다. 이 문제를 해결하기 위해 사용자 정의 컨테이너 클래스를 만들 것입니다. 이 클래스는 행 중심 인터페이스를 제공하며, 이는 코드에서 딕셔너리 목록처럼 보이고 작동한다는 것을 의미합니다. 그러나 내부적으로는 열 중심 형식으로 데이터를 저장하여 메모리를 절약하는 데 도움이 됩니다.

1. 먼저, WebIDE 편집기에서 `readrides.py` 파일을 엽니다. 이 파일에 새 클래스를 추가할 것입니다. 이 클래스는 사용자 정의 컨테이너의 기반이 됩니다.

```python
# Add this to readrides.py
from collections.abc import Sequence

class RideData(Sequence):
    def __init__(self):
        # Each value is a list with all of the values (a column)
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        # All lists assumed to have the same length
        return len(self.routes)

    def __getitem__(self, index):
        return {'route': self.routes[index],
                'date': self.dates[index],
                'daytype': self.daytypes[index],
                'rides': self.numrides[index]}

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])
```

이 코드에서는 `Sequence`에서 상속받는 `RideData`라는 클래스를 정의합니다. `__init__` 메서드는 각 열을 나타내는 네 개의 빈 리스트를 초기화합니다. `__len__` 메서드는 컨테이너의 길이를 반환하며, 이는 `routes` 리스트의 길이와 같습니다. `__getitem__` 메서드를 사용하면 인덱스로 특정 레코드에 액세스하여 딕셔너리로 반환할 수 있습니다. `append` 메서드는 각 열 리스트에 값을 추가하여 컨테이너에 새 레코드를 추가합니다.

2. 이제 버스 운행 데이터를 사용자 정의 컨테이너로 읽는 함수가 필요합니다. 다음 함수를 `readrides.py` 파일에 추가합니다.

```python
# Add this to readrides.py
def read_rides_as_dicts(filename):
    '''
    Read the bus ride data as a list of dicts, but use our custom container
    '''
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides
            }
            records.append(record)
    return records
```

이 함수는 `RideData` 클래스의 인스턴스를 생성하고 CSV 파일의 데이터로 채웁니다. 파일에서 각 행을 읽고, 관련 정보를 추출하고, 각 레코드에 대한 딕셔너리를 생성한 다음, 이를 `RideData` 컨테이너에 추가합니다. 핵심은 딕셔너리 목록과 동일한 인터페이스를 유지하지만 내부적으로는 열로 데이터를 저장한다는 것입니다.

3. Python 셸에서 사용자 정의 컨테이너를 테스트해 보겠습니다. 이를 통해 예상대로 작동하는지 확인할 수 있습니다.

```python
import readrides

# Read the data using our custom container
rows = readrides.read_rides_as_dicts('ctabus.csv')

# Check the type of the returned object
type(rows)  # Should be readrides.RideData

# Check the length
len(rows)   # Should be 577563

# Access individual records
rows[0]     # Should return a dictionary for the first record
rows[1]     # Should return a dictionary for the second record
rows[2]     # Should return a dictionary for the third record
```

사용자 정의 컨테이너는 `Sequence` 인터페이스를 성공적으로 구현하므로 리스트처럼 동작합니다. `len()` 함수를 사용하여 컨테이너의 레코드 수를 얻을 수 있으며, 인덱싱을 사용하여 개별 레코드에 액세스할 수 있습니다. 각 레코드는 내부적으로 데이터가 열로 저장되어 있음에도 불구하고 딕셔너리처럼 보입니다. 이는 딕셔너리 목록을 예상하는 기존 코드가 수정 없이 사용자 정의 컨테이너로 계속 작동하기 때문에 매우 좋습니다.

4. 마지막으로, 사용자 정의 컨테이너의 메모리 사용량을 측정해 보겠습니다. 이를 통해 딕셔너리 목록과 비교하여 얼마나 많은 메모리를 절약하는지 확인할 수 있습니다.

```python
import tracemalloc

tracemalloc.start()
rows = readrides.read_rides_as_dicts('ctabus.csv')
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current/1024/1024:.2f} MB")
print(f"Peak memory usage: {peak/1024/1024:.2f} MB")
tracemalloc.stop()
```

이 코드를 실행하면 메모리 사용량이 열 중심 접근 방식과 유사하다는 것을 알 수 있으며, 이는 딕셔너리 목록이 사용하는 것보다 훨씬 적습니다. 이는 메모리 효율성 측면에서 사용자 정의 컨테이너의 장점을 보여줍니다.
