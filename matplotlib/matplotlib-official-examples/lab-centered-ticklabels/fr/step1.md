# Charger les données financières

Tout d'abord, nous devons charger certaines données financières sur le prix d'actions de Google à l'aide de la fonction `cbook.get_sample_data()` de Matplotlib. Nous utiliserons les données des 250 derniers jours.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

# Charger certaines données financières ; le prix d'actions de Google
r = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)
r = r[-250:]  # obtenir les 250 derniers jours
```
