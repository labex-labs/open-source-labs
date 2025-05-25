# 데이터셋 로드

`sklearn.datasets`의 `make_circles` 함수를 사용하여 두 개의 중첩된 원으로 구성된 데이터셋을 생성합니다.

```python
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split

X, y = make_circles(n_samples=1_000, factor=0.3, noise=0.05, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)
```
