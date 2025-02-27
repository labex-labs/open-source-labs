# t-SNE-Ergebnisse visualisieren

Schließlich können wir die t-SNE-Ergebnisse mithilfe eines Scatterplots visualisieren.

```python
ax = plt.subplot(1, 1, 1)
ax.scatter(Y[red, 0], Y[red, 1], c="r")
ax.scatter(Y[green, 0], Y[green, 1], c="g")
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
plt.axis("tight")
```
