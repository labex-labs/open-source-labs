# 데이터 로드 및 준비

먼저 Covtype 데이터셋을 로드하고, 하나의 클래스만 선택하여 이진 분류 문제로 변환합니다. 그런 다음 데이터를 학습 세트와 테스트 세트로 분할하고 특징을 정규화합니다.

```python
from sklearn.datasets import fetch_covtype
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, Normalizer

# Covtype 데이터셋을 로드하고, 하나의 클래스만 선택
X, y = fetch_covtype(return_X_y=True)
y[y != 2] = 0
y[y == 2] = 1

# 데이터를 학습 세트와 테스트 세트로 분할
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=5000, test_size=10000, random_state=42
)

# 특징 정규화
mm = make_pipeline(MinMaxScaler(), Normalizer())
X_train = mm.fit_transform(X_train)
X_test = mm.transform(X_test)
```
