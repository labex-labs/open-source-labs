# Contadores (Counters)

Solução: Use um `Counter`.

```python
from collections import Counter
total_shares = Counter()
for name, shares, price in portfolio:
    total_shares[name] += shares

total_shares['IBM']     # 150
```
