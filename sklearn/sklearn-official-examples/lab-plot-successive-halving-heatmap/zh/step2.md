# 执行网格搜索

我们将使用网格搜索对支持向量分类（SVC）模型进行参数搜索。我们将使用生成的合成数据集以及在步骤 1 中生成的参数网格。

```python
tic = time()
gs = GridSearchCV(estimator=clf, param_grid=param_grid)
gs.fit(X, y)
gs_time = time() - tic
```
