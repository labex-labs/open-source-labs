# 데이터 로드 및 준비

먼저, 당뇨병 데이터셋을 로드하고 모델링을 위해 준비합니다. scikit-learn 의 `load_diabetes` 함수를 사용하여 데이터셋을 두 개의 배열 `X`와 `y`에 로드합니다.

```python
from sklearn.datasets import load_diabetes

X, y = load_diabetes(return_X_y=True)
```
