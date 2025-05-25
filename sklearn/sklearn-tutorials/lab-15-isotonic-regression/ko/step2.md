# 샘플 데이터 생성

다음으로, 등장값 회귀 모델에 맞출 샘플 데이터를 생성해야 합니다. 이 예제에서는 입력 데이터와 대상 값을 각각 나타내는 두 개의 배열 `X`와 `y`를 생성합니다.

```python
import numpy as np

# 랜덤 입력 데이터 생성
np.random.seed(0)
X = np.random.rand(100)
y = 4 * X + np.random.randn(100)
```
