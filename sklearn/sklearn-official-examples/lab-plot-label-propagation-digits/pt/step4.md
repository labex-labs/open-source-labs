# Avaliar o Desempenho do Modelo

Avaliamos o desempenho do modelo gerando um relatório de classificação e uma matriz de confusão.

```python
predicted_labels = lp_model.transduction_[unlabeled_set]
true_labels = y[unlabeled_set]

print(
    "Modelo de Propagação de Rótulos: %d pontos rotulados & %d pontos não rotulados (%d total)"
    % (n_labeled_points, n_total_samples - n_labeled_points, n_total_samples)
)

print(classification_report(true_labels, predicted_labels))

ConfusionMatrixDisplay.from_predictions(
    true_labels, predicted_labels, labels=lp_model.classes_
)
```
