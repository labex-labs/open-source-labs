# Definieren einer Funktion zum Abrufen von RGB-Kanälen

In diesem Schritt definieren wir eine Funktion `get_rgb()`, um die R-, G- und B-Kanäle eines Bildes abzurufen. In diesem Beispiel verwenden wir die `get_sample_data()`-Funktion des `cbook`-Moduls, um ein Beispielbild zu erhalten.

```python
import matplotlib.cbook as cbook

def get_rgb():
    # Holen Sie sich ein Beispielbild
    Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
    Z[Z < 0] = 0.
    Z = Z / Z.max()

    # Holen Sie sich die R-, G- und B-Kanäle
    R = Z[:13, :13]
    G = Z[2:, 2:]
    B = Z[:13, 2:]

    return R, G, B
```
