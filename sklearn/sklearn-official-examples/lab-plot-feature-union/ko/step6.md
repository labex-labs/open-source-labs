# 결합된 특징

PCA 와 단변량 선택에서 얻은 특징을 `FeatureUnion` 변환기를 사용하여 결합합니다.

```python
combined_features = FeatureUnion([("pca", pca), ("univ_select", selection)])
```
