# 使用交叉验证执行网格搜索

网格搜索会详尽地搜索指定参数网格中所有可能的超参数组合。它使用交叉验证来评估每个组合的性能。

```python
# 创建GridSearchCV的实例
grid_search = GridSearchCV(svc, param_grid, cv=5)

# 拟合数据以执行网格搜索
grid_search.fit(X, y)

# 打印最佳超参数组合
print('最佳超参数:', grid_search.best_params_)
```
