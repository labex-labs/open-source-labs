# Avaliar o Desempenho do Modelo

```python
y_pred = clf.predict(X_test_pca)
print(classification_report(y_test, y_pred, target_names=target_names))
ConfusionMatrixDisplay.from_estimator(
    clf, X_test_pca, y_test, display_labels=target_names, xticks_rotation="vertical"
)
```

Prevemos os valores-alvo usando os dados de teste e avaliamos o desempenho do modelo usando a função `classification_report()`. Também plotamos a matriz de confusão usando a função `ConfusionMatrixDisplay()`.
