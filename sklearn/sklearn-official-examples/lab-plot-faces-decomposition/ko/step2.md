# 고유 얼굴 - 무작위 SVD 를 사용한 PCA

적용하는 첫 번째 방법은 PCA(주성분 분석) 입니다. PCA 는 데이터의 특이값 분해 (SVD) 를 사용하여 데이터를 저차원 공간으로 투영하는 선형 차원 축소 기법입니다. 표준 SVD 알고리즘의 빠른 근사값인 무작위 SVD 를 사용합니다. 처음 여섯 개의 주성분을 플롯합니다. 이 주성분들을 고유 얼굴이라고 합니다.

```python
# 고유 얼굴 - 무작위 SVD 를 사용한 PCA
pca_estimator = decomposition.PCA(
    n_components=n_components, svd_solver="randomized", whiten=True
)
pca_estimator.fit(faces_centered)
plot_gallery(
    "고유 얼굴 - 무작위 SVD 를 사용한 PCA", pca_estimator.components_[:n_components]
)
```
