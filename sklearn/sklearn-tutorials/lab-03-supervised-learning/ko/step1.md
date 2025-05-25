# 최근접 이웃 분류

이 단계에서는 최근접 이웃 분류의 개념과 scikit-learn 을 사용하여 구현하는 방법을 탐색합니다. 다양한 아이리스 꽃의 측정값으로 구성된 아이리스 데이터셋을 사용할 것입니다.

#### 아이리스 데이터셋 로드

```python
import numpy as np
from sklearn import datasets

iris_X, iris_y = datasets.load_iris(return_X_y=True)
```

#### 데이터를 학습 및 테스트 세트로 분할

```python
np.random.seed(0)
indices = np.random.permutation(len(iris_X))
iris_X_train = iris_X[indices[:-10]]
iris_y_train = iris_y[indices[:-10]]
iris_X_test = iris_X[indices[-10:]]
iris_y_test = iris_y[indices[-10:]]
```

#### 최근접 이웃 분류기 생성 및 학습

```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(iris_X_train, iris_y_train)
```

#### 예측 수행

```python
predictions = knn.predict(iris_X_test)
```
