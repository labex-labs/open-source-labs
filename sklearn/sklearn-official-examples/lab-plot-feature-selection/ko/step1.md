# 샘플 데이터 생성

먼저, 이 데모를 위해 샘플 데이터를 생성합니다. 아이리스 (iris) 데이터 세트를 사용하고 상관 관계가 없는 일부 잡음 데이터를 추가합니다.

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# 아이리스 데이터 세트
X, y = load_iris(return_X_y=True)

# 상관 관계가 없는 일부 잡음 데이터
E = np.random.RandomState(42).uniform(0, 0.1, size=(X.shape[0], 20))

# 정보 특징에 잡음 데이터 추가
X = np.hstack((X, E))

# 특징 선택 및 분류기 평가를 위해 데이터 세트 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)
```
