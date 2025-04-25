# 网格搜索

网格搜索是一种可用于找到估计器参数值最佳组合的技术。它包括指定一个参数值网格，针对每个参数组合在训练数据上拟合估计器，并选择能产生最高交叉验证分数的参数。

```python
from sklearn.model_selection import GridSearchCV

# 定义一个参数值网格
Cs = np.logspace(-6, -1, 10)

# 使用支持向量机分类器和参数网格创建一个 GridSearchCV 对象
clf = GridSearchCV(estimator=svc, param_grid=dict(C=Cs), n_jobs=-1)

# 在训练数据上拟合 GridSearchCV 对象
clf.fit(X_digits[:1000], y_digits[:1000])

print(clf.best_score_)
print(clf.best_estimator_.C)
```
