# Das Kreisdiagramm erstellen

Um das Kreisdiagramm zu erstellen, werden wir die `pie()`-Funktion aus Matplotlib verwenden.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels)
```
