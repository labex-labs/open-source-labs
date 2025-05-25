# 데이터셋 생성 및 분할

Scikit-learn 의 `make_classification` 함수를 사용하여 이진 분류 데이터셋을 생성하고, Scikit-learn 의 `train_test_split` 함수를 사용하여 데이터셋을 학습 및 테스트 서브셋으로 분할합니다.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(
    n_features=20,
    n_informative=3,
    n_redundant=0,
    n_classes=2,
    n_clusters_per_class=2,
    random_state=42,
)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
```
