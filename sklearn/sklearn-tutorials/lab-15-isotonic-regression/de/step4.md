# Vorhersagen mit dem Modell

Nachdem das Modell angepasst wurde, können wir es verwenden, um Vorhersagen für neue Daten zu machen. Lassen Sie uns ein neues Array `X_new` erstellen und die entsprechenden Zielwerte vorhersagen.

```python
# Create new data for prediction
X_new = np.linspace(0, 1, 100)
y_pred = ir.predict(X_new)
```
