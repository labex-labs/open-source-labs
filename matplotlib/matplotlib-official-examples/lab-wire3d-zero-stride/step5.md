# Create the second subplot

We will create the second subplot with the `rstride` parameter set to `0` and `cstride` parameter set to `10`.

```python
ax2.plot_wireframe(X, Y, Z, rstride=0, cstride=10)
ax2.set_title("Row (y) stride set to 0")
```
