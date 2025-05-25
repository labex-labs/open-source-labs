# Ocultar _spines_ desnecessários

Você também deseja ocultar os _spines_ superior e direito, pois eles não são necessários.

```python
ax.spines[["top", "right"]].set_visible(False)
```
