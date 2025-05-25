# 데이터셋 이해

Scikit-learn 은 데이터셋을 2 차원 배열로 표현합니다. 첫 번째 축은 샘플 (관측치) 을, 두 번째 축은 특징 (변수) 을 나타냅니다. 아래는 iris 데이터셋을 사용한 예시입니다.

```python
from sklearn import datasets

iris = datasets.load_iris()
data = iris.data
print(data.shape)
```

출력:

```
(150, 4)
```

iris 데이터셋은 붓꽃 150 개의 관측치로 구성되며, 각 관측치는 4 개의 특징으로 설명됩니다. 데이터 배열의 형태는 (150, 4) 입니다.
