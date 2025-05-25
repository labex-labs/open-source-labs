# 희소 배열 생성

먼저, 희소 값을 효율적으로 저장하기 위한 pandas 데이터 구조인 희소 배열 (SparseArray) 을 생성합니다. 희소 값은 대부분의 값과 유사하여 중복으로 간주되므로 저장되지 않는 값입니다.

```python
# 필요한 라이브러리 임포트
import pandas as pd
import numpy as np

# 랜덤 값으로 numpy 배열 생성
arr = np.random.randn(10)

# 일부 값을 NaN 으로 설정
arr[2:-2] = np.nan

# pandas 로 희소 배열 생성
ts = pd.Series(pd.arrays.SparseArray(arr))

# 희소 배열 출력
print(ts)
```
