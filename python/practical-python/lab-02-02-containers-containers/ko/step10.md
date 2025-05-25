# 연습 문제 2.5: 딕셔너리의 리스트

연습 문제 2.4 에서 작성한 함수를 가져와 튜플 대신 딕셔너리로 포트폴리오의 각 주식을 나타내도록 수정합니다. 이 딕셔너리에서 "name", "shares", "price" 필드 이름을 사용하여 입력 파일의 서로 다른 열을 나타냅니다.

연습 문제 2.4 에서와 동일한 방식으로 이 새로운 함수를 실험해 보십시오.

```python
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')
>>> portfolio
[{'name': 'AA', 'shares': 100, 'price': 32.2}, {'name': 'IBM', 'shares': 50, 'price': 91.1},
    {'name': 'CAT', 'shares': 150, 'price': 83.44}, {'name': 'MSFT', 'shares': 200, 'price': 51.23},
    {'name': 'GE', 'shares': 95, 'price': 40.37}, {'name': 'MSFT', 'shares': 50, 'price': 65.1},
    {'name': 'IBM', 'shares': 100, 'price': 70.44}]
>>> portfolio[0]
{'name': 'AA', 'shares': 100, 'price': 32.2}
>>> portfolio[1]
{'name': 'IBM', 'shares': 50, 'price': 91.1}
>>> portfolio[1]['shares']
50
>>> total = 0.0
>>> for s in portfolio:
        total += s['shares']*s['price']

>>> print(total)
44671.15
>>>
```

여기에서 각 항목의 서로 다른 필드는 숫자 열 번호 대신 키 이름으로 액세스됨을 알 수 있습니다. 결과 코드가 나중에 읽기 더 쉽기 때문에 이 방법이 선호되는 경우가 많습니다.

큰 딕셔너리와 리스트를 보는 것은 지저분할 수 있습니다. 디버깅을 위해 출력을 정리하려면 `pprint` 함수를 사용하는 것을 고려하십시오.

```python
>>> from pprint import pprint
>>> pprint(portfolio)
[{'name': 'AA', 'price': 32.2, 'shares': 100},
    {'name': 'IBM', 'price': 91.1, 'shares': 50},
    {'name': 'CAT', 'price': 83.44, 'shares': 150},
    {'name': 'MSFT', 'price': 51.23, 'shares': 200},
    {'name': 'GE', 'price': 40.37, 'shares': 95},
    {'name': 'MSFT', 'price': 65.1, 'shares': 50},
    {'name': 'IBM', 'price': 70.44, 'shares': 100}]
>>>
```
