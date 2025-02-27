# 異なる閾値での自己訓練

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

基本的な分類器と scikit - learn の `SelfTrainingClassifier` クラスを使って、異なる閾値で自己訓練を行います。データを学習用とテスト用に分割するために層化 k 分割交差検証を使用します。その後、自己訓練分類器を学習セットに適合させ、テストセットでの分類器の精度を計算します。また、各分割についてのラベル付きサンプルの数と反復回数も保存します。
