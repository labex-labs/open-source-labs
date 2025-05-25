# 데이터셋 로드 및 랜덤 피처 생성

붓꽃 (iris) 데이터셋을 사용할 것입니다. 이 데이터셋은 3 가지 종류의 붓꽃에서 측정된 값으로 구성되어 있으며, 붓꽃 데이터셋의 클래스 레이블과 상관관계가 없는 랜덤 피처 데이터 (즉, 20 개의 피처) 를 생성합니다.

```python
from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()
X = iris.data
y = iris.target

n_uncorrelated_features = 20
rng = np.random.RandomState(seed=0)
X_rand = rng.normal(size=(X.shape[0], n_uncorrelated_features))
```
