# 연습 문제 2.20: 시퀀스 축약 (Sequence Reductions)

단일 Python 문을 사용하여 포트폴리오의 총 비용을 계산합니다.

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> cost = sum([ s['shares'] * s['price'] for s in portfolio ])
>>> cost
44671.15
>>>
```

그 후, 단일 문을 사용하여 포트폴리오의 현재 가치를 계산하는 방법을 보여주세요.

```python
>>> value = sum([ s['shares'] * prices[s['name']] for s in portfolio ])
>>> value
28686.1
>>>
```

위의 두 연산 모두 맵 - 리덕션 (map-reduction) 의 예입니다. 리스트 컴프리헨션은 리스트 전체에 연산을 매핑합니다.

```python
>>> [ s['shares'] * s['price'] for s in portfolio ]
[3220.0000000000005, 4555.0, 12516.0, 10246.0, 3835.1499999999996, 3254.9999999999995, 7044.0]
>>>
```

그런 다음 `sum()` 함수는 결과에 대한 축약 (reduction) 을 수행합니다.

```python
>>> sum(_)
44671.15
>>>
```

이 지식을 바탕으로 이제 빅데이터 스타트업 회사를 시작할 준비가 되었습니다.
