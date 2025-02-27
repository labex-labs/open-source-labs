# Ridge Regression

Ridge Regression ist eine lineare Regressionsmethode, die einem gewöhnlichen kleinsten Quadrate Zielfunktion einen Strafbegriff hinzufügt. Dieser Strafbegriff hilft dabei, das Overfitting zu reduzieren, indem die Koeffizienten gegen Null zusammenziehen. Die Komplexität des Modells kann durch den Regularisierungsparameter kontrolliert werden.

Lassen Sie uns ein Ridge-Regressionsmodell anpassen.

```python
reg = linear_model.Ridge(alpha=0.5)
reg.fit([[0, 0], [0, 0], [1, 1]], [0, 0.1, 1])

print(reg.coef_)
```

- Wir erstellen eine Instanz von `Ridge` mit dem Regularisierungsparameter `alpha` auf 0,5 gesetzt.
- Wir verwenden die `fit`-Methode, um das Modell an die Trainingsdaten anzupassen.
- Wir drucken die Koeffizienten des Ridge-Regressionsmodells.
