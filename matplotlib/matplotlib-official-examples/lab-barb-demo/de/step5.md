# Maskierten Windbubenplot erstellen

Wir können auch einen maskierten Windbubenplot erstellen, indem wir ein maskiertes Array verwenden. In diesem Fall werden wir den Wert eines Vektors in einen ungültigen Wert umwandeln und ihn maskieren.

```python
masked_u = np.ma.masked_array(U)
masked_u[4] = 1000  # Ungültiger Wert, der nicht geplottet werden soll, wenn maskiert
masked_u[4] = np.ma.masked

plt.barbs(X, Y, masked_u, V, length=8, pivot='middle')
plt.show()
```
