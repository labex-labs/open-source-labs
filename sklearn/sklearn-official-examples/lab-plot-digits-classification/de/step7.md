# Klassifikationsbericht aus der Konfusionsmatrix rekonstruieren

Wenn die Ergebnisse der Auswertung eines Klassifizierers in Form einer Konfusionsmatrix und nicht in Form von `y_true` und `y_pred` gespeichert sind, können wir immer noch einen Klassifikationsbericht mit der `metrics.classification_report()`-Methode wie folgt erstellen:

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
