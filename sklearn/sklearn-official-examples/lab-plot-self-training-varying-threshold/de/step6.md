# Selbsttraining mit variierendem Schwellwert

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

Wir durchführen Selbsttraining mit variierenden Schwellwerten, indem wir unseren Basisklassifizierer und die Klasse `SelfTrainingClassifier` aus scikit-learn verwenden. Wir verwenden stratifizierte Kreuzvalidierung, um unsere Daten in Trainings- und Testsets aufzuteilen. Anschließend trainieren wir den Selbsttrainingsklassifizierer auf dem Trainingsset und berechnen die Genauigkeit des Klassifizierers auf dem Testset. Wir speichern auch die Anzahl der markierten Proben und die Iterationsnummer für jede Fold.
