# GridSearchCV オブジェクトを作成してデータに適合させる

前のステップで定義したパイプラインとパラメータグリッドを使用して `GridSearchCV` オブジェクトを作成します。その後、データをこのオブジェクトに適合させます。

```python
grid = GridSearchCV(pipe, n_jobs=1, param_grid=param_grid)
grid.fit(X, y)
```
