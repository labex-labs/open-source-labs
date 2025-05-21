# map() 함수 사용하기

Python 에서 고차 함수는 다른 함수를 인수로 받거나 함수를 결과로 반환할 수 있는 함수입니다. Python 의 `map()` 함수는 고차 함수의 훌륭한 예입니다. 이는 주어진 함수를 리스트나 튜플과 같은 반복 가능한 객체의 각 항목에 적용할 수 있는 강력한 도구입니다. 각 항목에 함수를 적용한 후 결과의 이터레이터 (iterator) 를 반환합니다. 이러한 기능으로 인해 `map()`은 CSV 파일의 행과 같이 데이터 시퀀스를 처리하는 데 완벽합니다.

`map()` 함수의 기본 구문은 다음과 같습니다.

```python
map(function, iterable, ...)
```

여기서 `function`은 `iterable`의 각 항목에 대해 수행하려는 작업입니다. `iterable`은 리스트 또는 튜플과 같은 항목의 시퀀스입니다.

간단한 예제를 살펴보겠습니다. 숫자 목록이 있고 해당 목록의 각 숫자를 제곱하고 싶다고 가정해 보겠습니다. `map()` 함수를 사용하여 이를 수행할 수 있습니다. 방법은 다음과 같습니다.

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
```

이 예제에서는 먼저 `numbers`라는 리스트를 정의합니다. 그런 다음 `map()` 함수를 사용합니다. `lambda` 함수 `lambda x: x * x`는 `numbers` 리스트의 각 항목에 대해 수행하려는 작업입니다. `map()` 함수는 이 `lambda` 함수를 리스트의 각 숫자에 적용합니다. `map()`은 이터레이터를 반환하므로 `list()` 함수를 사용하여 리스트로 변환합니다. 마지막으로, 원래 숫자의 제곱 값을 포함하는 `squared` 리스트를 출력합니다.

이제 `map()` 함수를 사용하여 `convert_csv()` 함수를 수정하는 방법을 살펴보겠습니다. 이전에는 `for` 루프를 사용하여 CSV 데이터의 행을 반복했습니다. 이제 해당 `for` 루프를 `map()` 함수로 대체합니다.

```python
def convert_csv(lines, conversion_func, *, headers=None):
    '''
    Convert lines of CSV data using the provided conversion function
    '''
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)

    # Use map to apply conversion_func to each row
    records = list(map(lambda row: conversion_func(headers, row), rows))
    return records
```

이 업데이트된 버전의 `convert_csv()` 함수는 이전 버전과 정확히 동일한 작업을 수행하지만 `for` 루프 대신 `map()` 함수를 사용합니다. `map()` 내부의 `lambda` 함수는 CSV 데이터에서 각 행을 가져와 헤더와 함께 `conversion_func`을 적용합니다.

이 업데이트된 함수가 제대로 작동하는지 테스트해 보겠습니다. 먼저 터미널을 열고 프로젝트 디렉토리로 이동합니다. 그런 다음 `reader.py` 파일로 Python 대화형 셸을 시작합니다.

```bash
cd ~/project
python3 -i reader.py
```

Python 셸에 들어가면 다음 코드를 실행하여 업데이트된 `convert_csv()` 함수를 테스트합니다.

```python
# Test the updated convert_csv function
with open('portfolio.csv') as f:
    result = convert_csv(f, make_dict)
print(result[0])  # Should print the first dictionary

# Test that csv_as_dicts still works
with open('portfolio.csv') as f:
    portfolio = csv_as_dicts(f, [str, int, float])
print(portfolio[0])  # Should print the first dictionary with converted types
```

이 코드를 실행한 후 다음과 유사한 출력이 표시되어야 합니다.

```
{'name': 'AA', 'shares': '100', 'price': '32.20'}
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

이 출력은 `map()` 함수를 사용하는 업데이트된 `convert_csv()` 함수가 올바르게 작동하고, 이에 의존하는 함수도 예상대로 계속 작동함을 보여줍니다.

`map()` 함수를 사용하면 다음과 같은 몇 가지 장점이 있습니다.

1. `for` 루프보다 더 간결할 수 있습니다. `for` 루프에 대해 여러 줄의 코드를 작성하는 대신 `map()`을 사용하여 동일한 결과를 한 줄로 얻을 수 있습니다.
2. 시퀀스의 각 항목을 변환하려는 의도를 명확하게 전달합니다. `map()`을 보면 즉시 함수를 반복 가능한 객체의 각 항목에 적용하고 있음을 알 수 있습니다.
3. 이터레이터를 반환하므로 메모리 효율성이 더 높을 수 있습니다. 이터레이터는 값을 즉시 생성하므로 모든 결과를 한 번에 메모리에 저장하지 않습니다. 이 예제에서는 `map()`에서 반환된 이터레이터를 리스트로 변환했지만, 경우에 따라 메모리를 절약하기 위해 이터레이터를 직접 사용할 수 있습니다.

Python 셸을 종료하려면 `exit()`를 입력하거나 Ctrl+D 를 누르세요.
