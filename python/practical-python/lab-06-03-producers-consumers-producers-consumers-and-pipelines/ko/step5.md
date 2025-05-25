# 연습 6.10: 더 많은 파이프라인 구성 요소 만들기

전체 아이디어를 더 큰 파이프라인으로 확장해 보겠습니다. 별도의 파일 `ticker.py`에서 위에서 했던 것처럼 CSV 파일을 읽는 함수를 생성하는 것으로 시작합니다.

```python
# ticker.py

from follow import follow
import csv

def parse_stock_data(lines):
    rows = csv.reader(lines)
    return rows

if __name__ == '__main__':
    lines = follow('stocklog.csv')
    rows = parse_stock_data(lines)
    for row in rows:
        print(row)
```

특정 열을 선택하는 새 함수를 작성합니다.

    # ticker.py
    ...
    def select_columns(rows, indices):
        for row in rows:
            yield [row[index] for index in indices]
    ...
    def parse_stock_data(lines):
        rows = csv.reader(lines)
        rows = select_columns(rows, [0, 1, 4])
        return rows

프로그램을 다시 실행합니다. 다음과 같이 좁혀진 출력을 볼 수 있습니다.

    ['GOOG', '1503.06', '2.81']
    ['AAPL', '253.31', '2.81']
    ['GOOG', '1503.07', '2.82']
    ['AAPL', '253.32', '2.82']
    ['GOOG', '1503.08', '2.83']
    ...

데이터 유형을 변환하고 딕셔너리를 구축하는 제너레이터 함수를 작성합니다. 예를 들어:

```python
# ticker.py
...

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))
...
def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows
...
```

프로그램을 다시 실행합니다. 이제 다음과 같은 딕셔너리 스트림을 볼 수 있습니다.

    {'name': 'GOOG', 'price': 1503.4, 'change': 3.15}
    {'name': 'AAPL', 'price': 253.65, 'change': 3.15}
    {'name': 'GOOG', 'price': 1503.41, 'change': 3.16}
    {'name': 'AAPL', 'price': 253.66, 'change': 3.16}
    {'name': 'GOOG', 'price': 1503.42, 'change': 3.17}
    {'name': 'AAPL', 'price': 253.67, 'change': 3.17}
    ...
