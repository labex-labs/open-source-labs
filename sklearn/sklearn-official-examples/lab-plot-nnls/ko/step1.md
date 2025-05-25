# 랜덤 데이터 생성

알고리즘을 테스트하기 위해 랜덤 데이터를 생성할 것입니다. 50 개의 특징을 가진 200 개의 샘플을 만들고 각 특징에 대한 실제 계수를 3 으로 설정할 것입니다. 그런 다음 계수를 임계값으로 설정하여 음수가 아닌 값으로 만들 것입니다. 마지막으로 샘플에 약간의 노이즈를 추가할 것입니다.

```python
import numpy as np

np.random.seed(42)

n_samples, n_features = 200, 50
X = np.random.randn(n_samples, n_features)
true_coef = 3 * np.random.randn(n_features)
true_coef[true_coef < 0] = 0
y = np.dot(X, true_coef)
y += 5 * np.random.normal(size=(n_samples,))
```
