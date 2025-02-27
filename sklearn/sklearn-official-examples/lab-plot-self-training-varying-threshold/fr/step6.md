# Auto-formation avec un seuil variable

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

Nous effectuons une auto-formation avec des seuils variables, en utilisant notre classifieur de base et la classe `SelfTrainingClassifier` de scikit-learn. Nous utilisons une validation croisée k-fold stratifiée pour diviser nos données en ensembles d'entraînement et de test. Nous ajustons ensuite le classifieur d auto-formation sur l ensemble d entraînement et calculons la précision du classifieur sur l ensemble de test. Nous stockons également le nombre d'échantillons étiquetés et le numéro d itération pour chaque plie.
