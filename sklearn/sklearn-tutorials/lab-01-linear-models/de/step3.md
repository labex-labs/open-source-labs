# Lasso

Lasso ist eine lineare Regressionsmethode, die einem gewöhnlichen kleinsten Quadrate Zielfunktion einen Strafbegriff hinzufügt. Der Strafbegriff hat die Wirkung, einige Koeffizienten genau auf Null zu setzen, wodurch eine Feature-Selektion durchgeführt wird. Lasso kann zur Schätzung von sparsen Modellen verwendet werden.

Lassen Sie uns ein Lasso-Modell anpassen.

```python
reg = linear_model.Lasso(alpha=0.1)
reg.fit([[0, 0], [1, 1]], [0, 1])

print(reg.coef_)
```

- Wir erstellen eine Instanz von `Lasso` mit dem Regularisierungsparameter `alpha` auf 0,1 gesetzt.
- Wir verwenden die `fit`-Methode, um das Modell an die Trainingsdaten anzupassen.
- Wir drucken die Koeffizienten des Lasso-Modells.
