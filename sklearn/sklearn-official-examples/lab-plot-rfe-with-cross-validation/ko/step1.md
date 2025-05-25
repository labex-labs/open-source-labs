# 데이터 생성

scikit-learn 의 `make_classification` 함수를 사용하여 분류 작업을 생성할 것입니다. 15 개의 특징 중 3 개는 정보적이고, 2 개는 중복되며, 10 개는 정보가 없는 500 개의 샘플을 생성할 것입니다.

```python
from sklearn.datasets import make_classification

X, y = make_classification(
    n_samples=500,
    n_features=15,
    n_informative=3,
    n_redundant=2,
    n_repeated=0,
    n_classes=8,
    n_clusters_per_class=1,
    class_sep=0.8,
    random_state=0,
)
```
