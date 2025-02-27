# Label die am ungewissesten Punkte

Wir werden die menschlichen Labels zu den gelabelten Datenpunkten hinzufügen und das Modell mit ihnen trainieren.

```python
y_train[uncertainty_index] = y[uncertainty_index]
lp_model.fit(X, y_train)
```
