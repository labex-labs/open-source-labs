# 嵌套交叉验证

我们使用嵌套交叉验证来估计模型及其超参数的泛化误差。在内循环中，我们进行网格搜索以找到每个训练集的最佳超参数。在外循环中，我们在测试集上评估模型的性能。

```python
from sklearn.model_selection import KFold, cross_val_score

# 随机试验次数
NUM_TRIALS = 30

# 用于存储分数的数组
non_nested_scores = np.zeros(NUM_TRIALS)
nested_scores = np.zeros(NUM_TRIALS)

# 每次试验的循环
for i in range(NUM_TRIALS):
    # 为内循环和外循环选择交叉验证技术，
    # 与数据集无关。
    inner_cv = KFold(n_splits=4, shuffle=True, random_state=i)
    outer_cv = KFold(n_splits=4, shuffle=True, random_state=i)

    # 带有参数优化的嵌套交叉验证
    clf = GridSearchCV(estimator=svm, param_grid=p_grid, cv=inner_cv)
    nested_score = cross_val_score(clf, X=X_iris, y=y_iris, cv=outer_cv)
    nested_scores[i] = nested_score.mean()

score_difference = non_nested_score - nested_scores.mean()
```
