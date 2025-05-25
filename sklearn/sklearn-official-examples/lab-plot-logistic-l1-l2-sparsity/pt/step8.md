# Definir Títulos e Rótulos

Definiremos os títulos e rótulos dos subgráficos.

```python
    if i == 0:
        axes_row[0].set_title("Penalidade L1")
        axes_row[1].set_title("Rede elástica\nl1_ratio = %s" % l1_ratio)
        axes_row[2].set_title("Penalidade L2")

    axes_row[0].set_ylabel("C = %s" % C)
```
