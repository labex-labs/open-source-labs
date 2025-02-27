# GridSearchCV を実行する

PCA トランケーションと分類器の正則化の最適な組み合わせを見つけるために、GridSearchCV を実行します。

```python
search = GridSearchCV(pipe, param_grid, n_jobs=2)
search.fit(X_digits, y_digits)
```
