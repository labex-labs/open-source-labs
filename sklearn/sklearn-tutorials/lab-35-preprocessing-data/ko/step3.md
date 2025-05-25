# 정규화

정규화는 개별 샘플의 노름 (norm) 을 1 로 조정하는 과정입니다. 데이터의 크기가 중요하지 않고 방향 (또는 각도) 만 관심 있는 경우에 일반적으로 사용됩니다. scikit-learn 의 `Normalizer`를 사용하여 정규화를 수행할 수 있습니다.

```python
from sklearn.preprocessing import Normalizer
import numpy as np

# 샘플 데이터 생성
X = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])

# Normalizer 초기화
normalizer = Normalizer()

# 학습 데이터에 대해 fit 및 transform
X_normalized = normalizer.fit_transform(X)

# 변환된 데이터 출력
print(X_normalized)
```
