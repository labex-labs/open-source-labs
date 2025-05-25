# Treinar um Modelo de Classificação de Máquina de Vetores de Suporte (SVM)

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

Treinamos um modelo de classificação SVM usando os dados transformados. Usamos `RandomizedSearchCV()` para encontrar os melhores hiperparâmetros para o modelo SVM.
