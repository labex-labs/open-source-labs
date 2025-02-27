# Trainieren und Evaluieren des LabelSpreading-Modells

In diesem Schritt verwenden wir LabelSpreading auf 20 % der gelabelten Daten. Wir wählen zufällig 20 % der gelabelten Daten aus, trainieren das Modell auf diesen Daten und verwenden dann das Modell, um Labels für die verbleibenden ungelabelten Daten vorherzusagen.

```python
# Train and evaluate the LabelSpreading pipeline
ls_pipeline.fit(X_train, y_train)
y_pred = ls_pipeline.predict(X_test)
print(
    "Micro-averaged F1 score on test set: %0.3f"
    % f1_score(y_test, y_pred, average="micro")
)
```
