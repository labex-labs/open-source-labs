# 추정기 및 조기 종료 전략 정의

다음 단계는 추정기와 조기 종료 전략을 정의하는 것입니다. scikit-learn 의 `SGDClassifier` 모델을 사용할 것입니다. 세 가지 다른 중단 기준 (중단 기준 없음, 훈련 손실, 검증 점수) 을 정의할 것입니다. `fit_and_score` 함수를 사용하여 추정기를 훈련 세트에 맞추고 두 세트 모두에 대해 점수를 매길 것입니다.

```python
@ignore_warnings(category=ConvergenceWarning)
def fit_and_score(estimator, max_iter, X_train, X_test, y_train, y_test):
    """훈련 세트에 추정기를 맞추고 두 세트 모두에 대해 점수를 매깁니다."""
    estimator.set_params(max_iter=max_iter)
    estimator.set_params(random_state=0)

    start = time.time()
    estimator.fit(X_train, y_train)

    fit_time = time.time() - start
    n_iter = estimator.n_iter_
    train_score = estimator.score(X_train, y_train)
    test_score = estimator.score(X_test, y_test)

    return fit_time, n_iter, train_score, test_score

# 비교할 추정기 정의
estimator_dict = {
    "중단 기준 없음": linear_model.SGDClassifier(n_iter_no_change=3),
    "훈련 손실": linear_model.SGDClassifier(
        early_stopping=False, n_iter_no_change=3, tol=0.1
    ),
    "검증 점수": linear_model.SGDClassifier(
        early_stopping=True, n_iter_no_change=3, tol=0.0001, validation_fraction=0.2
    ),
}
```
