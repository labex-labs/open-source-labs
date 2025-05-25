# 연습 문제 2.18: Counter 를 사용한 표 작성 (Tabulating with Counters)

각 주식의 총 주식 수를 표로 만들고 싶다고 가정해 봅시다. `Counter` 객체를 사용하면 쉽습니다. 시도해 보세요:

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> from collections import Counter
>>> holdings = Counter()
>>> for s in portfolio:
        holdings[s['name']] += s['shares']

>>> holdings
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
>>>
```

`portfolio`에서 `MSFT`와 `IBM`에 대한 여러 항목이 어떻게 여기에 단일 항목으로 결합되는지 주의 깊게 살펴보세요.

개별 값을 검색하기 위해 Counter 를 사전처럼 사용할 수 있습니다:

```python
>>> holdings['IBM']
150
>>> holdings['MSFT']
250
>>>
```

값을 순위별로 정렬하려면 다음과 같이 하세요:

```python
>>> # Get three most held stocks
>>> holdings.most_common(3)
[('MSFT', 250), ('IBM', 150), ('CAT', 150)]
>>>
```

다른 주식 포트폴리오를 가져와서 새로운 Counter 를 만들어 봅시다:

```python
>>> portfolio2 = read_portfolio('portfolio2.csv')
>>> holdings2 = Counter()
>>> for s in portfolio2:
          holdings2[s['name']] += s['shares']

>>> holdings2
Counter({'HPQ': 250, 'GE': 125, 'AA': 50, 'MSFT': 25})
>>>
```

마지막으로, 간단한 연산을 수행하여 모든 보유 주식을 결합해 봅시다:

```python
>>> holdings
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
>>> holdings2
Counter({'HPQ': 250, 'GE': 125, 'AA': 50, 'MSFT': 25})
>>> combined = holdings + holdings2
>>> combined
Counter({'MSFT': 275, 'HPQ': 250, 'GE': 220, 'AA': 150, 'IBM': 150, 'CAT': 150})
>>>
```

이것은 Counter 가 제공하는 기능의 작은 맛보기일 뿐입니다. 하지만 값을 표로 만들어야 할 경우, Counter 사용을 고려해야 합니다.
