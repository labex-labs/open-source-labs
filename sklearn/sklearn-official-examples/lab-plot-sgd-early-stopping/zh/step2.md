# 定义估计器和早停策略

下一步是定义估计器和早停策略。我们将使用 scikit-learn 中的 `SGDClassifier` 模型。我们将定义三种不同的停止标准：无停止标准、训练损失和验证分数。我们将使用 `fit_and_score` 函数在训练集上拟合估计器，并在两个数据集上对其进行评分。

```python
@ignore_warnings(category=ConvergenceWarning)
def fit_and_score(estimator, max_iter, X_train, X_test, y_train, y_test):
    """在训练集上拟合估计器，并在两个数据集上对其进行评分"""
    estimator.set_params(max_iter=max_iter)
    estimator.set_params(random_state=0)

    start = time.time()
    estimator.fit(X_train, y_train)

    fit_time = time.time() - start
    n_iter = estimator.n_iter_
    train_score = estimator.score(X_train, y_train)
    test_score = estimator.score(X_test, y_test)

    return fit_time, n_iter, train_score, test_score

# 定义要比较的估计器
estimator_dict = {
    "无停止标准": linear_model.SGDClassifier(n_iter_no_change=3),
    "训练损失": linear_model.SGDClassifier(
        early_stopping=False, n_iter_no_change=3, tol=0.1
    ),
    "验证分数": linear_model.SGDClassifier(
        early_stopping=True, n_iter_no_change=3, tol=0.0001, validation_fraction=0.2
    ),
}
```
