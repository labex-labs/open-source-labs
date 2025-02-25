# Erstellen des zweiten Teilplots

Wir werden den zweiten Teilplot erstellen, wobei der Parameter `rstride` auf `0` und der Parameter `cstride` auf `10` gesetzt ist.

```python
ax2.plot_wireframe(X, Y, Z, rstride=0, cstride=10)
ax2.set_title("Row (y) stride set to 0")
```
