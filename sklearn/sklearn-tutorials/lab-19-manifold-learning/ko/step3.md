# t-distributed Stochastic Neighbor Embedding (t-SNE)

t-SNE 는 데이터 포인트의 친화도를 확률로 변환하는 인기 있는 다양체 학습 방법입니다. 특히 고차원 데이터를 시각화하는 데 효과적입니다.

```python
from sklearn.manifold import TSNE

# t-SNE 알고리즘의 인스턴스를 생성합니다.
tsne = TSNE(n_components=2)

# 알고리즘을 데이터에 맞추고 데이터를 저차원 공간으로 변환합니다.
X_transformed = tsne.fit_transform(X)
```
