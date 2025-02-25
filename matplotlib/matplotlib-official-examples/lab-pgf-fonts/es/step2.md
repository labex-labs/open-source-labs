# Establecer la familia de fuentes

Estableceremos la familia de fuentes en "serif" utilizando el parámetro `font.family`. Además, estableceremos el parámetro `font.serif` en una lista vacía para usar la fuente serif de LaTeX predeterminada.

```python
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": [],
})
```
