# Darstellung der Ergebnisse

Schließlich stellen wir dar, wie gut unsere beiden Regressoren, der einzelne Decision Tree Regressor und der AdaBoost Regressor, die Daten approximieren können. Wir verwenden die `scatter()`-Funktion von Matplotlib, um die Trainingsdatenpunkte und die vorhergesagten Werte beider Regressoren zu plotten. Wir verwenden die `plot()`-Funktion von Matplotlib, um die vorhergesagten Werte gegen die Daten für beide Regressoren zu plotten. Wir fügen einer Legende hinzu, um zwischen den beiden Regressoren zu unterscheiden.

```python
import matplotlib.pyplot as plt
import seaborn as sns

colors = sns.color_palette("colorblind")

plt.figure()
plt.scatter(X, y, color=colors[0], label="training samples")
plt.plot(X, y_1, color=colors[1], label="n_estimators=1", linewidth=2)
plt.plot(X, y_2, color=colors[2], label="n_estimators=300", linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.title("Boosted Decision Tree Regression")
plt.legend()
plt.show()
```
