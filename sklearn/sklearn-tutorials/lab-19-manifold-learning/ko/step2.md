# Locally Linear Embedding (LLE)

Locally Linear Embedding (LLE) 는 또 다른 다양체 학습 알고리즘입니다. 데이터의 국소 이웃 내 거리를 보존하는 저차원 투영을 찾습니다.

```python
from sklearn.manifold import LocallyLinearEmbedding

# LLE 알고리즘의 인스턴스를 생성합니다.
lle = LocallyLinearEmbedding(n_components=2)

# 알고리즘을 데이터에 맞추고 데이터를 저차원 공간으로 변환합니다.
X_transformed = lle.fit_transform(X)
```
