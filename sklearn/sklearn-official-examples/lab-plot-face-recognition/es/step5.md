# Entrenar un modelo de clasificación con Máquinas de Vectores de Soporte (SVM)

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

Entrenamos un modelo de clasificación con SVM utilizando los datos transformados. Utilizamos `RandomizedSearchCV()` para encontrar los mejores hiperparámetros para el modelo SVM.
