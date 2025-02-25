# Demobild abrufen

In diesem Schritt werden wir eine Funktion definieren, um ein Demobild und seine Ausdehnung abzurufen. Wir werden die Funktion `get_sample_data()` aus `cbook` verwenden, um ein Beispielbild zu erhalten.

```python
def get_demo_image():
    z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # 15x15 array
    return z, (-3, 4, -4, 3)
```
