# 2 개의 구성요소를 사용한 PCR

PLS 와 비교하기 위해 2 개의 구성요소를 사용한 PCR 을 사용합니다.

```python
pca_2 = make_pipeline(PCA(n_components=2), LinearRegression())
pca_2.fit(X_train, y_train)
print(f"PCR r-squared with 2 components {pca_2.score(X_test, y_test):.3f}")
```
