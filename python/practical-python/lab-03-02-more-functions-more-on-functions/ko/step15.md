# 연습 3.5: 타입 변환 수행

`/home/labex/project/fileparse_3.5.py` 디렉토리의 `parse_csv()` 함수를 수정하여 반환된 데이터에 타입 변환을 선택적으로 적용할 수 있도록 합니다. 예를 들어:

```python
>>> portfolio = parse_csv('/home/labex/project/portfolio.csv', types=[str, int, float])
>>> portfolio
[{'name': 'AA', 'shares': 100, 'price': 32.2}, {'name': 'IBM', 'shares': 50, 'price': 91.1}, {'name': 'CAT', 'shares': 150, 'price': 83.44}, {'name': 'MSFT', 'shares': 200, 'price': 51.23}, {'name': 'GE', 'shares': 95, 'price': 40.37}, {'name': 'MSFT', 'shares': 50, 'price': 65.1}, {'name': 'IBM', 'shares': 100, 'price': 70.44}]

>>> shares_held = parse_csv('/home/labex/project/portfolio.csv', select=['name', 'shares'], types=[str, int])
>>> shares_held
[{'name': 'AA', 'shares': 100}, {'name': 'IBM', 'shares': 50}, {'name': 'CAT', 'shares': 150}, {'name': 'MSFT', 'shares': 200}, {'name': 'GE', 'shares': 95}, {'name': 'MSFT', 'shares': 50}, {'name': 'IBM', 'shares': 100}]
>>>
```

이미 연습 2.24 에서 이를 탐구했습니다. 다음 코드 조각을 솔루션에 삽입해야 합니다.

```python
...
if types:
    row = [func(val) for func, val in zip(types, row) ]
...
```
