# Graphen erstellen

In diesem Schritt werden wir den Graphen mit den im vorherigen Schritt erstellten maskierten Arrays erstellen. Wir werden jedes maskierte Array separat plotten und für jedes eine andere Farbe verwenden.

```python
fig, ax = plt.subplots()
ax.plot(t, smiddle, t, slower, t, supper)
plt.show()
```
