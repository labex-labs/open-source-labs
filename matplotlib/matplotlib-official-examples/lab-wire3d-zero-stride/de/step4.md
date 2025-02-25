# Erstellen des ersten Teilplots

Wir werden den ersten Teilplot erstellen, wobei der Parameter `rstride` auf `10` und der Parameter `cstride` auf `0` gesetzt ist.

```python
ax1.plot_wireframe(X, Y, Z, rstride=10, cstride=0)
ax1.set_title("Column (x) stride set to 0")
```
