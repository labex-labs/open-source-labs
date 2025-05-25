# PCA 수행

PCA 클래스의 인스턴스를 초기화하고 데이터에 맞춰 적용하여 아이리스 데이터셋에 PCA 를 수행합니다.

```python
pca = PCA(n_components=n_components)
X_pca = pca.fit_transform(X)
```
