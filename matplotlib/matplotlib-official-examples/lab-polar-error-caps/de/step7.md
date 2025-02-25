# Große Radius-Fehlerbalken erstellen

In diesem Schritt werden wir große Radius-Fehlerbalken erstellen, um zu demonstrieren, wie sie zu einem unerwünschten Maßstab in den Daten führen können und den angezeigten Bereich verringern.

```python
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(projection='polar')
ax.errorbar(theta, r, xerr=0.25, yerr=10.1, capsize=7, fmt="o", c="orangered")
ax.set_title("Large Radius Error Bars")
plt.show()
```
