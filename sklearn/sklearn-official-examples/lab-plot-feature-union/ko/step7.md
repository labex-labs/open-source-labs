# 변환된 데이터셋

결합된 특징을 사용하여 데이터셋을 변환합니다.

```python
X_features = combined_features.fit(X, y).transform(X)
print("결합된 공간에는", X_features.shape[1], "개의 특징이 있습니다")
```
