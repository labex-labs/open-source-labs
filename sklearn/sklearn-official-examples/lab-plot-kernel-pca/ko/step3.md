# PCA 를 이용한 데이터셋 투영

PCA 를 사용하여 데이터셋을 원래의 변동성을 대부분 유지하는 새로운 공간으로 투영합니다.

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)

X_test_pca = pca.fit(X_train).transform(X_test)
```
