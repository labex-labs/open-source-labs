# Entscheidungsgrenze des multinomialen logistischen Regressionsmodells zeichnen

Wir werden nun die Entscheidungsfläche des multinomialen logistischen Regressionsmodells mit der Funktion `DecisionBoundaryDisplay` aus scikit-learn zeichnen. Wir werden die Antwortmethode auf `"predict"` setzen, die Farbpalette auf `"plt.cm.Paired"` und auch die Trainingspunkte zeichnen.

```python
_, ax = plt.subplots()
DecisionBoundaryDisplay.from_estimator(
        clf, X, response_method="predict", cmap=plt.cm.Paired, ax=ax
    )
plt.title("Decision surface of LogisticRegression (multinomial)")
plt.axis("tight")

colors = "bry"
for i, color in zip(clf.classes_, colors):
        idx = np.where(y == i)
        plt.scatter(
            X[idx, 0], X[idx, 1], c=color, cmap=plt.cm.Paired, edgecolor="black", s=20
        )
```
