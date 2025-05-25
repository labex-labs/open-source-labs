# 독립 성분 - FastICA

독립 성분 분석 (ICA) 은 다변량 신호를 최대 독립적인 가산 하위 성분으로 분리하는 방법입니다. ICA 에 대한 빠르고 강력한 알고리즘인 FastICA 를 적용합니다.

```python
# 독립 성분 - FastICA
ica_estimator = decomposition.FastICA(
    n_components=n_components, max_iter=400, whiten="arbitrary-variance", tol=15e-5
)
ica_estimator.fit(faces_centered)
plot_gallery(
    "독립 성분 - FastICA", ica_estimator.components_[:n_components]
)
```
