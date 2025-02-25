# Überlappende Theta-Fehlerbalken erstellen

In diesem Schritt werden wir überlappende Theta-Fehlerbalken erstellen, um zu demonstrieren, wie sie die Lesbarkeit des ausgegebenen Diagramms verringern können.

```python
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(projection='polar')
ax.errorbar(theta, r, xerr=5.25, yerr=0.1, capsize=7, fmt="o", c="darkred")
ax.set_title("Overlappende Theta-Fehlerbalken")
plt.show()
```
