# Ergebnisse grafisch darstellen

Schließlich können wir die Ergebnisse grafisch darstellen, um die Leistung des Modells für verschiedene Iterationszahlen zu visualisieren. Wir werden die negative Log-Loss-Funktion auf der y-Achse und die Iterationszahl auf der x-Achse darstellen.

```python
plt.figure(figsize=(10, 5))
plt.plot(range(1, params['n_estimators'] + 1), cv_scores, label='CV')
plt.plot(range(1, params['n_estimators'] + 1), test_scores, label='Test')
plt.axvline(x=best_n_estimators, color='red', linestyle='--')
plt.xlabel('Number of iterations')
plt.ylabel('Negative log-loss')
plt.legend()
plt.show()
```
