# 推定器と早期終了戦略を定義する

次のステップは、推定器と早期終了戦略を定義することです。scikit-learnの`SGDClassifier`モデルを使用します。3つの異なる停止基準を定義します：停止基準なし、学習損失、検証スコア。`fit_and_score`関数を使用して、推定器をトレーニングセットに適合させ、両方のセットでスコア付けします。

```python
@ignore_warnings(category=ConvergenceWarning)
def fit_and_score(estimator, max_iter, X_train, X_test, y_train, y_test):
    """推定器をトレーニングセットに適合させ、両方のセットでスコア付けする"""
    estimator.set_params(max_iter=max_iter)
    estimator.set_params(random_state=0)

    start = time.time()
    estimator.fit(X_train, y_train)

    fit_time = time.time() - start
    n_iter = estimator.n_iter_
    train_score = estimator.score(X_train, y_train)
    test_score = estimator.score(X_test, y_test)

    return fit_time, n_iter, train_score, test_score

# 比較する推定器を定義する
estimator_dict = {
    "停止基準なし": linear_model.SGDClassifier(n_iter_no_change=3),
    "学習損失": linear_model.SGDClassifier(
        early_stopping=False, n_iter_no_change=3, tol=0.1
    ),
    "検証スコア": linear_model.SGDClassifier(
        early_stopping=True, n_iter_no_change=3, tol=0.0001, validation_fraction=0.2
    ),
}
```
