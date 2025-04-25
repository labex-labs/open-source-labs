# 不同阈值下的自训练

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

我们使用基础分类器和 scikit-learn 中的`SelfTrainingClassifier`类，在不同阈值下进行自训练。我们使用分层 k 折交叉验证将数据拆分为训练集和测试集。然后我们在训练集上拟合自训练分类器，并计算分类器在测试集上的准确率。我们还存储了每个折的标记样本数量和迭代次数。
