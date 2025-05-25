# 합성 데이터 생성

scikit-learn 의 `make_classification` 함수를 사용하여 합성 데이터를 생성합니다. 이 함수는 n 개의 정보 특징, n 개의 중복 특징, 그리고 클래스당 n 개의 클러스터를 가진 무작위 n-클래스 분류 문제를 생성합니다. 2 개의 정보 특징과 난수 상태 1 을 사용하여 1000 개의 샘플을 생성합니다. 그런 다음 데이터를 훈련 세트와 테스트 세트로 60/40 비율로 분할합니다.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X, y = make_classification(
    n_samples=1_000,
    n_features=2,
    n_redundant=0,
    n_informative=2,
    random_state=1,
    n_clusters_per_class=1,
)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
```
