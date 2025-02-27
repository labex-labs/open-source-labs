# Обучение модели классификации на основе метода опорных векторов (Support Vector Machine, SVM)

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

Мы обучаем модель классификации SVM с использованием преобразованных данных. Мы используем функцию `RandomizedSearchCV()` для нахождения наилучших гиперпараметров для модели SVM.
