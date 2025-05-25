# 연습 문제 2.21: 데이터 쿼리 (Data Queries)

다양한 데이터 쿼리의 다음 예제를 시도해 보세요.

먼저, 100 주 이상 보유한 모든 포트폴리오 보유 목록입니다.

```python
>>> more100 = [ s for s in portfolio if s['shares'] > 100 ]
>>> more100
[{'price': 83.44, 'name': 'CAT', 'shares': 150}, {'price': 51.23, 'name': 'MSFT', 'shares': 200}]
>>>
```

MSFT 및 IBM 주식에 대한 모든 포트폴리오 보유 목록입니다.

```python
>>> msftibm = [ s for s in portfolio if s['name'] in {'MSFT','IBM'} ]
>>> msftibm
[{'price': 91.1, 'name': 'IBM', 'shares': 50}, {'price': 51.23, 'name': 'MSFT', 'shares': 200},
  {'price': 65.1, 'name': 'MSFT', 'shares': 50}, {'price': 70.44, 'name': 'IBM', 'shares': 100}]
>>>
```

10,000 달러 이상 비용이 드는 모든 포트폴리오 보유 목록입니다.

```python
>>> cost10k = [ s for s in portfolio if s['shares'] * s['price'] > 10000 ]
>>> cost10k
[{'price': 83.44, 'name': 'CAT', 'shares': 150}, {'price': 51.23, 'name': 'MSFT', 'shares': 200}]
>>>
```
