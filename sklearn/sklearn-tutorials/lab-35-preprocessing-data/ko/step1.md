# 표준화

표준화는 많은 머신러닝 알고리즘에서 일반적인 전처리 단계입니다. 특징의 평균을 0 으로, 분산을 1 로 변환합니다. scikit-learn 의 `StandardScaler`를 사용하여 표준화를 수행할 수 있습니다.

```python
from sklearn.preprocessing import StandardScaler
import numpy as np

# 샘플 데이터 생성
X = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])

# StandardScaler 초기화
scaler = StandardScaler()

# 학습 데이터에 대해 scaler 를 맞춤
scaler.fit(X)

# 학습 데이터 변환
X_scaled = scaler.transform(X)

# 변환된 데이터 출력
print(X_scaled)
```
