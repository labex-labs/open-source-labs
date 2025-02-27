# Establecer títulos y etiquetas

Estableceremos los títulos y etiquetas para las subtramas.

```python
    if i == 0:
        axes_row[0].set_title("Penalización L1")
        axes_row[1].set_title("Elastic-Net\nl1_ratio = %s" % l1_ratio)
        axes_row[2].set_title("Penalización L2")

    axes_row[0].set_ylabel("C = %s" % C)
```
