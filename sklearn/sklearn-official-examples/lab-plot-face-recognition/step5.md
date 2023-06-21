# Train a Support Vector Machine (SVM) Classification Model

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

We train a SVM classification model using the transformed data. We use `RandomizedSearchCV()` to find the best hyperparameters for the SVM model.
