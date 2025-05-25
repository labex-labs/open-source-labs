# 연습 문제 2.22: 데이터 추출 (Data Extraction)

`name`과 `shares`가 `portfolio`에서 가져온 튜플 `(name, shares)`의 목록을 어떻게 만들 수 있는지 보여주세요.

```python
>>> name_shares =[ (s['name'], s['shares']) for s in portfolio ]
>>> name_shares
[('AA', 100), ('IBM', 50), ('CAT', 150), ('MSFT', 200), ('GE', 95), ('MSFT', 50), ('IBM', 100)]
>>>
```

대괄호 (`[`,`]`) 를 중괄호 (`{`, `}`) 로 변경하면 집합 컴프리헨션 (set comprehension) 이라고 하는 것을 얻게 됩니다. 이는 고유하거나 구별되는 값을 제공합니다.

예를 들어, 이것은 `portfolio`에 나타나는 고유한 주식 이름의 집합을 결정합니다.

```python
>>> names = { s['name'] for s in portfolio }
>>> names
{ 'AA', 'GE', 'IBM', 'MSFT', 'CAT' }
>>>
```

`key:value` 쌍을 지정하면 딕셔너리를 만들 수 있습니다. 예를 들어, 주식 이름을 보유한 총 주식 수에 매핑하는 딕셔너리를 만듭니다.

```python
>>> holdings = { name: 0 for name in names }
>>> holdings
{'AA': 0, 'GE': 0, 'IBM': 0, 'MSFT': 0, 'CAT': 0}
>>>
```

이 후자의 기능은 **딕셔너리 컴프리헨션 (dictionary comprehension)**이라고 합니다. 표로 정리해 보겠습니다.

```python
>>> for s in portfolio:
        holdings[s['name']] += s['shares']

>>> holdings
{ 'AA': 100, 'GE': 95, 'IBM': 150, 'MSFT':250, 'CAT': 150 }
>>>
```

`prices` 딕셔너리를 포트폴리오에 나타나는 이름만으로 필터링하는 이 예제를 시도해 보세요.

```python
>>> portfolio_prices = { name: prices[name] for name in names }
>>> portfolio_prices
{'AA': 9.22, 'GE': 13.48, 'IBM': 106.28, 'MSFT': 20.89, 'CAT': 35.46}
>>>
```
