# Zeichne die Entscheidungsgrenze basierend auf der Pfadlänge

Durch Festlegung von `response_method="decision_function"` repräsentiert der Hintergrund der `DecisionBoundaryDisplay` die Normalitätsmessung einer Beobachtung. Ein solcher Score wird durch die über einen Wald von zufälligen Bäumen gemittelte Pfadlänge gegeben, die selbst durch die Tiefe des Blattes (oder gleichwertig die Anzahl der Aufteilungen) angegeben wird, die erforderlich ist, um eine gegebene Probe zu isolieren.

```python
disp = DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    response_method="decision_function",
    alpha=0.5,
)
disp.ax_.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolor="k")
disp.ax_.set_title("Entscheidungsgrenze basierend auf der Pfadlänge \nvon IsolationForest")
plt.axis("square")
plt.legend(handles=handles, labels=["Ausreißer", "Innerpunkte"], title="wahre Klasse")
plt.colorbar(disp.ax_.collections[1])
plt.show()
```
