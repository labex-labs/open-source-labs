# 데이터 준비

먼저 80,000 개의 샘플로 구성된 대규모 데이터셋을 만들고 세 개의 집합으로 분할합니다.

- 나중에 특징 공학 변환기로 사용되는 앙상블 방법을 학습시키기 위한 집합
- 선형 모델을 학습시키기 위한 집합
- 선형 모델을 테스트하기 위한 집합

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=80_000, random_state=10)

X_full_train, X_test, y_full_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=10
)

X_train_ensemble, X_train_linear, y_train_ensemble, y_train_linear = train_test_split(
    X_full_train, y_full_train, test_size=0.5, random_state=10
)
```
