# Entraîner un modèle de classification à machine à vecteurs de support (SVM)

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

Nous entraînons un modèle de classification SVM en utilisant les données transformées. Nous utilisons `RandomizedSearchCV()` pour trouver les meilleurs hyperparamètres pour le modèle SVM.
