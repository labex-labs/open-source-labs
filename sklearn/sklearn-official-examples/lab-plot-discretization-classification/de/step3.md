# Klassifizierer und Parameter definieren

In diesem Schritt werden wir die Klassifizierer und die Parameter definieren, die im Feature-Diskretisierungsprozess verwendet werden sollen. Wir werden eine Liste von Klassifizierern erstellen, die Logistische Regression, linearen Support-Vektor-Maschine (SVM), Gradienten-Boosting-Klassifizierer und SVM mit einem radialbasisfunktionellen Kern umfasst. Wir werden auch einen Satz von Parametern für jeden Klassifizierer definieren, die im GridSearchCV-Algorithmus verwendet werden sollen.

```python
# Liste von (Schätzer, param_grid), wobei param_grid im GridSearchCV verwendet wird
# Die Parameterspaces in diesem Beispiel sind auf einen schmalen Bereich begrenzt, um die Laufzeit zu reduzieren.
# In einem realen Anwendungsfall sollte ein breiterer Suchraum für die Algorithmen verwendet werden.
classifiers = [
    (
        make_pipeline(StandardScaler(), LogisticRegression(random_state=0)),
        {"logisticregression__C": np.logspace(-1, 1, 3)},
    ),
    (
        make_pipeline(StandardScaler(), LinearSVC(random_state=0, dual="auto")),
        {"linearsvc__C": np.logspace(-1, 1, 3)},
    ),
    (
        make_pipeline(
            StandardScaler(),
            KBinsDiscretizer(encode="onehot"),
            LogisticRegression(random_state=0),
        ),
        {
            "kbinsdiscretizer__n_bins": np.arange(5, 8),
            "logisticregression__C": np.logspace(-1, 1, 3),
        },
    ),
    (
        make_pipeline(
            StandardScaler(),
            KBinsDiscretizer(encode="onehot"),
            LinearSVC(random_state=0, dual="auto"),
        ),
        {
            "kbinsdiscretizer__n_bins": np.arange(5, 8),
            "linearsvc__C": np.logspace(-1, 1, 3),
        },
    ),
    (
        make_pipeline(
            StandardScaler(), GradientBoostingClassifier(n_estimators=5, random_state=0)
        ),
        {"gradientboostingclassifier__learning_rate": np.logspace(-2, 0, 5)},
    ),
    (
        make_pipeline(StandardScaler(), SVC(random_state=0)),
        {"svc__C": np.logspace(-1, 1, 3)},
    ),
]

names = [get_name(e).replace("StandardScaler + ", "") for e, _ in classifiers]
```
