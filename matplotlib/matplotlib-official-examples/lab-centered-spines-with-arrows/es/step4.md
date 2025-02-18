# Ocultar los ejes (spines) innecesarios

También se desea ocultar los ejes superior y derecho ya que no son necesarios.

```python
ax.spines[["top", "right"]].set_visible(False)
```
