# 범용 CSV 리더 만들기

이 마지막 단계에서는 범용 함수를 만들 것입니다. 이 함수는 CSV 파일을 읽고 `from_row()` 클래스 메서드를 구현한 모든 클래스의 객체를 생성할 수 있습니다. 이는 클래스 메서드를 균일한 인터페이스로 사용하는 것의 강력함을 보여줍니다. 균일한 인터페이스는 서로 다른 클래스를 동일한 방식으로 사용할 수 있음을 의미하며, 이는 코드를 더 유연하고 관리하기 쉽게 만듭니다.

## read_portfolio() 함수 수정하기

먼저 `stock.py` 파일에서 `read_portfolio()` 함수를 업데이트합니다. 새로운 `from_row()` 클래스 메서드를 사용합니다. `stock.py` 파일을 열고 `read_portfolio()` 함수를 다음과 같이 변경합니다.

```python
def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of Stock instances
    '''
    import csv
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip header
        for row in rows:
            portfolio.append(Stock.from_row(row))
    return portfolio
```

이 함수의 새 버전은 더 간단합니다. 유형 변환의 책임을 실제로 속한 `Stock` 클래스에 부여합니다. 유형 변환은 문자열을 정수로 바꾸는 것과 같이 데이터를 한 유형에서 다른 유형으로 변경하는 것을 의미합니다. 이렇게 하면 코드를 더 체계적으로 만들고 이해하기 쉽게 만들 수 있습니다.

## 범용 CSV 리더 만들기

이제 `reader.py` 파일에서 더 범용적인 함수를 만들 것입니다. 이 함수는 CSV 데이터를 읽고 `from_row()` 클래스 메서드가 있는 모든 클래스의 인스턴스를 생성할 수 있습니다.

`reader.py` 파일을 열고 다음 함수를 추가합니다.

```python
def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances of the given class.

    Args:
        filename: Name of the CSV file
        cls: Class to instantiate (must have from_row class method)

    Returns:
        List of class instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip header
        for row in rows:
            records.append(cls.from_row(row))
    return records
```

이 함수는 파일 이름과 클래스라는 두 개의 입력을 받습니다. 그런 다음 CSV 파일의 데이터에서 생성된 해당 클래스의 인스턴스 목록을 반환합니다. 이는 `from_row()` 메서드가 있는 한 서로 다른 클래스에서 사용할 수 있으므로 매우 유용합니다.

## 범용 CSV 리더 테스트하기

범용 리더가 어떻게 작동하는지 확인하기 위해 테스트 파일을 만들어 보겠습니다. 다음 내용으로 `test_csv_reader.py`라는 파일을 만듭니다.

```python
# test_csv_reader.py
from reader import read_csv_as_instances
from stock import Stock
from decimal_stock import DStock

# Read portfolio as Stock instances
portfolio = read_csv_as_instances('portfolio.csv', Stock)
print(f"Portfolio contains {len(portfolio)} stocks")
print(f"First stock: {portfolio[0].name}, {portfolio[0].shares} shares at ${portfolio[0].price}")

# Read portfolio as DStock instances (with Decimal prices)
decimal_portfolio = read_csv_as_instances('portfolio.csv', DStock)
print(f"\nDecimal portfolio contains {len(decimal_portfolio)} stocks")
print(f"First stock: {decimal_portfolio[0].name}, {decimal_portfolio[0].shares} shares at ${decimal_portfolio[0].price}")

# Define a new class for reading the bus data
class BusRide:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

    @classmethod
    def from_row(cls, row):
        return cls(row[0], row[1], row[2], int(row[3]))

# Read some bus data (just the first 5 records for brevity)
print("\nReading bus data...")
import csv
with open('ctabus.csv') as f:
    rows = csv.reader(f)
    headers = next(rows)  # Skip header
    bus_rides = []
    for i, row in enumerate(rows):
        if i >= 5:  # Only read 5 records for the example
            break
        bus_rides.append(BusRide.from_row(row))

# Display the bus data
for ride in bus_rides:
    print(f"Route: {ride.route}, Date: {ride.date}, Type: {ride.daytype}, Rides: {ride.rides}")
```

결과를 보려면 이 파일을 실행하십시오. 터미널을 열고 다음 명령을 사용합니다.

```bash
cd ~/project
python test_csv_reader.py
```

포트폴리오 데이터가 `Stock` 및 `DStock` 인스턴스로 모두 로드되고 버스 노선 데이터가 `BusRide` 인스턴스로 로드되는 것을 보여주는 출력이 표시되어야 합니다. 이는 범용 리더가 서로 다른 클래스에서 작동함을 증명합니다.

## 이 접근 방식의 주요 이점

이 접근 방식은 몇 가지 강력한 개념을 보여줍니다.

1. **관심사 분리**: 데이터 읽기는 객체 생성과 분리됩니다. 즉, CSV 파일을 읽는 코드가 객체를 생성하는 코드와 혼합되지 않습니다. 코드를 이해하고 유지 관리하기가 더 쉬워집니다.
2. **다형성**: 동일한 코드가 동일한 인터페이스를 따르는 서로 다른 클래스에서 작동할 수 있습니다. 이 경우 클래스에 `from_row()` 메서드가 있는 한 범용 리더가 사용할 수 있습니다.
3. **유연성**: 서로 다른 클래스를 사용하여 데이터를 변환하는 방식을 쉽게 변경할 수 있습니다. 예를 들어, `Stock` 또는 `DStock`을 사용하여 포트폴리오 데이터를 다르게 처리할 수 있습니다.
4. **확장성**: 리더 코드를 변경하지 않고도 리더와 함께 작동하는 새 클래스를 추가할 수 있습니다. 이렇게 하면 코드가 미래에도 유용하게 사용될 수 있습니다.

이는 코드를 더 모듈화하고, 재사용 가능하며, 유지 관리 가능하게 만드는 Python 의 일반적인 패턴입니다.

## 클래스 메서드에 대한 최종 참고 사항

클래스 메서드는 Python 에서 대체 생성자로 자주 사용됩니다. 일반적으로 이름에 "from"이라는 단어가 포함되어 있는지 여부로 구분할 수 있습니다. 예를 들면 다음과 같습니다.

```python
# Some examples from Python's built-in types
dict.fromkeys(['a', 'b', 'c'], 0)  # Create a dict with default values
datetime.datetime.fromtimestamp(1627776000)  # Create datetime from timestamp
int.from_bytes(b'\x00\x01', byteorder='big')  # Create int from bytes
```

이 규칙을 따르면 코드를 더 읽기 쉽고 Python 의 내장 라이브러리와 일관되게 만들 수 있습니다. 이는 다른 개발자가 코드를 더 쉽게 이해하는 데 도움이 됩니다.
