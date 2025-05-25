# PCA 수행

다음으로, 데이터 세트에 PCA 를 수행합니다. 먼저 `x`, `y`, `z`를 연결하여 3 차원 배열 `Y`를 만듭니다. 그런 다음 PCA 클래스의 인스턴스를 만들고 데이터에 맞춥니다. 그런 다음 PCA 객체의 `components_` 속성을 사용하여 주요 구성 요소에 액세스할 수 있습니다.

```python
Y = np.c_[x, y, z]
pca = PCA(n_components=3)
pca.fit(Y)
components = pca.components_
```
