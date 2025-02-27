# Ergebnisse plotten

Wir werden die resultierende Projection, die von jeder Methode gegeben wird, plotten.

```python
for name in timing:
    title = f"{name} (time {timing[name]:.3f}s)"
    plot_embedding(projections[name], title)

plt.show()
```
