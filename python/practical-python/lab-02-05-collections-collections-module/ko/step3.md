# 예시: 일대다 매핑 (One-Many Mappings)

문제: 키를 여러 값에 매핑하고 싶습니다.

```python
portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]
```

이전 예제와 마찬가지로, 키 `IBM`은 대신 두 개의 서로 다른 튜플을 가져야 합니다.

해결책: `defaultdict`를 사용합니다.

```python
from collections import defaultdict
holdings = defaultdict(list)
for name, shares, price in portfolio:
    holdings[name].append((shares, price))
holdings['IBM'] # [ (50, 91.1), (100, 45.23) ]
```

`defaultdict`는 키에 접근할 때마다 기본값을 얻도록 보장합니다.
