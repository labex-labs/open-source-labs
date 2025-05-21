# 타입 힌트 추가

Python 3.5 이상 버전에서는 타입 힌트가 지원됩니다. 타입 힌트는 코드에서 변수, 함수 매개변수 및 반환 값의 예상 데이터 유형을 나타내는 방법입니다. 코드가 실행되는 방식은 변경하지 않지만 코드를 더 읽기 쉽게 만들고 코드가 실제로 실행되기 전에 특정 유형의 오류를 포착하는 데 도움이 될 수 있습니다. 이제 CSV 리더 함수에 타입 힌트를 추가해 보겠습니다.

1. `reader.py` 파일을 열고 타입 힌트를 포함하도록 업데이트합니다.

```python
# reader.py

import csv
from typing import List, Callable, Dict, Any, Type, Optional, TextIO, Iterator, TypeVar

# Define a generic type for the class parameter
T = TypeVar('T')

def csv_as_dicts(lines: Iterator[str],
                types: List[Callable[[str], Any]],
                headers: Optional[List[str]] = None) -> List[Dict[str, Any]]:
    '''
    반복 가능 항목에서 CSV 데이터를 딕셔너리 목록으로 구문 분석

    Args:
        lines: CSV 줄을 생성하는 반복 가능 항목
        types: 각 열에 대한 유형 변환 함수 목록
        headers: 선택적 열 이름 목록. None 인 경우 첫 번째 행이 헤더로 사용됨

    Returns:
        CSV 줄의 데이터가 있는 딕셔너리 목록
    '''
    records: List[Dict[str, Any]] = []
    rows = csv.reader(lines)

    if headers is None:
        # 제공된 헤더가 없으면 첫 번째 행을 헤더로 사용
        headers = next(rows)

    for row in rows:
        record = { name: func(val)
                  for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(lines: Iterator[str],
                    cls: Type[T],
                    headers: Optional[List[str]] = None) -> List[T]:
    '''
    반복 가능 항목에서 CSV 데이터를 클래스 인스턴스 목록으로 구문 분석

    Args:
        lines: CSV 줄을 생성하는 반복 가능 항목
        cls: 인스턴스를 생성할 클래스
        headers: 선택적 열 이름 목록. None 인 경우 첫 번째 행이 헤더로 사용됨

    Returns:
        CSV 줄의 데이터가 있는 클래스 인스턴스 목록
    '''
    records: List[T] = []
    rows = csv.reader(lines)

    if headers is None:
        # 헤더가 제공되지 않은 경우 첫 번째 행 건너뛰기
        next(rows)

    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records

def read_csv_as_dicts(filename: str,
                     types: List[Callable[[str], Any]],
                     headers: Optional[List[str]] = None) -> List[Dict[str, Any]]:
    '''
    선택적 유형 변환을 사용하여 CSV 데이터를 딕셔너리 목록으로 읽기

    Args:
        filename: CSV 파일 경로
        types: 각 열에 대한 유형 변환 함수 목록
        headers: 선택적 열 이름 목록. None 인 경우 첫 번째 행이 헤더로 사용됨

    Returns:
        CSV 파일의 데이터가 있는 딕셔너리 목록
    '''
    with open(filename) as file:
        return csv_as_dicts(file, types, headers)

def read_csv_as_instances(filename: str,
                         cls: Type[T],
                         headers: Optional[List[str]] = None) -> List[T]:
    '''
    CSV 데이터를 클래스 인스턴스 목록으로 읽기

    Args:
        filename: CSV 파일 경로
        cls: 인스턴스를 생성할 클래스
        headers: 선택적 열 이름 목록. None 인 경우 첫 번째 행이 헤더로 사용됨

    Returns:
        CSV 파일의 데이터가 있는 클래스 인스턴스 목록
    '''
    with open(filename) as file:
        return csv_as_instances(file, cls, headers)
```

코드에서 변경한 주요 사항을 이해해 보겠습니다.

1. `typing` 모듈에서 유형을 가져왔습니다. 이 모듈은 타입 힌트를 정의하는 데 사용할 수 있는 일련의 유형을 제공합니다. 예를 들어, `List`, `Dict` 및 `Optional`은 이 모듈의 유형입니다.
2. 클래스 유형을 나타내기 위해 제네릭 유형 변수 `T`를 추가했습니다. 제네릭 유형 변수를 사용하면 타입 안전 방식으로 다양한 유형으로 작동할 수 있는 함수를 작성할 수 있습니다.
3. 모든 함수 매개변수와 반환 값에 타입 힌트를 추가했습니다. 이를 통해 함수가 어떤 유형의 인수를 예상하고 어떤 유형의 값을 반환하는지 명확하게 알 수 있습니다.
4. `List`, `Dict` 및 `Optional`과 같은 적절한 컨테이너 유형을 사용했습니다. `List`는 목록을 나타내고, `Dict`는 딕셔너리를 나타내며, `Optional`은 매개변수가 특정 유형을 갖거나 `None`일 수 있음을 나타냅니다.
5. 유형 변환 함수에 `Callable`을 사용했습니다. `Callable`은 매개변수가 호출할 수 있는 함수임을 나타내는 데 사용됩니다.
6. `csv_as_instances`가 전달된 클래스의 인스턴스 목록을 반환한다는 것을 표현하기 위해 제네릭 `T`를 사용했습니다. 이는 IDE 및 기타 도구가 반환된 객체의 유형을 이해하는 데 도움이 됩니다.

7. 이제 모든 것이 제대로 작동하는지 확인하기 위해 간단한 테스트 파일을 만들어 보겠습니다.

```python
# test_types.py

import reader
import stock

# The functions should work exactly as before
portfolio = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("First item:", portfolio[0])

# But now we have better type checking and IDE support
stock_portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
print("\nFirst stock:", stock_portfolio[0])

# We can see that stock_portfolio is a list of Stock objects
# This helps IDEs provide better code completion
first_stock = stock_portfolio[0]
print(f"\nName: {first_stock.name}")
print(f"Shares: {first_stock.shares}")
print(f"Price: {first_stock.price}")
print(f"Value: {first_stock.shares * first_stock.price}")
```

3. 터미널에서 테스트 스크립트를 실행합니다.

```bash
python test_types.py
```

출력은 다음과 유사해야 합니다.

```
First item: {'name': 'AA', 'shares': 100, 'price': 32.2}

First stock: Stock('AA', 100, 32.2)

Name: AA
Shares: 100
Price: 32.2
Value: 3220.0
```

타입 힌트는 코드가 실행되는 방식을 변경하지 않지만 몇 가지 이점을 제공합니다.

1. 코드 완성 기능으로 더 나은 IDE 지원을 제공합니다. PyCharm 또는 VS Code 와 같은 IDE 를 사용하는 경우 타입 힌트를 사용하여 변수에 대한 올바른 메서드와 속성을 제안할 수 있습니다.
2. 예상 매개변수 및 반환 유형에 대한 더 명확한 문서를 제공합니다. 함수 정의만 봐도 어떤 유형의 인수를 예상하고 어떤 유형의 값을 반환하는지 알 수 있습니다.
3. mypy 와 같은 정적 타입 검사기를 사용하여 오류를 조기에 포착할 수 있습니다. 정적 타입 검사기는 코드를 실행하지 않고 분석하여 코드를 실행하기 전에 타입 관련 오류를 찾을 수 있습니다.
4. 코드 가독성과 유지 관리성을 향상시킵니다. 개발자 또는 다른 개발자가 나중에 코드로 돌아오면 코드가 무엇을 하는지 더 쉽게 이해할 수 있습니다.

대규모 코드베이스에서 이러한 이점은 버그를 크게 줄이고 코드를 더 쉽게 이해하고 유지 관리할 수 있습니다.

**참고:** 타입 힌트는 Python 에서 선택 사항이지만 전문적인 코드에서 점점 더 많이 사용되고 있습니다. Python 표준 라이브러리의 라이브러리와 많은 인기 있는 타사 패키지에는 이제 광범위한 타입 힌트가 포함되어 있습니다.
