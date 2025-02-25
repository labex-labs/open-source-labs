# Importation des bibliothèques et des données requises

Nous devons tout d'abord importer les bibliothèques requises, qui sont `matplotlib`, `numpy` et `matplotlib.cbook`. Nous devons également charger un tableau enregistré numpy à partir de données csv de Yahoo avec les champs date, ouverture, haut, bas, fermeture, volume, fermeture ajustée à partir du répertoire mpl-data/sample_data. Le tableau enregistré stocke la date sous forme d'un np.datetime64 avec une unité de jour ('D') dans la colonne date. Nous utiliserons ces données pour tracer la série temporelle financière.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

# Charger les données à partir du répertoire sample_data
r = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)
r = r[:9]  # prendre les 9 premiers jours
```
