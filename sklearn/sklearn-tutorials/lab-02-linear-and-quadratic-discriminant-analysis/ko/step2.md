# 합성 데이터 생성

다음으로, LDA 와 QDA 의 차이를 보여주기 위해 합성 데이터를 생성합니다. scikit-learn 의 `make_classification` 함수를 사용하여 서로 다른 패턴을 가진 두 개의 클래스를 생성합니다.

```python
from sklearn.datasets import make_classification

# 합성 데이터 생성
X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, n_classes=2, random_state=1)
```
