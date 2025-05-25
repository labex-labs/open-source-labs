# 다양한 임계값을 사용한 자가 학습

```python
for i, threshold in enumerate(x_values):
    self_training_clf = SelfTrainingClassifier(base_classifier, threshold=threshold)

    skfolds = StratifiedKFold(n_splits=n_splits)
    for fold, (train_index, test_index) in enumerate(skfolds.split(X, y)):
        X_train = X[train_index]
        y_train = y[train_index]
        X_test = X[test_index]
        y_test = y[test_index]
        y_test_true = y_true[test_index]

        self_training_clf.fit(X_train, y_train)

        amount_labeled[i, fold] = (
            total_samples
            - np.unique(self_training_clf.labeled_iter_, return_counts=True)[1][0]
        )

        amount_iterations[i, fold] = np.max(self_training_clf.labeled_iter_)

        y_pred = self_training_clf.predict(X_test)
        scores[i, fold] = accuracy_score(y_test_true, y_pred)
```

기본 분류기를 사용하고 scikit-learn 의 `SelfTrainingClassifier` 클래스를 활용하여 다양한 임계값으로 자가 학습을 수행합니다. 계층적 k-겹 교차 검증을 사용하여 데이터를 학습 및 테스트 세트로 분할합니다. 그런 다음 학습 세트에서 자가 학습 분류기를 학습시키고, 테스트 세트에서 분류기의 정확도를 계산합니다. 또한 각 폴드에 대한 레이블링된 샘플 수와 반복 횟수를 저장합니다.
