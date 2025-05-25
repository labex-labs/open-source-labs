# 연습 문제 2.23: CSV 파일에서 데이터 추출

리스트, 집합 및 딕셔너리 컴프리헨션 (list, set, and dictionary comprehensions) 의 다양한 조합을 사용하는 방법을 아는 것은 다양한 형태의 데이터 처리에 유용할 수 있습니다. 다음은 CSV 파일에서 선택한 열을 추출하는 방법을 보여주는 예제입니다.

먼저, CSV 파일에서 헤더 정보 행을 읽습니다.

```python
>>> import csv
>>> f = open('portfoliodate.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> headers
['name', 'date', 'time', 'shares', 'price']
>>>
```

다음으로, 실제로 관심 있는 열을 나열하는 변수를 정의합니다.

```python
>>> select = ['name', 'shares', 'price']
>>>
```

이제 소스 CSV 파일에서 위의 열의 인덱스를 찾습니다.

```python
>>> indices = [ headers.index(colname) for colname in select ]
>>> indices
[0, 3, 4]
>>>
```

마지막으로, 데이터 행을 읽고 딕셔너리 컴프리헨션을 사용하여 딕셔너리로 변환합니다.

```python
>>> row = next(rows)
>>> record = { colname: row[index] for colname, index in zip(select, indices) }   # dict-comprehension
>>> record
{'price': '32.20', 'name': 'AA', 'shares': '100'}
>>>
```

방금 일어난 일에 익숙하다면, 파일의 나머지 부분을 읽으세요.

```python
>>> portfolio = [ { colname: row[index] for colname, index in zip(select, indices) } for row in rows ]
>>> portfolio
[{'price': '91.10', 'name': 'IBM', 'shares': '50'}, {'price': '83.44', 'name': 'CAT', 'shares': '150'},
  {'price': '51.23', 'name': 'MSFT', 'shares': '200'}, {'price': '40.37', 'name': 'GE', 'shares': '95'},
  {'price': '65.10', 'name': 'MSFT', 'shares': '50'}, {'price': '70.44', 'name': 'IBM', 'shares': '100'}]
>>>
```

맙소사, `read_portfolio()` 함수의 많은 부분을 단일 문장으로 줄였습니다.
