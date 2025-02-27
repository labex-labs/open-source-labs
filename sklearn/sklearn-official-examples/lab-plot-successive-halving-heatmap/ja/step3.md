# 逐次半分法を実行する

ここでは、ステップ2で使用した同じSVCモデルとデータセットに対して、逐次半分法を使ってパラメータ探索を行います。

```python
tic = time()
gsh = HalvingGridSearchCV(
    estimator=clf, param_grid=param_grid, factor=2, random_state=rng
)
gsh.fit(X, y)
gsh_time = time() - tic
```
