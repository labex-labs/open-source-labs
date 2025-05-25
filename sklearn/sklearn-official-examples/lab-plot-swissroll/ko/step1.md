# 스위스 롤 데이터셋 생성

`sklearn.datasets`의 `make_swiss_roll()` 함수를 사용하여 스위스 롤 데이터셋을 생성합니다. 이 함수는 나선형 모양의 3 차원 데이터셋을 생성합니다.

```python
import matplotlib.pyplot as plt
from sklearn import manifold, datasets

sr_points, sr_color = datasets.make_swiss_roll(n_samples=1500, random_state=0)
```
