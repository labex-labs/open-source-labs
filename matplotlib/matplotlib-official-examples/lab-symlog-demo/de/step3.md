# Plots erstellen

Jetzt, wo wir unsere Daten haben, können wir unsere Plots erstellen. Wir werden drei Teilplots erstellen, jeder mit einer anderen `symlog`-Achsenskalierung.

```python
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3)
```
