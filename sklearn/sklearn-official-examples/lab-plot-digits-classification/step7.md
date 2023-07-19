# Rebuild Classification Report from Confusion Matrix

If the results from evaluating a classifier are stored in the form of a confusion matrix and not in terms of `y_true` and `y_pred`, we can still build a classification report using `metrics.classification_report()` method as follows:

```python
y_true = []
y_pred = []
cm = disp.confusion_matrix

for gt in range(len(cm)):
    for pred in range(len(cm)):
        y_true += [gt] * cm[gt][pred]
        y_pred += [pred] * cm[gt][pred]

print(
    "Classification report rebuilt from confusion matrix:\n"
    f"{metrics.classification_report(y_true, y_pred)}\n"
)
```
