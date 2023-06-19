# Create the first subplot

We will create the first subplot with the `rstride` parameter set to `10` and `cstride` parameter set to `0`.

```python
ax1.plot_wireframe(X, Y, Z, rstride=10, cstride=0)
ax1.set_title("Column (x) stride set to 0")
```
