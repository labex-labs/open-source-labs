# 执行网格搜索

在这一步中，我们将使用GridSearchCV函数来执行网格搜索。我们将为决策树分类器模型的min_samples_split参数搜索最佳超参数。

```python
gs = GridSearchCV(
    DecisionTreeClassifier(random_state=42),
    param_grid={"min_samples_split": range(2, 403, 20)},
    scoring=scoring,
    refit="AUC",
    n_jobs=2,
    return_train_score=True,
)
gs.fit(X, y)
results = gs.cv_results_
```
