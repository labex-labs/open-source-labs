# 비음수 행렬 분해 (NMF)

#### Frobenius 노름을 사용한 NMF

비음수 행렬 분해 (NMF) 는 비음수 데이터와 성분을 가정하는 분해의 대안적인 방법입니다. 두 행렬의 곱과 데이터 사이의 거리를 최적화하여 데이터를 비음수 요소로 구성된 두 행렬로 분해합니다. NMF 는 scikit-learn 의 `NMF` 클래스를 사용하여 구현할 수 있습니다.

```python
from sklearn.decomposition import NMF

# 원하는 성분의 수를 n_components 로 설정한 NMF 객체 생성
nmf = NMF(n_components=2)

# NMF 모델을 데이터에 맞춤
nmf.fit(data)

# 데이터를 두 개의 비음수 행렬로 분해
matrix_W = nmf.transform(data)
matrix_H = nmf.components_
```
