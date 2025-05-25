# PCA 수행

이제 데이터셋을 시각화했으므로, 이제 PCA 를 수행해 보겠습니다. 이를 위해 scikit-learn 의 `PCA()` 함수를 사용할 것입니다. 데이터셋을 4 차원 (4 개의 특징) 에서 3 차원으로 줄이려고 하므로, 구성 요소의 수를 3 으로 설정합니다.

```python
pca = decomposition.PCA(n_components=3)
pca.fit(X)
X = pca.transform(X)
```
