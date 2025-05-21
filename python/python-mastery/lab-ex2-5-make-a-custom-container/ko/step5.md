# 슬라이싱을 위한 사용자 정의 컨테이너 향상

사용자 정의 컨테이너는 개별 레코드에 액세스하는 데 매우 유용합니다. 그러나 슬라이싱과 관련하여 문제가 있습니다. 컨테이너의 슬라이스를 가져오려고 하면 결과가 일반적으로 예상하는 것과 다릅니다.

이러한 현상이 발생하는 이유를 이해해 보겠습니다. Python 에서 슬라이싱은 시퀀스의 일부를 추출하는 데 사용되는 일반적인 연산입니다. 그러나 사용자 정의 컨테이너의 경우 Python 은 슬라이스된 데이터만 사용하여 새 `RideData` 객체를 만드는 방법을 알지 못합니다. 대신, 슬라이스의 각 인덱스에 대해 `__getitem__`을 호출한 결과를 포함하는 리스트를 생성합니다.

1. Python 셸에서 슬라이싱을 테스트해 보겠습니다.

```python
import readrides

rows = readrides.read_rides_as_dicts('ctabus.csv')
r = rows[0:10]  # Take a slice of the first 10 records
type(r)  # This will likely be a list, not a RideData object
print(r)  # This might look like a list of numbers, not dictionaries
```

이 코드에서는 먼저 `readrides` 모듈을 가져옵니다. 그런 다음 `ctabus.csv` 파일에서 데이터를 읽어 `rows` 변수에 저장합니다. 처음 10 개의 레코드의 슬라이스를 가져와 결과의 유형을 확인하려고 하면 `RideData` 객체 대신 리스트임을 알 수 있습니다. 결과를 출력하면 딕셔너리 대신 숫자 목록과 같이 예상치 못한 내용이 표시될 수 있습니다.

2. 슬라이싱을 제대로 처리하도록 `RideData` 클래스를 수정해 보겠습니다. `readrides.py`를 열고 `__getitem__` 메서드를 업데이트합니다.

```python
def __getitem__(self, index):
    if isinstance(index, slice):
        # Handle slice
        result = RideData()
        result.routes = self.routes[index]
        result.dates = self.dates[index]
        result.daytypes = self.daytypes[index]
        result.numrides = self.numrides[index]
        return result
    else:
        # Handle single index
        return {'route': self.routes[index],
                'date': self.dates[index],
                'daytype': self.daytypes[index],
                'rides': self.numrides[index]}
```

이 업데이트된 `__getitem__` 메서드에서는 먼저 `index`가 슬라이스인지 확인합니다. 슬라이스인 경우 `result`라는 새 `RideData` 객체를 만듭니다. 그런 다음 이 새 객체를 원래 데이터 열 (`routes`, `dates`, `daytypes`, `numrides`) 의 슬라이스로 채웁니다. 이렇게 하면 사용자 정의 컨테이너를 슬라이싱할 때 리스트 대신 다른 `RideData` 객체를 얻을 수 있습니다. `index`가 슬라이스가 아닌 경우 (즉, 단일 인덱스인 경우) 관련 레코드를 포함하는 딕셔너리를 반환합니다.

3. 향상된 슬라이싱 기능을 테스트해 보겠습니다.

```python
import readrides

rows = readrides.read_rides_as_dicts('ctabus.csv')
r = rows[0:10]  # Take a slice of the first 10 records
type(r)  # Should now be readrides.RideData
len(r)   # Should be 10
r[0]     # Should be the same as rows[0]
r[1]     # Should be the same as rows[1]
```

`__getitem__` 메서드를 업데이트한 후 슬라이싱을 다시 테스트할 수 있습니다. 처음 10 개의 레코드의 슬라이스를 가져오면 결과의 유형이 이제 `readrides.RideData`여야 합니다. 슬라이스의 길이는 10 이어야 하며, 슬라이스의 개별 요소에 액세스하면 원래 컨테이너의 해당 요소에 액세스하는 것과 동일한 결과를 얻어야 합니다.

4. 다양한 슬라이스 패턴으로도 테스트할 수 있습니다.

```python
# Get every other record from the first 20
r2 = rows[0:20:2]
len(r2)  # Should be 10

# Get the last 10 records
r3 = rows[-10:]
len(r3)  # Should be 10
```

여기서는 다양한 슬라이스 패턴을 테스트하고 있습니다. 첫 번째 슬라이스 `rows[0:20:2]`는 처음 20 개의 레코드에서 두 번째 레코드마다 가져오며, 결과 슬라이스의 길이는 10 이어야 합니다. 두 번째 슬라이스 `rows[-10:]`는 마지막 10 개의 레코드를 가져오며, 그 길이도 10 이어야 합니다.

슬라이싱을 제대로 구현함으로써 사용자 정의 컨테이너는 열 중심 스토리지를 유지하면서 표준 Python 리스트처럼 더욱 동작합니다.

내장 Python 컨테이너를 모방하지만 내부 표현이 다른 사용자 정의 컨테이너 클래스를 만드는 이 접근 방식은 코드가 사용자에게 제공하는 인터페이스를 변경하지 않고 메모리 사용량을 최적화하는 강력한 기술입니다.
