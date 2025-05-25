# 음수가 아닌 성분 - NMF

다음으로, 음수가 아닌 행렬 분해 (NMF) 를 적용합니다. NMF 는 데이터 행렬을 두 개의 음수가 아닌 행렬로 분해합니다. 하나는 기저 벡터를 포함하고 다른 하나는 계수를 포함합니다. 이는 데이터의 부분 기반 표현으로 이어집니다.

```python
# 음수가 아닌 성분 - NMF
nmf_estimator = decomposition.NMF(n_components=n_components, tol=5e-3)
nmf_estimator.fit(faces)  # 원본 음수가 아닌 데이터 세트
plot_gallery("음수가 아닌 성분 - NMF", nmf_estimator.components_[:n_components])
```
