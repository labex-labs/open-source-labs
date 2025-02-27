# Darstellung der partiellen Abhängigkeit für zwei Merkmale

In diesem Schritt werden wir die partiellen Abhängigkeitskurven für die Merkmale "age" (Alter) und "bmi" (Körpermasseindex) für den Entscheidungsbaum darstellen. Bei zwei Merkmalen erwartet `PartialDependenceDisplay.from_estimator`, zwei Kurven zu plotten. Hier platziert die Plot-Funktion ein Gitter von zwei Plots mithilfe des durch `ax` definierten Raums.

```python
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_title("Decision Tree")
tree_disp = PartialDependenceDisplay.from_estimator(tree, X, ["age", "bmi"], ax=ax)
```

Die partiellen Abhängigkeitskurven können auch für das Multilayer-Perzeptron geplottet werden. In diesem Fall wird `line_kw` an `PartialDependenceDisplay.from_estimator` übergeben, um die Farbe der Kurve zu ändern.

```python
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_title("Multi-layer Perceptron")
mlp_disp = PartialDependenceDisplay.from_estimator(
    mlp, X, ["age", "bmi"], ax=ax, line_kw={"color": "red"}
)
```
