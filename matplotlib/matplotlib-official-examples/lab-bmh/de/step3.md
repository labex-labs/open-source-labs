# Erstellen des Diagramms

In diesem Schritt erstellen wir das Diagramm, indem wir die Funktion `plot_beta_hist()` aufrufen und die Parameter übergeben.

```python
fig, ax = plt.subplots()
plot_beta_hist(ax, 10, 10)
plot_beta_hist(ax, 4, 12)
plot_beta_hist(ax, 50, 12)
plot_beta_hist(ax, 6, 55)
ax.set_title("'bmh' style sheet")

plt.show()
```
