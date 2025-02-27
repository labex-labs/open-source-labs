# Modell anpassen und Vorhersagen treffen

Wir werden das Modell anpassen und Vorhersagen auf dem Evaluierungssatz treffen.

```python
grid_search.fit(X_train, y_train)

# Die von der Grid-Search mit unserer benutzerdefinierten Strategie ausgewählten Parameter sind:
grid_search.best_params_

# Schließlich evaluieren wir das feingestellte Modell auf dem ausgelassenen Evaluierungssatz: das
# `grid_search`-Objekt **wurde automatisch erneut trainiert** auf dem gesamten Trainingssatz
# mit den von unserer benutzerdefinierten Refit-Strategie ausgewählten Parametern.
y_pred = grid_search.predict(X_test)
print(classification_report(y_test, y_pred))
```
