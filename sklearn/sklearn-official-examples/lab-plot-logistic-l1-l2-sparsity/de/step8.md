# Setzen von Titeln und Beschriftungen

Wir werden die Titel und Beschriftungen für die Subplots setzen.

```python
    if i == 0:
        axes_row[0].set_title("L1 Strafe")
        axes_row[1].set_title("Elastic-Net\nl1_ratio = %s" % l1_ratio)
        axes_row[2].set_title("L2 Strafe")

    axes_row[0].set_ylabel("C = %s" % C)
```
