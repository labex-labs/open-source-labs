# Isomap

Isomap 알고리즘은 다양체 학습의 초기 접근 방식 중 하나입니다. 모든 점 사이의 지오데식 거리를 유지하는 저차원 임베딩을 찾습니다.

```python
from sklearn.manifold import Isomap

# Isomap 알고리즘의 인스턴스를 생성합니다.
isomap = Isomap(n_components=2)

# 알고리즘을 데이터에 맞추고 데이터를 저차원 공간으로 변환합니다.
X_transformed = isomap.fit_transform(X)
```
