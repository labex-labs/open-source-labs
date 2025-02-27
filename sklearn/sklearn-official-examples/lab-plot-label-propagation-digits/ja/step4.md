# モデルの性能評価

分類レポート（classification report）と混同行列（confusion matrix）を生成することで、モデルの性能を評価します。

```python
predicted_labels = lp_model.transduction_[unlabeled_set]
true_labels = y[unlabeled_set]

print(
    "Label Spreading model: %d labeled & %d unlabeled points (%d total)"
    % (n_labeled_points, n_total_samples - n_labeled_points, n_total_samples)
)

print(classification_report(true_labels, predicted_labels))

ConfusionMatrixDisplay.from_predictions(
    true_labels, predicted_labels, labels=lp_model.classes_
)
```
