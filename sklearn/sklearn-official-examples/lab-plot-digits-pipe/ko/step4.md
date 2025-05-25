# GridSearchCV 수행

PCA 절단과 분류기 정규화의 최적 조합을 찾기 위해 GridSearchCV 를 수행합니다.

```python
search = GridSearchCV(pipe, param_grid, n_jobs=2)
search.fit(X_digits, y_digits)
```
