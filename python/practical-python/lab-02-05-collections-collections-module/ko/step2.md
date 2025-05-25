# Counter (카운터)

해결책: `Counter`를 사용합니다.

```python
from collections import Counter
total_shares = Counter()
for name, shares, price in portfolio:
    total_shares[name] += shares

total_shares['IBM']     # 150
```
