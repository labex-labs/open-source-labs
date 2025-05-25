# 데이터셋

100,000 개의 샘플과 20 개의 특징을 가진 합성 이진 분류 데이터셋을 사용합니다. 20 개의 특징 중 2 개만 정보적이고, 10 개는 중복적 (정보적 특징의 무작위 조합) 이며, 나머지 8 개는 비정보적 (무작위 숫자) 입니다. 100,000 개의 샘플 중 1,000 개는 모델 학습에 사용하고 나머지는 테스트에 사용합니다.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(
    n_samples=100_000, n_features=20, n_informative=2, n_redundant=10, random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.99, random_state=42
)
```
