# Ein Support-Vektor-Maschinen (Support Vector Machine, SVM)-Klassifizierungsmodell trainieren

```python
param_grid = {
    "C": loguniform(1e3, 1e5),
    "gamma": loguniform(1e-4, 1e-1),
}

clf = RandomizedSearchCV(
    SVC(kernel="rbf", class_weight="balanced"), param_grid, n_iter=10
)
clf = clf.fit(X_train_pca, y_train)
```

Wir trainieren ein SVM-Klassifizierungsmodell mit den transformierten Daten. Wir verwenden `RandomizedSearchCV()`, um die besten Hyperparameter für das SVM-Modell zu finden.
