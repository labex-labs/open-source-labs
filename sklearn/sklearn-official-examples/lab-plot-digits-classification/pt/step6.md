# Prever e Avaliar o Modelo

Usaremos o modelo treinado para prever o valor dos dígitos para as amostras no subconjunto de teste. Em seguida, avaliaremos o modelo usando os métodos `metrics.classification_report()` e `metrics.ConfusionMatrixDisplay.from_predictions()` da biblioteca `sklearn.metrics`.

```python
predicted = clf.predict(X_test)

print(
    f"Relatório de classificação para o classificador {clf}:\n"
    f"{metrics.classification_report(y_test, predicted)}\n"
)

disp = metrics.ConfusionMatrixDisplay.from_predictions(y_test, predicted)
disp.figure_.suptitle("Matriz de Confusão")
print(f"Matriz de confusão:\n{disp.confusion_matrix}")
```
