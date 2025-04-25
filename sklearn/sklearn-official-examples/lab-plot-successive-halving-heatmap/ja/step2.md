# グリッド探索を実行する

SVC モデルに対してパラメータ探索を行うためにグリッド探索を使用します。生成した合成データセットとステップ 1 で生成したパラメータグリッドを使用します。

```python
tic = time()
gs = GridSearchCV(estimator=clf, param_grid=param_grid)
gs.fit(X, y)
gs_time = time() - tic
```
