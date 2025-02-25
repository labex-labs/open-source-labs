# Erstellen der Figur und der Teilplots

In diesem Schritt erstellen wir eine Figur mit zwei Teilplots für die kumulativen Verteilungen. Wir setzen auch die Größe der Figur auf 9x4.

```python
fig = plt.figure(figsize=(9, 4), layout="constrained")
axs = fig.subplots(1, 2, sharex=True, sharey=True)
```
