# Truncated SVD 를 이용한 차원 축소 결과 시각화

이 단계에서는 Truncated SVD 를 사용하여 차원을 축소한 결과를 시각화합니다.

```python
svd = TruncatedSVD(n_components=2)
X_reduced = svd.fit_transform(X_transformed)
```
