# Trainiere und bewerte das LabelSpreading-Modell

In diesem Schritt werden wir LabelSpreading auf 20% der markierten Daten anwenden. Wir werden 20% der markierten Daten zufällig auswählen, das Modell auf diesen Daten trainieren und dann das Modell verwenden, um die Labels für die verbleibenden unmarkierten Daten vorherzusagen.

```python
# Trainiere und bewerte die LabelSpreading-Pipeline
ls_pipeline.fit(X_train, y_train)
y_pred = ls_pipeline.predict(X_test)
print(
    "Mikro-aggregierter F1-Score auf dem Testset: %0.3f"
    % f1_score(y_test, y_pred, average="micro")
)
```