# Definiere Bilddaten

Wir definieren eine Funktion, die ein Beispielbilddatum und seinen Bereich zurückgibt.

```python
def get_demo_image():
    z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # 15x15 array
    return z, (-3, 4, -4, 3)
```
